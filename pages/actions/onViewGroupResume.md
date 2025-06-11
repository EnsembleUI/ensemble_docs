# Action: onViewGroupResume

The `onViewGroupResume` action allows users to execute actions when navigate back to the viewGroup within the app’s navigation stack. when the user navigates back, the ViewGroup reappears and action specified under `onViewGroupResume` is executed. This action is useful when working with all type of menus.

### Properties

| Property | Type   | Description                                                                                                     |
| :------- | :----- | :-------------------------------------------------------------------------------------------------------------- |
| Action     | ensemble action | Any ensemble action that'll be executed when navigating back to ViewGroup. Such as `executeCode`, `showDialog`, `showToast` etc. |


## Example: onViewGroupResume

In this example, we use the `navigateScreen` action to navigate to another screen, and then use the `onViewGroupResume` action to execute any user specified action while returning to screen.

### Originating Screen

```yaml
ViewGroup:
  onViewGroupResume:
    showDialog:
      body:
        Text:
          text: onViewGroupResume executed
  BottomNavBar:
    items:
      - label: Screen1
        icon:
          name: home
        page: onViewGroupResume1
      - label: Screen2
        icon:
          name: input
        page: onViewGroupResume2
      - label: Screen3
        icon:
          name: settings
        page: onViewGroupResume3

```

### Pushed Screen

```yaml
View:
  styles:
    useSafeArea: true
  header:
    titleText: Overlay
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
        - Text:
            text: This is overlay screen

        - Button:
            label: Tap to Navigate Back to ViewGroup
            onTap:
              navigateBack:
```
### Explanation

1. **Navigate to Another Screen:**  
   First, the user clicks the "Go to another screen" button, which triggers the `navigateScreen` action, navigating to a new screen called `overlay`.

   ```yaml
     - Button:
        label: Go to another screen
        onTap:
          navigateScreen:
            name: overlay
   ```
   
2. **Trigger `onViewGroupResume` on the ViewGroup screen:**  
   On the overlay screen, there’s a button with the label "Go Back." When this button is pressed, the `onViewGroupResume` action is triggered, executing any action provided on ViewGroup screen:
   ```yaml
    - Button:
        label: Tap to Navigate Back to ViewGroup
        onTap:
            navigateBack:
   ```


You can try complete example [here](https://studio.ensembleui.com/app/2Mc1NI4RQlrEH23sU288/screens)
