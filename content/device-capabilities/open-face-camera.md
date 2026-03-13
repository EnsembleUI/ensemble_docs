# openFaceCamera

Use `openFaceCamera` when you need **real-time** face detection — such as selfies, profile photos etc — instead of plain camera access.

It adds face detection, alignment guidance (framing overlay), status messages, and optional **auto-capture** when the face meets quality criteria.

### When to use this instead of `openCamera`

- You want visual guidance to center and align the face before capture
- You need automatic capture once a valid face is detected
- You want stricter face quality rules (especially on web with `accuracyConfig`)

### Key Properties

| Property   | Type   | Description                                                                 |
|------------|--------|-----------------------------------------------------------------------------|
| id         | string | Bind captured result (access via `${yourId.files}`)                         |
| onCapture  | action | Runs after successful capture (`event.data.files` available)                |
| onError    | action | Handles errors (`event.error` available)                                    |
| options    | object | Controls camera lens, UI, auto-capture, resolution, flash, and detection    |

### Quick Examples

**Basic face capture**

```yaml
- Button:
    label: Open Face Camera
    onTap:
      openFaceCamera:
        id: myFace
```
**Auto-capture verified selfie**

```yaml
- Button:
    label: Capture Verified Selfie
    onTap:
      openFaceCamera:
        id: profilePhoto
        options:
          initialCamera: front
          autoCapture: true
          message: "Align your face in the frame"
          performanceMode: accurate
        onCapture:
          showToast:
            message: "Selfie captured!"
        onError:
          showToast:
            message: "Capture failed: ${event.error}"
```

To learn more about openCamera functionalities, test it out here in [Ensemble Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/iLJkHUPgX3ii9EdQ1D8K) app.
