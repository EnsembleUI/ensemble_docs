# navigateViewGroup

navigateViewGroup action allows users to navigate between menu items while maintaining the menu in place. This simulate the experience when user taps on different nav items.

To use this action, first create your [ViewGroup](/screens-and-widgets/screen-structure#view-group).

### Properties

| Property       | Type    | Description                                                                             |
| :------------- | :------ | :-------------------------------------------------------------------------------------- |
| viewIndex      | integer | The index of the menu item to navigate to, starting from 0                              |
| name           | string  | The name of the ViewGroup. This is the name given to the screen when it was created. If the current screen is part of the ViewGroup, name is not required.  |


### Example


Given the following ViewGroup, named `home`:

```yaml
ViewGroup:
  BottomNavBar:
    items:
      - label: Screen1
        icon:
          name: home
        page: NavigateViewGroupScreen1
      - label: Screen2
        icon:
          name: input
        page: NavigateViewGroupScreen2
      - label: Screen3
        icon:
          name: settings
        page: NavigateViewGroupScreen3

```

Use the `navigateViewGroup` action to nvaigate between the tabs without dismissing the menu. 


```yaml
View:
  styles:
    scrollableView: true
    backgroundColor: 0xFFA2728D

  header:
    title: Screen 2
    styles:
      backgroundColor: 0xFFA2728D

  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
        - Button:
            label: Go to NavigateViewGroupScreen1
            onTap:
              navigateViewGroup:
                name: home
                viewIndex: 0

        - Button:
            label: Go to NavigateViewGroupScreen3
            onTap:
              navigateViewGroup:
                name: home
                viewIndex: 2
```


This action will ensure that the menu renders when you navigate to the target screen. In contrast, using `navigateScreen` action will result in only displaying the new screen without the menu.
