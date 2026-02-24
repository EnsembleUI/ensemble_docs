# Screen Lifecycle
An Ensemble app consists of a series of screens, each with its own lifecycle that defines how it renders, pauses, resumes, and disposes of resources. You can provide actions to be triggered at each of these lifecycle stages.

### onLoad
This stage is triggered when the screen is first loaded and the body widget has been rendered. At this point, you will have access to all widget IDs (if specified). This is an ideal place to initialize your screen's states and invoke APIs.

### onPause
This stage is triggered when the screen is no longer active. This could be due to the user navigating to another screen or, in native applications, the app moving to the background. In the latter case, the OS may terminate the app if the Action takes too long to process or uses excessive resources, so it is recommended to execute actions that will complete promptly.

`onPause` includes the following payload (accessible via `event.data.*`):
| Property     | Type    | Description                                                                                                                                                                                              |
| :----------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isAppPause | boolean  | This will be true if the app (Native only) is causing onPause to be called because it is going to the background (or the user is switching to another App). Use this to differentiate from the user navigating to another screen. |


### onResume
This stage is triggered when the screen becomes active again after having previously been inactive. This could be due to the user navigating back to the screen or the app (native only) coming to the foreground.

Note that this will not be triggered if you navigate to another instance of the same screen. In other words, only navigating back (or switching screens using the bottom navigation bar) will trigger this.

`onResume` has the following payload (accessible via `event.data.*`):
| Property     | Type    | Description                                                                                                                                                                                              |
| :----------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| inactiveDuration | number (ms) | Specifying how long the screen has been in inactive state (in milliseconds). This is useful for tracking how long the screen has been inactive and re-fetching the data. Note that we may not always able to determine this, so it may be null. |
| isAppResume | boolean  | This will be true if the app is causing onResume to be called because it is going to the foreground (the user is opening your app). Use this to differentiate with the user navigating back to your screen. |

