# Share

Using the native sharing capabilities of the device to provide users with the ability to share text and files.

### Properties

| Property   | Type   | Description                                                                                |
| :--------- | :----- | :----------------------------------------------------------------------------------------- |
| title         | string | Optional title (e.g. email's title)     |
| text          | string | Text and/or URL to share                                                        |
| files         | string | Binded files from sources like camera or picker. e.g ${filePicker.files}, ${camerId.files}                                        |

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
**Share Sheet Screenshot**
<div style="display: flex; flex-direction: column; align-items: center; margin-top: 10px;">
  <img src="/images/actions/sharesheetiphone.png" style="text-align: center;" alt="Output Screenshot" width="250"/>
  <p>Clicking the "Open Share Sheet" will open share sheet to share the provided text and title</p>
</div>

Here's the example of how you can share files using `share` action
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
