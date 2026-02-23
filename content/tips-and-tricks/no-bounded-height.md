# No Bounded Height Error

You get the error **"This widget requires a height."** on some widgets

e.g. Divider (vertical), Map, ...

## Reason

A widget needs a height (and a width) to render. Some widgets can automatically calculate its height based on its content (e.g. Text with lineHeight of 2) or from its children, while other widgets rely on the parent to constrain (give) them a dimension.

## Solution

1. Set an explicit height on this widget.
2. The parent needs to constrain the height of this widget. This can mean either setting a height on the parent or force the parent to decide how to distribute the vertical space.
    - If the parent (or ancestor) is **Column**: Column does not constrain the children's heights so consider using *FlexColumn* instead. FlexColumn will stretch to fill its parent's height and distribute the available vertical space between its children. Be careful when using FlexColumn inside a scrollable ancestor (all widgets inside a scrollable ancestor need to be able to calculate their own heights).
    - If the parent is **Row**: Row does constrain the height (crossAxis) so it alone is **not** a problem. However if the parent of the Row is another Column, the Column will not send the height constraint to the Row, which in turn cannot provide the constraint to its children. If your Row has at least 1 child that has a height, you may explicitly set the height constraint to the tallest child's height using `crossAxisConstraint: largestChild`. This will ensure all children without a height will get the height of the row.
    - For **Stack** parent: Similarly Stack also do not constrain the children's widths. Adjust its stackPositionTop / stackPositionBottom attributes to constrain the children within this height.
    - For **vertical scrollable** parent: Scrollable parent allows its children to decide their own height (so it knows how to scroll), meaning all children must be able to calculate their own heights. Consider changing your design if you run into this situation.
