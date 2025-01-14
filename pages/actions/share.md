# Share

Using the native sharing capabilities of the device to provide users with the ability to share text and files.

### Properties

| Property   | Type   | Description                                                                                |
| :--------- | :----- | :----------------------------------------------------------------------------------------- |
| title         | string | Optional title (e.g. email's title)     |
| text          | string | Text and/or URL to share                                                        |
| files         | Files | Files list to share                                        |

**Example**

The share action is triggered when the "Open Share Sheet" button is tapped. It typically opens the native share sheet on the device, allowing users to share content. In this case, it shares a title ("EnsembleUI") and a URL ("https://ensembleui.com/").

```yaml
  - Button:
      label: Open Share Sheet
      onTap:
        share:
          title: EnsembleUI
          text: https://ensembleui.com/
  - Text:
      text: Works only on Native iOS and Android
```

After tapping “Share Files” in the example and selecting files, the ShareAction is triggered to share the chosen files and given text.
```yaml
- Button:
        label: Share Files
        onTap:
          pickFiles:
            id: filePicker
            source: files
            onComplete:
              share:
                files: ${filePicker.files}
                text: I selected this file
```


complete example [here](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/Dnv8CceAHCHlEpS61DEE)
