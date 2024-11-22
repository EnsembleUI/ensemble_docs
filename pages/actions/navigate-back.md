# Action: navigateBack

The `navigateBack` action allows users to navigate back to the previous screen within the app’s navigation stack. It removes the current screen from the navigation history, so when the user navigates back, the previous screen reappears. This action is also useful when working with modal screens, as it closes the modal and returns the user to the originating screen.

### Properties

| Property | Type   | Description                                                                                                     |
| :------- | :----- | :-------------------------------------------------------------------------------------------------------------- |
| data     | object | Data object to send back to the previous screen. This allows you to pass information back when navigating back. |

---

## Example: Navigating Back

In this example, we use the `navigateScreen` action to navigate to another screen, and then use the `navigateBack` action to return to the previous screen. The `data` is used to send data back to the previous screen when navigating back.

### Source Screen YAML
```yaml
View:
  styles:
    scrollableView: true
  body:
    Column:
      styles:
        padding: 24
      children:
        - Button:
            label: Go to demo screen
            onTap:
              navigateScreen:
                name: navigateBack Demo
                onNavigateBack:
                  showToast:
                    message: ${event.data}
```
### Navigating Screen YAML
```yaml
View:
  styles:
    scrollableView: true
  body:
    Column:
      styles:
        padding: 24
      children:
        - Button:
            label: Go Back
            onTap:
              navigateBack:
                data:
                  message: This is example of data passed when navigating back.

```
### Explanation

1. **Navigate to Another Screen:**  
   First, the user clicks the "Go to demo screen" button, which triggers the `navigateScreen` action, navigating to a new screen called `navigateBack Demo`.

   ```yaml
     - Button:
        label: Go to demo screen
        onTap:
          navigateScreen:
            name: navigateBack Demo
            onNavigateBack:
              showToast:
                message: ${event.data}
   ```
   
2. **Trigger `navigateBack` on the Target Screen:**  
   On the demo screen, there’s a button with the label "Go Back." When this button is pressed, the `navigateBack` action is triggered, sending a data containing a message back to the previous screen:
   ```yaml
   - Button:
      label: Go Back
      onTap:
        navigateBack:
           data:
             message: This is example of data passed when navigating back.
   ```

3. **Access the data on the Originating Screen:**  
   When the user navigates back using the `navigateBack` action, the `onNavigateBack` event is triggered on the source screen. This event gives you access to the data sent during the `navigateBack` action via `event.data`. You can then use this data to perform actions, such as displaying a message with `showToast` or updating other UI elements on the source screen.
   
   ```yaml
     - Button:
        label: Go to demo screen
        onTap:
          navigateScreen:
            name: navigateBack Demo
            onNavigateBack:
              showToast:
                message: ${event.data}
   ```

You can try complete example [here](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/XjvL2XseLnRvYO4FS82e)
