This widget also inherits these base styles:
| Property | Type | Description |
|------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| visible | boolean | Toggle a widget visibility on/off. Note that an invisible widget will not occupy UI space, unless the visibilityTransitionDuration is specified. |
| visibilityTransitionDuration | number | Specify the duration in seconds when a widget animates between visible and not visible state. Note that setting this value will cause the widget to still occupy the UI space even when it is not visible. |
| opacity | double | Adjusts the opacity of the widget. Values range from 0 (fully transparent) to 1 (opaque). Default is `1`. |
| elevation | integer | The z-coordinate at which to place this material relative to its parent. A non-zero value will show a shadow, with its size relative to the elevation value. (Minimum: 0, Maximum: 24) |
| elevationShadowColor | [Color](/widgets/types#Color) | The shadow color for the elevation. |
| elevationBorderRadius | integer / string | If the widget has a borderRadius, this should be changed to have the same value. Use with CSS-like notation (1 to 4 integers). |
| alignment | [Alignment](/widgets/types#Alignment) | Align this widget relative to its parent. |
| stackPositionTop | integer | The distance of the child's top edge from the top of the stack. This is applicable only for Stack's children. |
| stackPositionBottom | integer | The distance that the child's bottom edge from the bottom of the stack. This is applicable only for Stack's children. |
| stackPositionLeft | integer | The distance that the child's left edge from the left of the stack. This is applicable only for Stack's children. |
| stackPositionRight | integer | The distance that the child's right edge from the right of the stack. This is applicable only for Stack's children. |
| captureWebPointer | boolean | Applicable for Web only. When overlaying widgets on top of certain HTML container (e.g., Maps), the mouse click is captured by the HTML container, causing issue interacting with the widget. Use this to capture and maintain the mouse pointer on your widget. |
| tooltip | object | Configuration object for customizing the tooltip [properties](#Tooltip Properties). |

#### Tooltip Properties
| Property | Type | Description |
|----------|------|-------------|
| message | string | The text message displayed in the tooltip |
| onTriggered | function | Callback triggered when the tooltip is shown |
| styles | object | Contains the following properties: `textStyle`, `verticalOffset`, `preferBelow`, `waitDuration`, `showDuration`, `triggerMode`, `backgroundColor`, `borderRadius`, `padding`, `margin`, `borderColor`, `borderWidth`. |


