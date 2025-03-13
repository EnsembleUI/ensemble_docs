# No Bounded Width Error

You get the error **"This widget requires a width."** on some widgets.

e.g. TextInput, Map, ...

## Reason

A widget needs a width (and a height) to render. Some widgets can automatically calculate its width based on its content (e.g. Text) or from its children. Others widgets cannot (or should not e.g. what should the width of a Map widget be?). These widgets rely on the parent to constrain (give) them a dimension.

## Solution

1. Set an explicit width or max width on this widget (if applicable).
2. The parent needs to constrain the width of this widget. This can mean setting a width on the parent or force the parent to decide how to distribute the space.
   - For **Row** parent: Row does not constrain the children's widths so consider using *FlexRow* instead. FlexRow will stretch to fill its parent and distribute the available space between its children.
   - For **Stack** parent: Similarly Stack also do not constrain the children's widths. Adjust its stackPositionLeft / stackPositionRight attributes to constrain the children within this width.
   - For **horizontal scrollable** parent: Scrollable parent allows its children to decide their own widths (so it knows how to scroll), meaning all children must be able to calculate their own widths. Consider changing your design if you run into this situation.
