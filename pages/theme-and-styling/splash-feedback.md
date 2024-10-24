# Splash Feedback (Touchable Opacity)

The **Splash Feedback** is a visual feedback mechanism that creates a ripple or splash animation when a user interacts with a widget. This effect enhances the user experience by providing immediate visual confirmation that an action, such as a tap or click, has been recognized by the interface.

In many user interfaces, buttons come with a default splash effect, providing instant feedback during interaction. Recognizing the value of this visual feedback, Ensemble introduces the ability to extend the splash effect to other widgets, such as rows, columns, and containers, which don't have a splash effect by default.

[Kitchen Sink Example](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/sXFnorqUvN0l9zfSnTcX)



### Widget List
Following are the list of widgets that support Splash Feedback
| Widget       | Documentation  | Kitchen sink example    |
| ------------ | -------------- | ----------------------- |
| Column       | [Link](/widgets/column)        | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/90a8e4df-5eab-4473-ba10-2ecffc9596b0) |
| FittedColumn | [Link](/widgets/fitted-column) | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/hRFxxoaBePQaLfmoBiIb)  |
| Row          | [Link](/widgets/row)           | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/4bd0d453-c243-429d-a562-93cbc9db38e3) |
| FittedRow    | [Link](/widgets/fitted-row)    | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/fvSONumk7npuTDmIWwis) |
| Flex         | [Link](/widgets/flex)          | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/R3KgxV3UPWb4TjoiPI0U) |
| Stack        | [Link](/widgets/stack)         | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/572ecf3b-b9f2-46f4-960f-ff438e5fa1dc) |
<!-- | Flow         | [Link](/widgets/flow)          | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/3e901fb8-a0e8-4f52-979b-7f5f2547e650) | -->
<!-- | ListView     | [Link](/widgets/listview)      | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/w0Wmu9ZMP4csk7IELSx3) |
| GridView     | [Link](/widgets/gridview)      | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/DX5j2WVQFabmxD9FCD5h) |
| StaggeredGrid | [Link](/widgets/staggeredgrid.md) | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/a9iIs4wvgqDOhU4rN6GR) | -->
<!-- | DataGrid     | [Link](/widgets/data-grid)      | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/c5940e18-f2c1-4318-8e68-a678a6ae7247) |
| TabBar       | [Link](/widgets/tabbar)        | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/cebd491d-7d90-43f4-9f17-b8575de441ca) |
| Carousel     | [Link](/widgets/carousel)      | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/2e1d88b1-f281-4c2c-9bb1-bd18016d2b8c) |
| Divider      | [Link](/widgets/divider)       | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/4a893a2e-5bde-400c-b974-b25b497d31a5) |
| Spacer       | [Link](/widgets/spacer)        | [Link](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/1d7e42a9-5bbc-4b4b-9a02-8c102234ee05)   | -->




## Enable Splash Feedback

To enable splash feedback on a widget, use the `enableSplashFeedback` property in the widget’s styles. Set this property to true to activate the visual effect. However, keep in mind that the splash feedback will only work if the widget is using `onTap` action.

```yaml
Row:
  styles:
    enableSplashFeedback: true
    padding: 10
    borderWidth: 1
  onTap:
    executeCode:
      body: |
        console.log("Enabled Splash Feedback")
```

## Splash Color

To enable splash feedback on a widget, use the `enableSplashFeedback` property in the widget’s styles. Set this property to true to activate the visual effect. However, keep in mind that the splash feedback will only work if the widget is using `onTap` action.

```yaml
Row:
  styles:
    enableSplashFeedback: true
    padding: 10
    borderWidth: 1
  onTap:
    executeCode:
      body: |
        console.log("Enabled Splash Feedback")
```

## Set max and min text scaling

You can continue supporting text scaling, but set max and min for the scaling factor:

## Disable text scaling

To disable text scaling globally across your app, go to your app's theme, and add the following:

```yaml
App:
  textScale:
    enabled: true  # this is the default behavior
    maxFactor: 1.2
    minFactor: 0.8
```

In the above example, text size will be increase by max 20%. E.g. if user selects a scaling factor of 1.5 in the OS settings, the text will no be increased more than 20%.
