import os, json, re


def slugify(text):
    """Convert text to a URL-friendly slug (lowercase, hyphens, no special chars)."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = text.strip().replace(" ", "-")
    text = re.sub(r"-+", "-", text)
    return text


def to_sentence_case(s):
    """
    Convert a hyphenated or lower-case string into sentence-case.
    For example, "desktop-app" becomes "Desktop App" and
    "screens-and-widgets" becomes "Screens and Widgets".
    """
    s = s.replace("-", " ")
    words = s.split()
    if not words:
        return s
    minor_words = {"and", "or", "the", "of", "in", "a", "an"}
    # Capitalize first word fully
    result = [words[0].capitalize()]
    for word in words[1:]:
        # Lowercase minor words, capitalize others
        if word.lower() in minor_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)


def get_first_heading(file_path):
    """Extract the first markdown heading from a file, skipping YAML frontmatter."""
    heading_text = None
    with open(file_path, "r", encoding="utf-8") as f:
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
                text = line.lstrip("#").strip()
                if text:
                    heading_text = text
                    break
    return heading_text


def get_description_content(file_path):
    """Extract description content from index file, starting from 'What is Ensemble?' section."""
    with open(file_path, "r", encoding="utf-8") as f:
        in_frontmatter = False
        found_what_is = False
        description_lines = []
        for line in f:
            line_stripped = line.strip()

            # Skip frontmatter
            if line_stripped.startswith("---"):
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter:
                continue

            # Skip HTML comments
            if line_stripped.startswith("<!--"):
                continue

            # Look for "What is Ensemble?" section
            if line_stripped.startswith("## What is Ensemble?"):
                found_what_is = True
                continue

            # If we found the section, collect content until next section or end
            if found_what_is:
                if line_stripped.startswith("##"):  # Next section starts
                    break
                if line_stripped:  # Non-empty line
                    description_lines.append(line_stripped)

        return " ".join(description_lines) if description_lines else None


def get_full_content(file_path):
    """Extract the full content from a file, skipping YAML frontmatter and first heading."""
    with open(file_path, "r", encoding="utf-8") as f:
        content_lines = []
        in_frontmatter = False
        first_heading_skipped = False

        for line in f:
            if line.strip().startswith("---"):
                in_frontmatter = not in_frontmatter
                continue
            if in_frontmatter:
                continue

            # Skip the first heading (starts with #)
            if not first_heading_skipped and line.strip().startswith("#"):
                first_heading_skipped = True
                continue

            content_lines.append(line.rstrip())

    # Join and clean up the content
    content = "\n".join(content_lines).strip()
    # Remove any remaining HTML comments
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    return content


def resolve_entry_path(dir_path, name):
    """
    Given a directory and an entry name from _meta.json, try to resolve it to an actual file or directory.
    If name does not exist, try appending .md and then .mdx.
    """
    full_path = os.path.join(dir_path, name)
    if os.path.exists(full_path):
        return full_path
    for ext in [".md", ".mdx"]:
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
    meta_descriptions = {}

    if os.path.isfile(meta_file):
        with open(meta_file, "r", encoding="utf-8") as f:
            meta = json.load(f)
        for key, val in meta.items():
            if isinstance(val, dict) and "description" in val:
                # Store description for this key
                meta_descriptions[key] = val["description"]
                # Extract title if it exists
                title = val.get("title", key)
                entries.append((key, title))
            else:
                entries.append((key, val))
    else:
        for name in sorted(os.listdir(dir_path)):
            if name.startswith("_"):
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

        # Get description from _meta.json if available
        meta_description = meta_descriptions.get(name)

        if os.path.isfile(resolved):
            if skip_index and base in ("index.md", "index.mdx"):
                continue
            page_title = title if isinstance(title, str) else None
            heading_text = get_first_heading(resolved)
            if page_title is None:
                page_title = heading_text if heading_text else name
            if heading_text is None:
                heading_text = page_title

            nodes.append(
                {
                    "title": page_title,
                    "path": resolved,
                    "heading": heading_text,
                    "meta_description": meta_description,  # Only from _meta.json
                }
            )
        elif os.path.isdir(resolved):
            group_title = title if isinstance(title, str) else name
            sub_nodes = process_dir(resolved, skip_index=False)
            index_node = next(
                (
                    child
                    for child in sub_nodes
                    if "path" in child
                    and os.path.basename(child["path"]).lower()
                    in ("index.md", "index.mdx")
                ),
                None,
            )
            if index_node:
                sub_nodes.remove(index_node)
            group_node = {"title": group_title, "children": sub_nodes}
            if index_node:
                group_node["index_path"] = index_node["path"]
                group_node["heading"] = index_node.get("heading", group_title)
                group_node["meta_description"] = (
                    meta_description  # Only from _meta.json
                )
            else:
                group_node["heading"] = group_title
                group_node["meta_description"] = (
                    meta_description  # Only from _meta.json
                )
            nodes.append(group_node)
    return nodes


def generate_toc(nodes, depth=0):
    """Generate a nested markdown list for the Table of Contents."""
    toc_lines = []
    indent = "  " * depth
    for node in nodes:
        # For directories (groups), convert title to sentence-case.
        if "children" in node:
            title = to_sentence_case(node["title"])
            if node.get("index_path"):
                anchor_text = node.get("heading", title)
                anchor = slugify(anchor_text) if anchor_text else ""
                toc_lines.append(f"{indent}- [{title}](#{anchor})")
            else:
                toc_lines.append(f"{indent}- **{title}**")
            if node["children"]:
                toc_lines += generate_toc(node["children"], depth + 1)
        else:
            title = node["title"]  # For files, assume title is already correct.
            anchor_text = node.get("heading", title)
            anchor = slugify(anchor_text) if anchor_text else ""
            toc_lines.append(f"{indent}- [{title}](#{anchor})")
    return toc_lines


def generate_llms_toc(nodes, base_url="https://docs.ensembleui.com"):
    """Generate table of contents in llms.txt format."""
    lines = []

    for node in nodes:
        if "children" in node:
            # This is a section/group
            section_title = to_sentence_case(node["title"])

            # Add index page if it exists
            if node.get("index_path"):
                title = node.get("heading", section_title)
                rel_path = os.path.relpath(node["index_path"], "pages")
                url_path = (
                    rel_path.replace("\\", "/").replace(".mdx", "").replace(".md", "")
                )
                if url_path == "index":
                    url_path = ""
                elif url_path.endswith("/index"):
                    url_path = url_path[:-6]

                url = f"{base_url}/{url_path}" if url_path else base_url
                meta_description = node.get("meta_description")
                if meta_description:
                    lines.append(f"- [{title}]({url}): {meta_description}")
                else:
                    lines.append(f"- [{title}]({url})")

            # Add child pages
            for child in node["children"]:
                if "path" in child:
                    title = child["title"]
                    rel_path = os.path.relpath(child["path"], "pages")
                    url_path = (
                        rel_path.replace("\\", "/")
                        .replace(".mdx", "")
                        .replace(".md", "")
                    )
                    url = f"{base_url}/{url_path}"
                    meta_description = child.get("meta_description")
                    if meta_description:
                        lines.append(f"- [{title}]({url}): {meta_description}")
                    else:
                        lines.append(f"- [{title}]({url})")
        else:
            # This is a standalone page at root level
            title = node["title"]
            rel_path = os.path.relpath(node["path"], "pages")
            url_path = (
                rel_path.replace("\\", "/").replace(".mdx", "").replace(".md", "")
            )
            url = f"{base_url}/{url_path}"
            meta_description = node.get("meta_description")
            if meta_description:
                lines.append(f"- [{title}]({url}): {meta_description}")
            else:
                lines.append(f"- [{title}]({url})")

    return lines


def collect_all_pages(nodes):
    """Collect all pages from the structure for full content generation."""
    pages = []

    for node in nodes:
        if "children" in node:
            # Add index page if it exists
            if node.get("index_path"):
                pages.append(
                    {
                        "title": node.get("heading", node["title"]),
                        "path": node["index_path"],
                        "url_path": get_url_path(node["index_path"]),
                    }
                )

            # Add child pages
            pages.extend(collect_all_pages(node["children"]))
        else:
            # This is a standalone page
            pages.append(
                {
                    "title": node["title"],
                    "path": node["path"],
                    "url_path": get_url_path(node["path"]),
                }
            )

    return pages


def get_url_path(file_path):
    """Convert file path to URL path."""
    rel_path = os.path.relpath(file_path, "pages")
    url_path = rel_path.replace("\\", "/").replace(".mdx", "").replace(".md", "")
    if url_path == "index":
        url_path = ""
    elif url_path.endswith("/index"):
        url_path = url_path[:-6]
    return url_path


def generate_full_docs(pages, base_url="https://docs.ensembleui.com"):
    """Generate full documentation content in llms-full.txt format."""
    content_blocks = []

    for page in pages:
        title = page["title"]
        file_path = page["path"]
        url_path = page["url_path"]

        url = f"{base_url}/{url_path}" if url_path else base_url

        # Get full content
        full_content = get_full_content(file_path)

        # Format as does: # Title \n Source: URL \n Content
        block = f"# {title}\nSource: {url}\n\n{full_content}\n"
        content_blocks.append(block)

    return content_blocks


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
    component_start_pattern = re.compile(r"^\s*<([A-Z][\w]+)")
    # Regex for markdown images: ![alt](/images/...
    md_image_pattern = re.compile(r"(!\[[^\]]*\]\()(/images/)", re.IGNORECASE)
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

            if line.lstrip().startswith("import ") or line.lstrip().startswith(
                "export "
            ):
                continue

            comp_match = component_start_pattern.match(line)
            if comp_match:
                in_component_block = True
                continue

            # Fix markdown image paths.
            line = md_image_pattern.sub(r"\1/public/images/", line)
            # Fix HTML image paths.
            line = html_img_pattern.sub(r"\1public/images/", line)

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
                with open(node["index_path"], "r", encoding="utf-8") as f:
                    raw = f.read().splitlines()
                section_intro = clean_content(raw)
                lines += section_intro
                if section_intro and section_intro[-1] != "":
                    lines.append("")
                # Add separator after index file of a section.
                lines.append("---")
                lines.append("")
            lines += collect_content(node["children"], level + 1)
        else:
            with open(node["path"], "r", encoding="utf-8") as f:
                raw = f.read().splitlines()
            page_lines = clean_content(raw)
            lines += page_lines
            if page_lines and page_lines[-1] != "":
                lines.append("")
            # Append a separator for each file.
            lines.append("---")
            lines.append("")
    return lines


def resolve_entry_path_custom(dir_path, name):
    """Helper to resolve an index entry from the given dir."""
    for candidate in [name, name + ".md", name + ".mdx"]:
        path = os.path.join(dir_path, candidate)
        if os.path.exists(path):
            return path
    return None


# Base directory settings
repo_root = os.getcwd()
pages_dir = os.path.join(repo_root, "pages")
public_dir = os.path.join(repo_root, "public")

# Ensure public directory exists
os.makedirs(public_dir, exist_ok=True)

# Process the pages directory.
structure = process_dir(pages_dir, skip_index=True)

# Read the root index.mdx content to place it at the beginning.
index_path = resolve_entry_path_custom(pages_dir, "index")
index_lines = []
main_title = "Ensemble"
main_description = "Documentation for the Ensemble platform"

if index_path and os.path.isfile(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        raw_index = f.read().splitlines()
    index_lines = clean_content(raw_index)

    # Extract title for llms.txt
    title_from_index = get_first_heading(index_path)
    if title_from_index:
        main_title = title_from_index

    # Extract description for llms.txt
    description_content = get_description_content(index_path)
    if description_content:
        main_description = description_content

# Generate README.md
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
with open("README.md", "w", encoding="utf-8") as out_file:
    out_file.write("\n".join(output_lines))

print("Merged documentation written to README.md")

# Generate llms.txt (table of contents)
toc_lines = []
toc_lines.append(f"# {main_title}")
toc_lines.append("")
toc_lines.append(f"{main_description}")
toc_lines.append("")
toc_lines.append("## Docs")
toc_lines.append("")

# Generate TOC links
toc_content = generate_llms_toc(structure)
toc_lines.extend(toc_content)

# Add optional section at the end
toc_lines.append("")
toc_lines.append("## Optional")
toc_lines.append("")
toc_lines.append("- [Website](https://ensembleui.com/)")
toc_lines.append("- [Ensemble Studio](https://studio.ensembleui.com/)")
toc_lines.append("- [Chat with us on Discord](https://discord.gg/cEHkJTmn75)")
toc_lines.append(
    "- [Join our office hours](https://discord.gg/eJrUWhnRHS?event=1218554330765066310)"
)
toc_lines.append("- [Drop us an email](mailto:hello@ensembleui.com)")

# Write llms.txt
llms_txt_path = os.path.join(public_dir, "llms.txt")
with open(llms_txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(toc_lines))

# Generate llms-full.txt (full content)
all_pages = collect_all_pages(structure)
full_content_blocks = generate_full_docs(all_pages)

# Prepend only the title and description section to llms-full.txt (not the full TOC)
header_section = []
header_section.append(f"# {main_title}")
header_section.append("")
header_section.append(f"{main_description}")
header_section.append("")
header_section.append("---")  # Add separator before full content
header_section.append("")

# Combine header with full content
full_content_with_header = header_section + full_content_blocks

llms_full_txt_path = os.path.join(public_dir, "llms-full.txt")
with open(llms_full_txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(full_content_with_header))

print(f"Generated {llms_txt_path} successfully!")
print(f"Generated {llms_full_txt_path} successfully!")
print(f"Total pages in full docs: {len(all_pages)}")
