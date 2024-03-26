#### Error
You get the error **"FlexColumn requires a height for child distribution."**


#### Reason
FlexColumn's layout algorithm works by distributing a pre-defined height proportionally to all its children. If the FlexColumn does not have an explicit height, its parent is required to constrain its height. This is a variation of [no-bounded-height](/error/no-bounded-height) error, but specific to FlexColumn.

#### Solution
1. Set an explicit height on the FlexColumn. This height will then be distributed proportionally to its children.
2. The parent (anywhere up the chain) needs to constrain the height of this widget. This can mean either setting a height on the parent or forcing the parent to decide how to distribute the vertical space.
    - For **vertical Scrollable** ancestor: Having a FlexColumn (stretch to parent) inside a vertical Scrollable (height is calculated from all children combined) does not make sense. There has to be an explicit height set at least once in the hierarchy chain between the FlexColumn and the Scrollable ancestor. 
    - For **Column** ancestor: Column does not constrain its children's heights (it lets the children dictate their own heights). For this reason, ensure there is a height set (can be explicit or stretched to parent) at least once in the hierarchy chain between the FlexColumn and the Column ancestor. 
      - Consider using all FlexColumn(s) instead of Column up the ancestor chain to the root View. This ensure the screen height is distributed properly down to our last FlexColumn.
      - If you don't need FlexColumn's distribution capability, considered using all Columns instead. Columns lay out their children with their requested heights in a top-down manner, with the ability to add vertical scrollbar as needed.

