#### Error
You get the error **"This widget requires a height."** on some widgets

e.g. Divider (vertical), Map, ...

#### Reason
A widget needs a height (and a width) to render. Some widgets can automatically calculate its height based on its content (e.g. Text with lineHeight of 2) or from its children, while other widgets rely on the parent to constrain (give) them a dimension.

#### Solution
1. Set an explicit height on this widget.
2. The parent needs to constrain the height of this widget. This can mean setting a height on the parent or force the parent to decide how to distribute the vertical space.
    - For **Column** parent: Column does not constrain the children's heights so consider using *FlexColumn* instead. FlexColumn will stretch to fill its parent's height and distribute the available vertical space between its children. Be careful when using FlexColumn inside a scrollable ancestor (all widgets inside a scrollable ancestor need to be able to calculate their own heights).
    - For **Stack** parent: Similarly Stack also do not constrain the children's widths. Adjust its stackPositionTop / stackPositionBottom attributes to constrain the children within this height.
    - For **vertical scrollable** parent: Scrollable parent allows its children to decide their own height (so it knows how to scroll), meaning all children must be able to calculate their own heights. Consider changing your design if you run into this situation.   
