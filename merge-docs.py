import os, json, re

def slugify(text):
    """Convert text to a URL-friendly slug (lowercase, hyphens, no special chars)."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = text.strip().replace(' ', '-')
    text = re.sub(r'-+', '-', text)
    return text

def get_first_heading(file_path):
    """Extract the first markdown heading from a file, skipping YAML frontmatter."""
    heading_text = None
    with open(file_path, 'r', encoding='utf-8') as f:
        in_frontmatter = False
        for line in f:
            line = line.strip()
            if not line or line.startswith("<!--"):
                continue
            if line.startswith("---"):
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter:
                continue
            if line.startswith("#"):
                text = line.lstrip('#').strip()
                if text:
                    heading_text = text
                    break
    return heading_text

def resolve_entry_path(dir_path, name):
    """
    Given a directory and an entry name from _meta.json, try to resolve it to an actual file or directory.
    If name does not exist, try appending .md and then .mdx.
    """
    full_path = os.path.join(dir_path, name)
    if os.path.exists(full_path):
        return full_path
    for ext in ['.md', '.mdx']:
        candidate = full_path + ext
        if os.path.exists(candidate):
            return candidate
    return None

def process_dir(dir_path, skip_index=False):
    """
    Recursively traverse a docs directory following _meta.json for order and grouping.
    Returns a list of nodes that represent pages or groups.
    """
    meta_file = os.path.join(dir_path, "_meta.json")
    entries = []
    if os.path.isfile(meta_file):
        with open(meta_file, 'r', encoding='utf-8') as f:
            meta = json.load(f)
        for key, val in meta.items():
            entries.append((key, val))
    else:
        for name in sorted(os.listdir(dir_path)):
            if name.startswith('_'):
                continue
            entries.append((name, None))
    nodes = []
    for name, title in entries:
        resolved = resolve_entry_path(dir_path, name)
        if resolved is None:
            continue

        # Skip the training-videos file
        base = os.path.basename(resolved).lower()
        if base in ("training-videos.md", "training-videos.mdx"):
            continue

        if os.path.isfile(resolved):
            if skip_index and base in ("index.md", "index.mdx"):
                continue
            page_title = title if isinstance(title, str) else None
            heading_text = get_first_heading(resolved)
            if page_title is None:
                page_title = heading_text if heading_text else name
            if heading_text is None:
                heading_text = page_title
            nodes.append({
                "title": page_title,
                "path": resolved,
                "heading": heading_text
            })
        elif os.path.isdir(resolved):
            group_title = title if isinstance(title, str) else name
            sub_nodes = process_dir(resolved, skip_index=False)
            index_node = next((child for child in sub_nodes 
                               if "path" in child and os.path.basename(child["path"]).lower() in ("index.md", "index.mdx")), None)
            if index_node:
                sub_nodes.remove(index_node)
            group_node = {"title": group_title, "children": sub_nodes}
            if index_node:
                group_node["index_path"] = index_node["path"]
                group_node["heading"] = index_node.get("heading", group_title)
            else:
                group_node["heading"] = group_title
            nodes.append(group_node)
    return nodes

def generate_toc(nodes, depth=0):
    """Generate a nested markdown list for the Table of Contents."""
    toc_lines = []
    indent = "  " * depth
    for node in nodes:
        if "children" in node:
            title = node["title"]
            if node.get("index_path"):
                anchor_text = node.get("heading", title)
                anchor = slugify(anchor_text) if anchor_text else ""
                toc_lines.append(f"{indent}- [{title}](#{anchor})")
            else:
                toc_lines.append(f"{indent}- **{title}**")
            if node["children"]:
                toc_lines += generate_toc(node["children"], depth+1)
        else:
            title = node["title"]
            anchor_text = node.get("heading", title)
            anchor = slugify(anchor_text) if anchor_text else ""
            toc_lines.append(f"{indent}- [{title}](#{anchor})")
    return toc_lines

def clean_content(lines):
    """
    Clean the content lines by:
      - Removing MDX import/export lines.
      - Converting MDX Callout blocks into Markdown note blocks.
      - Removing other MDX component blocks.
      - Fixing markdown and HTML image paths (inserting 'public/' before /images/).
    """
    cleaned = []
    in_code_block = False
    in_callout_block = False
    in_component_block = False
    component_start_pattern = re.compile(r'^\s*<([A-Z][\w]+)')
    # Regex for markdown images: ![alt](/images/...
    md_image_pattern = re.compile(r'(!\[[^\]]*\]\()(/images/)', re.IGNORECASE)
    # Regex for HTML image tags: <img ... src="/images/...
    html_img_pattern = re.compile(r'(<img\s+[^>]*src=["\'])(/images/)', re.IGNORECASE)
    
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            cleaned.append(line)
            continue
        
        if not in_code_block:
            # Process Callout blocks specially:
            if not in_callout_block:
                callout_match = re.match(r'\s*<Callout\s+type="[^"]+"\s*>', line)
                if callout_match:
                    in_callout_block = True
                    cleaned.append("> [!NOTE]")
                    continue
            
            if in_callout_block:
                if "</Callout>" in line:
                    in_callout_block = False
                    continue
                stripped = line.strip()
                if stripped:
                    cleaned.append("> " + stripped)
                else:
                    cleaned.append(">")
                continue

            # For other MDX components, skip them.
            if in_component_block:
                if "</" in line and ">" in line:
                    in_component_block = False
                continue

            if line.lstrip().startswith("import ") or line.lstrip().startswith("export "):
                continue

            comp_match = component_start_pattern.match(line)
            if comp_match:
                in_component_block = True
                continue

            # Fix markdown image paths.
            line = md_image_pattern.sub(r'\1/public/images/', line)
            # Fix HTML image paths.
            line = html_img_pattern.sub(r'\1public/images/', line)
            
        cleaned.append(line)
    return cleaned

def collect_content(nodes, level=1):
    """
    Collect the content of all pages in the nodes, including sections.
    For each file (leaf node), append a separator '---' at the end.
    For group nodes without an index file, do not add an extra heading.
    """
    lines = []
    for node in nodes:
        if "children" in node:
            if node.get("index_path"):
                with open(node["index_path"], 'r', encoding='utf-8') as f:
                    raw = f.read().splitlines()
                section_intro = clean_content(raw)
                lines += section_intro
                if section_intro and section_intro[-1] != "":
                    lines.append("")
                # Add separator after index file of a section.
                lines.append("---")
                lines.append("")
            lines += collect_content(node["children"], level+1)
        else:
            with open(node["path"], 'r', encoding='utf-8') as f:
                raw = f.read().splitlines()
            page_lines = clean_content(raw)
            lines += page_lines
            if page_lines and page_lines[-1] != "":
                lines.append("")
            # Append a separator for each file.
            lines.append("---")
            lines.append("")
    return lines

# Base directory settings
repo_root = os.getcwd()
pages_dir = os.path.join(repo_root, "pages")

# Process the pages directory.
structure = process_dir(pages_dir, skip_index=True)

# Read the root index.mdx content to place it at the beginning.
def resolve_entry_path_custom(dir_path, name):
    """Helper to resolve an index entry from the given dir."""
    for candidate in [name, name + ".md", name + ".mdx"]:
        path = os.path.join(dir_path, candidate)
        if os.path.exists(path):
            return path
    return None

index_path = resolve_entry_path_custom(pages_dir, "index")
index_lines = []
if index_path and os.path.isfile(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        raw_index = f.read().splitlines()
    index_lines = clean_content(raw_index)

# Assemble the final README content.
output_lines = []
if index_lines:
    output_lines += index_lines
    if output_lines and output_lines[-1] != "":
        output_lines.append("")
# Generate the Table of Contents from the sidebar structure.
toc = generate_toc(structure)
if toc:
    output_lines.append("## Table of Contents")
    output_lines.append("")
    output_lines += toc
    output_lines.append("")
# Append the remaining content in the defined order.
output_lines += collect_content(structure)

# Write the merged content to README.md.
with open("README.md", 'w', encoding='utf-8') as out_file:
    out_file.write("\n".join(output_lines))

print("Merged documentation written to README.md")
