# openCamera

`OpenCamera` action enables users to access their device's camera, capturing images or videos directly from the app, enhancing interactivity and enabling seamless integration of media functionalities within the application. With `id` property we can bind results of camera. Then use the `onComplete` properties to execute other actions after capture or selection is done.

### Properties

| Property      | Type   | Description                                                                        |
| :---------    | :----- | :--------------------------------------------------------------------------------- |
| id            | string | Give the camera an ID, allows you to bind to its result. e.g. ${cameraId.files...} |
| onComplete    | action | Execute an Action after completing capturing media                                 |
| onClose       | action | Execute an Action on camera close                                                  |
| onCapture     | action | Execute an Action on each capture                                                  |
| options       | object | different options to chose for `openCamera` action. [see properties](#)            |
| overlayWidget | widget | Custom overlay Widget to display over camera.                                      |
| loadingWidget | widget | Custom widget to show for loading indicator in camera.                             |

#### properties.options

| Property                | Type    | Description                                                                                                                    |
| :---------------------- | :------ | :----------------------------------------------------------------------------------------------------------------------------- |
| mode                    | string  | Modes of camera. It can be photo only i.e allows to capture just photo. Similarly video or can be both. `photo` `video` `both` |
| initialCamera           | string  | Initialize either camera, back or front. `back` `front`                                                                        |
| allowGalleryPicker      | boolean | Allow users to pick media from gallery. Default (true).                                                                        |
| allowCameraRotate       | boolean | Allow users rotate camera i.e back and front. Default (true).                                                                  |
| allowFlashControl       | boolean | Allow users to control flash options. Default (true).                                                                          |
| preview                 | boolean | If set true, users can view captured/selected media.                                                                           |
| maxCount                | number  | It used to control number of media that can be captured/selected                                                               |
| maxCountMessage         | string  | Custom message to show when captured/selected media is greater than maxCount                                                   |
| minCount                | number  | It used to control number of media that can be captured/selected                                                               |
| minCountMessage         | string  | Custom message to show when captured/selected media is greater than minCount                                                   |
| permissionDeniedMessage | string  | Set custom message when access to camera is denied                                                                             |
| nextButtonLabel         | string  | Set custom label on next button.                                                                                               |
| cameraRotateIcon        | widget  | Set custom icon for camera rotate button. [see here](/widget-reference/Icon)                                                   |
| galleryPickerIcon       | widget  | Set custom icon for gallery picker button. [see here](/widget-reference/Icon)                                                  |
| focusIcon               | widget  | Set custom icon for focus node.                                                                                                |
| assistAngle             | object  | Show assist message whenever angle goes below minAngle or above minAngle. [see properties](#values-for-optionsassistangle)     |
| assistSpeed             | object  | Show assist message whenever camera is moving faster than maxSpeed. [see properties](#values-for-optionsassistspeed)           |
| autoCaptureInterval     | integer | If set any number n, on each n interval camera will capture                                                                    |
| captureOverlay          | boolean | If set picture will be cropped according to overlay widget                                                                     |
| faceDetection           | object  | Enable face detection. [see properties](#values-for-optionsfacedetection)                                                      |

##### Values for options.assistAngle

| Property                   | Type   | Description                                   |
| :------------------------- | :----- | :-------------------------------------------- |
| minAngle                   | number | Minimum angle                                 |
| maxAngle                   | number | Maximum Angle                                 |
| maxAngleassistAngleMessage | number | Custom message to show when condition is hit. |

##### Values for options.assistSpeed

| Property           | Type   | Description                                   |
| :----------------- | :----- | :-------------------------------------------- |
| maxSpeed           | number | Maximum speed in km/hr.                       |
| assistSpeedMessage | number | Custom message to show when condition is hit. |

##### Values for options.faceDetection

| Property                  | Type    | Description                                                                                                                                       |
| :------------------------ | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| enabled                   | boolean | Enable face detection.                                                                                                                            |
| message                   | string  | use this pass a message above the camera                                                                                                          |
| messageStyle              | object  | style applied to the message widget                                                                                                               |
| showControls              | boolean | set false to hide all controls                                                                                                                    |
| showCaptureControl        | boolean | set false to hide capture control icon                                                                                                            |
| showFlashControl          | boolean | set false to hide flash control control icon                                                                                                      |
| showCameraLensControl     | boolean | set false to hide camera lens control icon                                                                                                        |
| indicatorShape            | string  | use this to change the shape of the face indicator `circle`, `square`                                                                             |
| autoDisableCaptureControl | boolean | set true to disable capture control widget when no face is detected                                                                               |
| autoCapture               | boolean | set true to capture image on face detected                                                                                                        |
| imageResolution           | string  | use this to set image resolution `low`, `medium`, `high`                                                                                          |
| defaultFlashMode          | string  | use this to set initial flash mode `off`, `auto`, `always`                                                                                        |
| performanceMode           | string  | Use this to set your preferred performance mode. `accurate`, `fast`                                                                               |
| accuracyConfig            | object  | Use this to set accuracy config for face detection. Accuracy config is only supported on web. [see properties](#values-for-optionsaccuracyconfig) |

##### Values for options.accuracyConfig

> [Note]
> Accuracy config is only supported on web.

| Property                   | Type   | Description                                                                  |
| :------------------------- | :----- | :--------------------------------------------------------------------------- |
| detectionThreshold         | number | Minimum confidence score required to consider a face detection valid.        |
| intersectionRatioThreshold | number | Minimum allowed overlap ratio between the detected face and expected region. |
| extraHeightFactor          | number | Additional height factor added to the face bounding box.                     |
| inputSize                  | number | Size of the input image used for face detection.                             |
| landmarkRatio              | number | Minimum acceptable alignment accuracy for facial landmarks.                  |
| frameMargin                | number | Margin ratio to ensure face is not too close to frame edges.                 |
| tiltAngleThreshold         | number | Maximum allowed tilt angle of the detected face (in degrees).                |
| horizontalCenterTolerance  | number | Allowed tolerance for how centered the face must be horizontally.            |
| earThreshold               | number | Minimum Eye Aspect Ratio (EAR) to detect open eyes.                          |
| minFaceWidthRatio          | number | Minimum ratio of face width relative to the frame.                           |
| maxFaceWidthRatio          | number | Maximum ratio of face width relative to the frame.                           |
| qualityPassThreshold       | number | Minimum quality score required for a face to pass detection.                 |
| yawLowerThreshold          | number | Lower bound of acceptable yaw (left-right head rotation) ratio.              |
| yawUpperThreshold          | number | Upper bound of acceptable yaw (left-right head rotation) ratio.              |


**Usage Examples**



```yaml
View:
  header:
    title: "Action: openCamera"
  styles:
    scrollableView: true
  body:
    Column:
      styles: { gap: 16, padding: 24 }
      children:
        - Button:
            label: Open Camera
            onTap:
              openCamera:
                id: cameraId

                options:
                  mode: photo

        - Conditional:
            conditions:
              - if: ${cameraId.files.length > 0}
                Carousel:
                  item-template:
                    data: ${cameraId.files}
                    name: file
                    template:
                      Image:
                        source: ${file.path}
```



`openCamera` also comes with options



```yaml
- Button:
    label: Camera with options
    onTap:
      openCamera:
        id: cameraId1
        options:
          allowGalleryPicker: true
          allowCameraRotate: true
          allowFlashControl: true
          preview: true
          maxCount: 2
          mode: photo

- Conditional:
    conditions:
      - if: ${cameraId1.files.length > 0}
        Carousel:
          item-template:
            data: ${cameraId1.files}
            name: file
            template:
              Image:
                source: ${file.path}
```



`openCamera` also comes with advance options

- assistAngle, show message when phone angle goes below min angle or goes beyond max angle.
- assistSpeed, show message when phone goes beyond max speed.
- minCount/maxCount, type is a number and can also be set to `minCount: ${ensemble.storage.xyz}` to get a dynamic value



```yaml
- Button:
    label: Camera with advance options.
    onTap:
      openCamera:
        options:
          allowGalleryPicker: true
          allowCameraRotate: true
          allowFlashControl: true
          preview: true

          assistAngle:
            minAngle: 80
            maxAngle: 100
            assistAngleMessage: Please try to keep angle approx. 90 degree.

          assistSpeed:
            maxSpeed: 10
            assistSpeedMessage: Please try to speed below 10 km/hr.
```



`openCamera` also comes with custom overlay widget

- captureOverlay, crop image according to overlay widget.
- height/width, required to specify the crop area of widget.



```yaml
- Button:
    label: Camera with overlay widget.
    onTap:
      openCamera:
        options:
          captureOverlay: true
        
        loadingWidget:
          Progress:
            display: circular
            id: loading
            visible: false 
        
        overlayWidget:
          Column:
            styles:
              height: 170
              width: 260
            children:
              - Image:
                  source: https://i.imgur.com/rEYx444.png
```


You can capture and upload to specified API



```yaml
        - Button:
            label: Capture and upload
            onTap:
              openCamera:
                id: captureMedia
                onComplete:
                  uploadFiles:
                    id: uploader
                    files: ${captureMedia.files}
                    uploadApi: fileUploadApi
                    fieldName: files
                    inputs:
                      url: <specify your url>


        - Markdown:
            text: ${uploader.body}

API:
  fileUploadApi:
    inputs:
      - url
    uri: ${url}
    method: POST
```

You can clear previous camera results while recapturing using `cameraId.clear()`

```yaml
- Button:
    label: Clear Previous Result and Capture
    onTap:
      executeCode:
        body: |
          captureLatest.clear()
        onComplete:
          openCamera:
            id: captureLatest
```

Capture image on face detected

```yaml
- Button:
    label: Open Camera
    onTap:
      openCamera:
        id: cameraWithFaceDetection
        options:
          initialCamera: front
          faceDetection:
            enabled: true
            autoCapture: false
            performanceMode: accurate
            accuracyConfig: # accuracyConfig is only supported on web
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
            onComplete:
              showDialog:
                body:
                  Column:
                    children:
                      - TextInput:
                          value: ${cameraWithFaceDetection.files[0]}
                      - Image:
                          source: ${cameraWithFaceDetection.files[0].path}
```


To learn more about openCamera functionalities, test it out here in [Ensemble Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/USuOaOZApSgzE2uVrqlv) app.
