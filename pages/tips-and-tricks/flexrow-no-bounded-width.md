# FlexRow No Bounded Width Error

You get the error **"FlexRow requires a width for child distribution."**

## Reason

FlexRow's layout algorithm works by distributing a pre-defined width proportionally to all its children. If the FlexRow does not have an explicit width, its parent is required to constrain its width. This is a variation of [no-bounded-width](/error/no-bounded-width) error, but specific to FlexRow.

## Solution

1. Set an explicit width on the FlexRow. This width will then be distributed proportionally to its children.
2. The parent (anywhere up the chain) needs to constrain the width of this widget. This can mean either setting a width on the parent or forcing the parent to decide how to distribute the horizontal space.
    - For **horizontal Scrollable** ancestor: Having a FlexRow (stretching to the width of the parent) inside a horizontal Scrollable (width is calculated from all children combined) does not make sense. There has to be an explicit width set at least once in the hierarchy chain between the FlexRow and the Scrollable ancestor.
    - For **Row** ancestor: Row does not constrain its children's widths (it lets the children dictate their own widths). For this reason, ensure there is a width set (can be explicit or stretched to parent) at least once in the hierarchy chain between the FlexRow and the Row ancestor.
      - Consider using all FlexRow(s) instead of Row up the ancestor chain to the root View. This ensure the screen width is distributed properly down to our last FlexRow.
      - If you don't need FlexRow's distribution capability, considered using all Rows instead. Rows lay out their children with their requested widths in a left to right manner, with the ability to add horizontal scrollbar as needed.
