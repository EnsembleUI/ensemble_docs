# showBottomModal

The `showBottomModal` action enables the display of content on a modal that slides from the bottom of the device, providing a user experience similar to iOS Sheets.

```yaml
    - Button:
        label: Show Modal Using Code
        onTap:
            showBottomModal:
                widget: 
                    ActionsSheet:
                    inputs:
                        action1: Action 1
                        action2: Action 2
                styles: 
                    backgroundColor: white
                    barrierColor: 0x22000000
                options: 
                    enableDrag: true
                    enableDragHandler: true
```

The `showBottomModal` action is configured to call an `ActionsSheet` widget with two inputs: `action1` and `action2`. These inputs are then utilized within the `ActionsSheet` widget to customize its content.

## Properties

| Property      | Type      | Description  |
|:--------------|:----------|:-------------|
| widget        | [Widget](/widgets/) | Constructs the UI of the bottom modal using widgets. |
| styles        | [Styles](#styles) | Applies styles to customize the appearance of the modal. |
| options       | [Options](#options) | Offers customization options for the modal behavior. |
| onDismiss     | Action  | Execute predefined functions or custom code on modal dismiss. |

## Styles

| Property      | Type      | Description  |
|:--------------|:----------|:-------------|
| backgroundColor | string | Set the background color of the modal. |
| barrierColor | string | Sets the color of the barrier behind the modal. |

## Options

| Property      | Type      | Description  |
|:--------------|:----------|:-------------|
| enableDrag | boolean | Enable the user to drag the modal up and down. |
| enableDragHandler | boolean | Determines whether the drag handler is displayed. |
