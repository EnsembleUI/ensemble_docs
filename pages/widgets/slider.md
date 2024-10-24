# Slider widget

The Slider Widget enables users to select a value or a range of values by sliding a handle along a track. It provides a smooth and intuitive interface for adjusting numeric inputs, such as volume, brightness, or any adjustable parameters within your application.

[Test in Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/HvLk8sZ0mTmgppQbp4Zk)

## Examples:

### Slider without Divisions:

```yaml
Slider:
  id: sliderOne
  min: 0
  max: 10
  onChange: |
    sliderOneValue.text = "Slider is set to " + this.value;
```

### Slider with Divisions:

```yaml
Slider:
  id: sliderTwo
  label: Slider with divisions
  min: 0
  max: 10
  divisions: 10
  initialValue: 2
  onChange: |
    sliderTwoValue.text = "Slider is set to " + this.value;
```

## Properties

| Property     | Type    | Description                                                                                                                                                                                              |
| :----------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id           | string  | ID to be referenced later                                                                                                                                                                                |
| className    | string  | A custom class name that can be applied to the slider for additional styling and customization.                                                                                                          |
| label        | string  | Label for your widget                                                                                                                                                                                    |
| labelHint    | string  | Hint text on your label                                                                                                                                                                                  |
| required     | boolean | Whether the field is required                                                                                                                                                                            |
| enabled      | boolean | Enables or disables the interactivity and input functionality of the widget                                                                                                                              |
| initialValue | integer | The initial integer value of the slider, representing the default starting position of the slider handle.                                                                                                |
| max          | integer | The maximum integer value that the slider can reach, defining the upper limit of the slider range.                                                                                                       |
| min          | integer | The minimum integer value that the slider can reach, defining the lower limit of the slider range.                                                                                                       |
| divisions    | integer | The number of discrete steps or segments on the slider, dividing the track into equal intervals.                                                                                                         |
| icon         | object  | [See properties](#icon)                                                                                                                                                                                  |
| styles       | object  | [See properties](#styles)                                                                                                                                                                                |
| onChange     | action  | Call Ensemble's built-in functions or execute code when the slider value changes. This event triggers whenever the slider handle is moved to a new position.  |

### icon

| Property | Type              | Description                                                                                                                                                                                                                                                                                                                         |
| :------- | :---------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name     | string            | The name of the icon                                                                                                                                                                                                                                                                                                                |
| library  | string            | Which icon library to use.                                                                                                                                                                                                                                                                                                          |
| color    | integer or string | The color specification for the text, which can be represented in different formats. It can be specified as a number, a predefined color name, or a hexadecimal value starting with '0x'. `transparent` `black` `blue` `white` `red` `grey` `teal` `amber` `pink` `purple` `yellow` `green` `brown` `cyan` `indigo` `lime` `orange` |
| size     | integer           | Defines the dimensions or magnitude of an element, allowing control over its overall size within the layout.                                                                                                                                                                                                                        |

### styles

| Property                     | Type              | Description                                                                                                                                                                                                                                                                                                                                   |
| :--------------------------- | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| expanded                     | boolean           | If the parent is a Row or Column, this flag will stretch this widget in the appropriate direction. (e.g stretch horizontally for parent of type Row)                                                                                                                                                                                          |
| fillColor                    | integer or string | The fill color for this input fields. This property can be defined in the theme to apply to all Input widgets, starting with '0xFF' for full opacity. `transparent` `black` `blue` `white` `red` `grey` `teal` `amber` `pink` `purple` `yellow` `green` `brown` `cyan` `indigo` `lime` `orange`                                               |
| borderRadius                 | integer           | The border radius for this Input widget. This property can be defined in the theme to apply to all Input widgets.                                                                                                                                                                                                                             |
| maxWidth                | integer                                        | The max width of this Input widget (default 700). while min vlaue can be `0` and maximum can be `5000`                                                                                                                            |
| borderWidth                  | integer           | The border width for this Input widget. This property can be defined in the theme to apply to all Input widgets.                                                                                                                                                                                                                              |
| borderColor                  | integer or string | Sets the border color, starting with '0xFF' for full opacity. `transparent` `black` `blue` `white` `red` `grey` `teal` `amber` `pink` `purple` `yellow` `green` `brown` `cyan` `indigo` `lime` `orange`                                                                                                                                       |
| backgroundColor    | integer or string | Background color of the box. which can be represented in different formats. It can be specified as a number, a predefined color name, or a hexadecimal value starting with '0x'. `transparent` `black` `blue` `white` `red` `grey` `teal` `amber` `pink` `purple` `yellow` `green` `brown` `cyan` `indigo` `lime` `orange`                              |
| visible                      | boolean           | Toggle a widget visibility on/off. Note that an invisible widget will not occupy UI space, unless the visibilityTransitionDuration is specified.                                                                                                                                                                                              |
| textDirection                      | string           | `leftToRight` `rightToLeft`                                                                                                                                                                                              |
| labelStyle              | [TextStyle](/widgets/types#TextStyle) | Styling for the label                                                                                                                                                                                                             |
| visibilityTransitionDuration | number            | Specify the duration in seconds when a widget animates between visible and not visible state. Note that setting this value will cause the widget to still occupy the UI space even when it is not visible.                                                                                                                                    |
| stackPositionTop             | integer           | The distance of the child's top edge from the top of the stack. This is applicable only for Stack's children.                                                                                                                                                                                                                                 |
| stackPositionBottom          | integer           | The distance that the child's bottom edge from the bottom of the stack. This is applicable only for Stack's children.                                                                                                                                                                                                                         |
| stackPositionLeft            | integer           | The distance that the child's left edge from the left of the stack. This is applicable only for Stack's children.                                                                                                                                                                                                                             |
| stackPositionRight           | integer           | The distance that the child's right edge from the right of the stack. This is applicable only for Stack's children.                                                                                                                                                                                                                           |
| alignment                    | string            | The alignment of the widget relative to its parent. `topLeft`, `topCenter`, `topRight`, `centerLeft`, `center`, `centerRight`, `bottomLeft`, `bottomCenter`, `bottomRight`                                                                                                                                                                    |
| elevation                    | integer           | The z-coordinate at which to place this material relative to its parent. A non-zero value will show a shadow, with its size relative to the elevation value. Minimum value: 0, Maximum value: 24                                                                                                                                              |
| elevationShadowColor         | integer or string | The shadow color for the elevation, which can be represented in different formats. It can be specified as a number, a predefined color name, or a hexadecimal value starting with '0x'. `transparent` `black` `blue` `white` `red` `grey` `teal` `amber` `pink` `purple` `yellow` `green` `brown` `cyan` `indigo` `lime` `orange`             |
| elevationBorderRadius        | string or integer | The border radius of the widget.This can be specified using CSS-like notation with 1 to 4 integers. Minimum value: 0.                                                                                                                                                                                                                         |
| captureWebPointer            | boolean           | Applicable for Web only. When overlaying widgets on top of certain HTML container (e.g. Maps), the mouse click is captured by the HTML container, causing issue interacting with the widget. Use this to capture and maintain the mouse pointer on your widget.                                                                               |
