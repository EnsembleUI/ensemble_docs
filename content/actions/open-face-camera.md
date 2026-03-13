# openFaceCamera

`openFaceCamera` action opens the device camera with real-time face detection. It automatically captures an image when the face is properly aligned (position, angle, etc.), making it ideal for selfies, profile photos, or any face-detection task on mobile and web. Use the `id` property to bind the captured image result (e.g. to a variable or data binding).

### Setup in Ensemble Studio

1. Go to https://studio.ensembleui.com/
2. Open your app
3. From the left sidebar, click **Build & Deploy**
4. In the **Build Settings** tab, enable the **Face Camera** module/feature and update.
5. If building for iOS: switch to the **iOS** tab and add the required camera usage description (e.g. "We use the camera to capture your face for verification") and any face-related privacy descriptions


### Properties

| Property      | Type   | Description                                                                       |
| :------------ | :----- | :-------------------------------------------------------------------------------- |
| id            | string | Camera ID used to bind captured results (for example `${myFaceCamera.files}`).   |
| onCapture     | action | Executes when an image is captured. Captured files are available via `event.data.files`. |
| onError       | action | Executes on error. Error message is available via `event.error`.                  |
| options       | object | Additional configuration for camera and detection.                                |

### options

| Property                  | Type    | Description                                                                                       |
| :------------------------ | :------ | :------------------------------------------------------------------------------------------------ |
| initialCamera             | string  | Which lens to start with: `front` (default), `back`                                              |
| message                   | string  | Message shown above camera preview                                                                |
| messageStyle              | object  | Text style for `message`                                                                          |
| showControls              | boolean | Show/hide all camera controls. Default `true`                                                     |
| showCaptureControl        | boolean | Show/hide capture button. Default `true`                                                          |
| showFlashControl          | boolean | Show/hide flash control. Default `true`                                                           |
| showCameraLensControl     | boolean | Show/hide camera switch control. Default `true`                                                   |
| showStatusMessage         | boolean | Show/hide face detection status text. Default `true`                                              |
| indicatorShape            | string  | Face indicator shape: `circle`, `square`                                                          |
| autoDisableCaptureControl | boolean | Disable capture while no valid face is detected. Default `false`                                  |
| autoCapture               | boolean | Automatically capture when face qualifies. Default `false`                                        |
| imageResolution           | string  | Capture resolution: `low`, `medium`, `high` (default), `veryHigh`, `ultraHigh`, `max`            |
| defaultFlashMode          | string  | Initial flash mode: `off` (default), `auto`, `always`                                             |
| orientation               | string  | Camera orientation: `portraitUp` (default), `portraitDown`, `landscapeLeft`, `landscapeRight`    |
| performanceMode           | string  | Face detector mode: `fast` (default), `accurate`                                                  |
| accuracyConfig            | object  | Fine-grained face detection thresholds. Web only. See `options.accuracyConfig` below.            |

### options.accuracyConfig

> Note: `accuracyConfig` is supported only on web.

The following properties are verified in code as parsed and used by web face detection:

| Property                   | Type   | Default | Description                                                                  |
| :------------------------- | :----- | :------ | :--------------------------------------------------------------------------- |
| detectionThreshold         | number | 0.6     | Minimum confidence score for a valid face detection                          |
| intersectionRatioThreshold | number | 0.9     | Minimum overlap ratio between detected face and expected region              |
| extraHeightFactor          | number | 0.3     | Additional height factor for face bounding box                               |
| inputSize                  | number | 224     | Input image size used by detector                                             |
| landmarkRatio              | number | 0.95    | Minimum landmark alignment/visibility ratio                                  |
| frameMargin                | number | 0.05    | Margin ratio to ensure face is not too close to frame edges                 |
| tiltAngleThreshold         | number | 6       | Maximum allowed tilt angle in degrees                                        |
| horizontalCenterTolerance  | number | 0.08    | Allowed horizontal centering tolerance                                       |
| earThreshold               | number | 0.25    | Eye aspect ratio threshold for open-eye validation                           |
| minFaceWidthRatio          | number | 0.18    | Minimum face width ratio relative to frame                                   |
| maxFaceWidthRatio          | number | 0.82    | Maximum face width ratio relative to frame                                   |
| qualityPassThreshold       | number | 0.8     | Minimum quality score required to pass                                       |
| yawLowerThreshold          | number | 0.85    | Lower yaw ratio bound                                                        |
| yawUpperThreshold          | number | 1.15    | Upper yaw ratio bound                                                        |

Alias keys also supported by parser:

- `threshold` -> `detectionThreshold`
- `yaw` -> `yawUpperThreshold`
- `tilt` -> `tiltAngleThreshold`
- `minFaceSize` -> `minFaceWidthRatio`

## Usage Examples

### 1. Basic capture and preview

Open the face camera, bind the result to an ID, and preview the captured image.

```yaml
View:
  header:
    title: "Action: openFaceCamera"
  styles:
    scrollableView: true
  body:
    Column:
      styles: { gap: 16, padding: 24 }
      children:
        - Button:
            label: Open Face Camera
            onTap:
              openFaceCamera:
                id: myFaceCamera

        - Conditional:
            conditions:
              - if: ${myFaceCamera.files.length > 0}
                Image:
                  source: ${myFaceCamera.files[0].path}
```

### 2. Capture with common options

Configure the most common face camera options and log the result when a capture succeeds.

```yaml
- Button:
    label: Open Face Camera with Options
    onTap:
      openFaceCamera:
        id: myFaceCamera
        options:
          initialCamera: front
          performanceMode: fast
          imageResolution: high
          defaultFlashMode: off
          orientation: portraitUp
          message: "Align your face"
          messageStyle:
            color: 0xFFFFFFFF
          indicatorShape: circle
          showStatusMessage: true
          showControls: true
          showCaptureControl: true
          showFlashControl: true
          showCameraLensControl: true
        onCapture:
          executeCode:
            body: |
              console.log('Face camera captured image with id: ' + myFaceCamera.files);
        onError:
          showToast:
            message: "Error capturing image: ${event.error}"
```

### 3. Auto-capture and upload

Automatically capture once the face is valid, then upload the captured file.

```yaml
- Button:
    label: Auto Capture and Upload
    onTap:
      openFaceCamera:
        id: captureMedia
        options:
          autoCapture: true
          performanceMode: accurate
          message: "Hold still for capture"
        onCapture:
          uploadFiles:
            id: uploader
            files: ${captureMedia.files[0]}
            uploadApi: fileUploadApi
            fieldName: file

- Markdown:
    text: ${uploader.body}

API:
  fileUploadApi:
    inputs:
      - url
    uri: ${url}
    method: POST
```

### 4. Web accuracy config

Use strict face detection thresholds for web capture.

```yaml
- Button:
    label: Open Camera (web, strict)
    onTap:
      openFaceCamera:
        id: cameraWithFaceDetection
        options:
          initialCamera: front
          autoCapture: false
          performanceMode: accurate
          accuracyConfig:
            detectionThreshold: 0.5
            intersectionRatioThreshold: 0.9
            extraHeightFactor: 0.6
            inputSize: 224
            landmarkRatio: 0.95
            frameMargin: 0.05
            tiltAngleThreshold: 6
            horizontalCenterTolerance: 0.08
            earThreshold: 0.25
            minFaceWidthRatio: 0.18
            maxFaceWidthRatio: 0.82
            qualityPassThreshold: 0.8
            yawLowerThreshold: 0.85
            yawUpperThreshold: 1.15
          message: "Align your face in the square"
          messageStyle:
            color: "#FF0000"
            fontSize: 20
        onCapture:
          uploadFiles:
            id: uploader
            files: ${cameraWithFaceDetection.files[0]}
            uploadApi: fileUploadApi
            fieldName: file
        onError:
          showToast:
            message: "Error capturing image: ${event.error}"
```

To learn more about openCamera functionalities, test it out here in [Ensemble Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/iLJkHUPgX3ii9EdQ1D8K) app.
