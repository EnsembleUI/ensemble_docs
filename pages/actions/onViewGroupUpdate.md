# Action: onViewGroupUpdate

The `onViewGroupUpdate` action allows users to execute actions when update to the ViewGroup occurs. This action is useful when working with all type of menus.

### Properties

| Property | Type   | Description                                                                                                     |
| :------- | :----- | :-------------------------------------------------------------------------------------------------------------- |
| Action     | ensemble action | Any ensemble action that'll be executed when there's update in ViewGroup. Such as `executeCode`, `showDialog`, `showToast` etc. |


## Example: onViewGroupUpdate

In this example, we use the `onViewGroupUpdate` action to execute when viewGroup is updated.

### ViewGroup

```yaml
ViewGroup:
  BottomNavBar:
    items:
      - label: Screen1
        icon:
          name: home
        page: onViewGroupupdate1
      - label: Screen2
        icon:
          name: input
        page: onViewGroupUpdate2
      - label: Screen3
        icon:
          name: settings
        page: onViewGroupUpdate3

```

### Action execution View

```yaml
View:
  onViewGroupUpdate:
    showDialog:
       body:
        Text: text 
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

1. **ViewGroup update:**  
   First, the user clicks the any menu button, which triggers the `onViewGroupUpdate` action, navigating to selected screen.

   
2. **Trigger `onViewGroupUpdate` on the View screen:**  
   On the selected screen, the action specified is triggered automatically. Executing the action specified under `onViewGroupUpdate`.


You can try complete example [here](https://studio.ensembleui.com/app/2Mc1NI4RQlrEH23sU288/screens)
