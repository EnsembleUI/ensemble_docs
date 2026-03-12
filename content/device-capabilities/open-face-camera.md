# openFaceCamera

Use `openFaceCamera` when you need face-aware capture (for example selfie verification, identity checks, or attendance) instead of generic photo capture.

`openFaceCamera` provides guided framing, face validation, and optional auto-capture once the face qualifies.

## When to use this instead of openCamera

- You need face alignment guidance before capture.
- You need automatic capture when a valid face is detected.
- You need stricter face quality checks, especially on web via `accuracyConfig`.

For generic photo/video capture or gallery-first flows, continue using [`openCamera`](/device-capabilities/open-camera).

## Properties

| Property  | Type   | Description                                                                     |
| :-------- | :----- | :------------------------------------------------------------------------------ |
| id        | string | Camera ID used to bind captured results (for example `${myFaceCamera.files}`). |
| onCapture | action | Executes when an image is captured. Files are available in `event.data.files`. |
| onError   | action | Executes on error. Error message is available via `event.error`.               |
| options   | object | Face camera and detection configuration.                                        |

## options

| Property                  | Type    | Description                                                                     |
| :------------------------ | :------ | :------------------------------------------------------------------------------ |
| initialCamera             | string  | Which lens to start with: `front` (default), `back`                            |
| message                   | string  | Message shown above camera preview                                              |
| messageStyle              | object  | Text style for `message`                                                        |
| showControls              | boolean | Show/hide all camera controls. Default `true`                                   |
| showCaptureControl        | boolean | Show/hide capture button. Default `true`                                        |
| showFlashControl          | boolean | Show/hide flash control. Default `true`                                         |
| showCameraLensControl     | boolean | Show/hide camera switch control. Default `true`                                 |
| showStatusMessage         | boolean | Show/hide face detection status text. Default `true`                            |
| indicatorShape            | string  | Face indicator shape: `circle`, `square`                                        |
| autoDisableCaptureControl | boolean | Disable capture while no valid face is detected. Default `false`                |
| autoCapture               | boolean | Automatically capture when face qualifies. Default `false`                      |
| imageResolution           | string  | Capture resolution: `low`, `medium`, `high`, `veryHigh`, `ultraHigh`, `max`    |
| defaultFlashMode          | string  | Initial flash mode: `off` (default), `auto`, `always`                           |
| orientation               | string  | Camera orientation: `portraitUp`, `portraitDown`, `landscapeLeft`, `landscapeRight` |
| performanceMode           | string  | Face detector mode: `fast` (default), `accurate`                                |
| accuracyConfig            | object  | Fine-grained face detection thresholds. Web only.                               |

## Usage

### Basic

```yaml
- Button:
    label: Open Face Camera
    onTap:
      openFaceCamera:
        id: myFaceCamera
```

### Auto-capture

```yaml
- Button:
    label: Capture verified selfie
    onTap:
      openFaceCamera:
        id: profilePhoto
        options:
          initialCamera: front
          autoCapture: true
          performanceMode: accurate
          message: "Align your face"
        onCapture:
          executeCode:
            body: |
              console.log('Captured face image: ' + profilePhoto.files[0].path);
        onError:
          showToast:
            message: "Error capturing image: ${event.error}"
```

## Full Reference

For complete module setup, advanced `accuracyConfig` fields, and more examples, see [`openFaceCamera` action docs](/actions/open-face-camera).
