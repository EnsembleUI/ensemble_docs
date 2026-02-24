# Screen Navigation

Ensemble provides two primary mechanism for navigating between screens:

1. App menu, i.e. the nav bar, as [described here](/screens-and-widgets/screen-structure#menu)
2. Navigation actions, which we will cover here.

## The navigation stack

The navigation stack keeps track of the screens as they are pushed and popped off the stack.

For example, your app could have a home screen, that navigates to listing screen. From the listing user can navigate to a detail screen. When you navigate to a new screen, that screen is pushed onto the top of the stack.


![navigation stack](/images/navigation/nav-navigation-stack.jpg)

When you navigate back, the topmost screen is popped off the stack, and the previous screen becomes visible Navigation stack follows the Last In, First Out (LIFO) principle, meaning the last screen that was navigated to is the first one to be navigated away from when the user presses the back button.

![navigation stack](/images/navigation/nav-navigation-stack-pop.jpg)

## Navigate Screen action

[navigateScreen reference](/actions/navigate-screen)

Use `navigateScreen` action when navigating to a screen. This action will push the target screen on top of the current screen. You can pass inputs to the target screen when performing this action:

```yaml
- Button:
    label: View details
    onTap:
      navigateScreen:
        name: ProductDetails
        inputs:
          productId: ${product.id}
```

![navigation stack](/images/navigation/nav-navigateScreen.jpg)


Optionally, you can set `onNavigateBack` property to perform an action when user goes back to previous screen.

```yaml
- Button:
    label: View details
    onTap:
      navigateScreen:
        name: ProductDetails
        inputs:
          productId: ${product.id}
        onNavigateBack:
          showToast:
            message: You just returned from product detail screen.
```

In use cases where you do not want to allow user to go back to the previous screen, use `clearAllScreens: true` option. This essentially clears the navigation stack.

```yaml
- Button:
    label: SIGN IN
    onTap:
      invoteAPI:
        name: authenticateUser
        onResponse:
          navigateScreen:
            name: Home
            options:
              clearAllScreens: true
```

![navigation stack](/images/navigation/nav-navigateBack-clearAllScreens.jpg)


## Navigate back action

[navigateBack reference](/actions/navigate-back)

Use `navigateBack` to pop the current screen and go the previous screen in the stack. This is the same action that would be preformed when user taps the built-in back button.

![navigation stack](/images/navigation/nav-navigateBack.jpg)