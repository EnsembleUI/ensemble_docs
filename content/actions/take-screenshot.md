# takeScreenshot

takeScreenshot action allows you to capture a screenshot of read-only widgets using its widgetId. The screenshot is saved to the gallery on mobile platforms or downloaded directly on the web, while also providing the image bytes for further use. It's an efficient solution for exporting visual content in high quality.
### Properties

| Property   | Type   | Description                                                                                |
| :--------- | :----- | :----------------------------------------------------------------------------------------- |
| widgetId   | string | The ID of the target widget to be captured as a screenshot.          |
| onSuccess  | action | Action to be excecuted on successful screenshot capture.                                     |
| onError    | action | Action to be excecuted on error during screenshot capture.|

### Event Data

When the `onSuccess` action is executed, the following data is available under `event.data`:

- **imageBytes**: Provides bytes of the screenshot.
- **size**: Provides total size of image in bytes, e.g. if screenshot has size of 1KB then `size` will return 1024.
- **dimensions**: Provides dimentions of the image as `dimensions.width` and `dimensions.height`

When the `onError` action is executed, the following data is available under `event.data`:

- **error**: Error message describing the issue.
- 

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
