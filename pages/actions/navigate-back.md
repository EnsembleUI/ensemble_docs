# Action: navigateBack

The `navigateBack` action allows users to navigate back to the previous screen within the app’s navigation stack. It removes the current screen from the navigation history, so when the user navigates back, the previous screen reappears. This action is also useful when working with modal screens, as it closes the modal and returns the user to the originating screen.

### Properties

| Property | Type   | Description                                                                                                     |
| :------- | :----- | :-------------------------------------------------------------------------------------------------------------- |
| payload  | object | Data object to send back to the previous screen. This allows you to pass information back when navigating back. |

---

## Example: Navigating Back

In this example, we use the `navigateScreen` action to navigate to another screen, and then use the `navigateBack` action to return to the previous screen. The `payload` is used to send a message back to the previous screen when navigating back.

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
                payload:
                  message: This is the payload

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
   
2. **Trigger `navigateBack` on the New Screen:**  
   On the demo screen, there’s a button with the label "Go Back." When this button is pressed, the `navigateBack` action is triggered, sending a payload containing a message back to the previous screen. Following is the ELD of `navigateBack Demo` screen:
   ```yaml
   - Button:
      label: Go Back
      onTap:
        navigateBack:
          payload:
            message: This is the payload
   ```

3. **Access the Payload on the Source Screen:**  
   When the user navigates back using the `navigateBack` action, the `onNavigateBack` event is triggered on the source screen. This event gives you access to the payload sent during the `navigateBack` action via `event.data`. You can then use this data to perform actions, such as displaying a message with `showToast` or updating other UI elements on the source screen.
   
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
