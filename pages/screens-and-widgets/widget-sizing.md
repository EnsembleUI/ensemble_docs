# Understanding Widget Sizing
Widget sizing is a crucial aspect of building responsive UIs in Ensemble. In this guide, we'll explore the challenges of widget sizing, common solutions, and best practices to help you create layouts that look great on any screen.

## Core Concepts
#### Parent Constraints
In Ensemble, widget sizing is governed by a system of constraints passed down from parent widgets to their children. These constraints define the minimum and maximum sizes a widget can take on the screen.

Starting from the root (the screen dimension), constraints are passed down the layout tree to determine the size of each widget. Most widgets, if themselves receive constraints from their parent, will recalculate the constraints (e.g. subtract padding from the available space) and pass them down to their children. A widget may come up with its own size, but it will always be bounded by the constraints provided by its parent.

**Note**: *Row does not provided the **width constraint** to its children. Any children of Row must be able to determine their own width, or an error may occur. Similarly Column does not provide the **height constraint** to its children.*

**Note**: *Scrollable widgets (e.g ListView, Screen with scrollableView = true) do not provide constraints to their children in the scrollable direction.*

**Note**: *Any widget that does not receive constraints from its parent will not be able to pass the constraints down to its children.*


#### Widget with Intrinsic Sizes
Some widgets can automatically determine their own dimensions based on their content or specific properties. These widgets are straightforward to use because they require minimal configuration to look right.

**Examples:** Text, Image, Icon, ..
```yaml
# Text sizes itself based on the text and the applied styles
Text:
  text: Hello Ensemble !
  styles:
    fontSize: 16
```
**Note**: *just because a widget can determine its own size doesn't mean it will get the size it needs. The final sizing will be bounded by the constraints (minimum/maximum width and minimum/maximum height) provided by the parent widget.*

#### Widgets without Intrinsic Sizes
Conversely, some widgets cannot determine their sizes. These widgets rely on their parent to provide the sizing constraints. Without the constraint an error will occur, and the system will attempt to give you warnings. If the warning system misses this, the screen may be rendered as a blank screen.

**Examples:** Divider, Map, TextInput (width), ..
```yaml
# Column does not provide height constraint to its children,
# so Map will not have a height and cannot be rendered
Column:
  children:
    - Map:
```

## Sizing Challenges and Solutions
**Challenge 1**: Managing Unbounded Sizes<br>
When a widget does not have an intrinsic size nor receives explicit constraints from its parent, it faces an "unbounded size" problem.

<u>Example</u>: When a TextInput is inside a Row.<br>
TextInput does not have a width and rely on the parent to provide a width constraint, which the Row does not provide.<br>
<u>Solution</u>: Set the width on the TextInput, or use FlexRow as the parent. FlexRow will stretch itself to fill its parent's width constraint, and in turn provide a constraint to the TextInput.

<u>Example</u>: When a FlexColumn is inside a 'Screen with scrollableView=true'.<br>
A FlexColumn doesn't calculate its height from the children so it does not have a height. Instead it will attempt to stretch to fill the available height constraint provided by the parent. This will produce an error since the scrollable Screen cannot provide a height constraint.<br>
<u>Solution</u>: Ensure every widget in a scrollable direction has a size. In this case simply use a Column instead of a FlexColumn. A Column will calculate its height from the children, forgo the need for a height constraint.
