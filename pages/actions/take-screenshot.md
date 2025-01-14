# takeScreenshot

takeScreenshot action allows you to capture a screenshot of read-only widgets using its widgetId. The screenshot is saved to the gallery on mobile platforms or downloaded directly on the web, while also providing the image bytes for further use. It's an efficient solution for exporting visual content in high quality.
### Properties

| Property   | Type   | Description                                                                                |
| :--------- | :----- | :----------------------------------------------------------------------------------------- |
| widgetId   | string | The ID of the widget to capture a screenshot of.          |
| onComplete | action | Execute another Action upon successfully taking screenshot.                                     |
| onError    | action | Execute an Action when taking screenshot fails with error(s)                                        |


**Example**



```yaml
View:
  styles:
    scrollableView: true
  header:
    title: "Action: takeScreenshot"

  Column:
    styles:
      gap: 16
      padding: 24
    children:
      - Column:
          id: section1
          styles:
            gap: 16
          children:
            - Button:
                label: Test Button 1
            - Button:
                label: Test Button 2
        # Take Screenshot using `takeScreenshot` action
      - Button:
          label: Take Screenshot
          onTap:
            takeScreenshot:
              widgetId: ${section1}
              onSuccess:
                executeCode:
                  body: |
                    console.log(event.data.imageBytes)
                    console.log(event.data.size)
                    console.log(event.data.dimensions)

        # Take Screenshot using ensemble object in JavaScript `ensemble.takeScreenshot`
      - Button:
          label: Take Screenshot with JS
          onTap:  
             executeCode:
                body: |
                   ensemble.takeScreenshot({widgetId: section1})
```



complete example [here](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/C3zALhZvHQHyFISY9Yvo)
