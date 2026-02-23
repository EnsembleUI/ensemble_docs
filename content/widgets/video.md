# Video widget

The Video Widget enables seamless integration of video content within your application, providing an immersive and engaging multimedia experience for users.

> To get hands-on experience with `Video` widget, see live example in [Ensemble Studio](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/fce92bbb-af8e-403d-bf2d-c10926cc89a0)

## Properties

| Property | Type   | Description                      |
| :------- | :----- | :------------------------------- |
| source   | string | The URL source to the media file |
| showControls   | boolean | Offers options to show/hide video controls. (default true) |
| loadingWidget   | Widget | The widget to show when video is loading. |
| repeat   | boolean | Video will kept replaying in loop. |
| autoplay   | boolean | Automatically start the video when player is loaded. (default False) |
| playbackRate   | number | For changing the speed at which the video is displayed |
| volume   | number | Changes the volume. (max = 100, min = 0) |
| onChange   | Action | Action to execute when the video has changed |
| onStart   | Action | Call Ensemble's built-in functions or execute code when video is about to start |
| onEnd   | Action | Call Ensemble's built-in functions or execute code when video is about to end |

## Code Example
```
Video:
  source: https://flutter.github.io/assets-for-api-docs/assets/videos/bee.mp4
  repeat: true
  autoplay: true
  showControls: false
  loadingWidget: 
    Progress:
      display: circular
```
