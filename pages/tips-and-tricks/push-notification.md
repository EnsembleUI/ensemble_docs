# Push Notification

## Setup
This guide will walk you through setting up iOS/Android push notifications for your Ensemble app. Before you begin, ensure your bundle ID is correct. Also ensure the `appId` under `ensemble.properties` has the same bundle ID.

#### iOS Setup
An Apple developer account is required to setup push notification and deploy the app. Each account requires a single APNs certificate for push notifications that work across all your Apps. If you don't already have one, go to https://developer.apple.com/account/resources/authkeys/list.
- Create a new Key and select "Apple Push Notification service (APNs)".
- Download the key and save it in a secure location (you can only download it once). You will need this key to upload to Firebase.

#### Setup Firebase
- Create a new Firebase project if not already created. Go to Project Settings.
  - Under "General" tab, add an iOS or Android app, then download the `GoogleService-Info.plist` or `google-services.json` respectively.
  - Under "Cloud Messaging" tab and inside "Apple app configuration", upload the APNs Authentication Key you created / downloaded earlier in your Apple developer account.
    - Use the Key ID under the APNs key you created earlier.
    - Use the Team ID from your Apple Developer account.

### Setup Ensemble
- Open `/starter/lib/generated/ensemble_modules.dart` with an Editor and change `useNotifications` to true.
- open Xcode under `/starter/ios`.
  - Under Signing & Capabilities, click on `+ Capability` button.
  - Add `Push Notifications`.
  - Add `Background Modes` and check `Remote notifications`, `Background fetch` and `Background processing`.
    - drop "GoogleService-Info.plist" in ios/Runner
- Drop the `google-services.json` in `android/app` folder.

### Testing notifications
- Firebase requires a device token to send notification to. For testing purpose you can retrieve the device token by using the following app definition. Upon running this screen, it will ask the user to authorize Notifications. Once authorized, the device token will be displayed.
```yaml
View:
    onLoad:
      requestNotificationAccess:
        onAuthorized: |-
          status.value = event.data.deviceToken;
        
        # if denied, you may want to take the user to another screen, 
        # explaining why notifications are needed with an option to
        # take the user to Settings' Notification page.
        onDenied:
          navigateScreen:
            name: Enable Notifications

    # Optional - set the header for the screen
    header:
      title: What's my device token

    # Specify the body of the screen
    body:
      Column:
        styles:
          padding: 24
          gap: 8
        children:
          - TextInput:
              id: status
```
- To send a test notification from Firebase, Go to "Messaging" and create your first campaign.
  - Select `Firebase Notification messages`.
  - Enter a notification text and click "Send test message".
  - Enter the device token above and click "Test".
  - You should be receiving a push notification

### Update when token changes
- Firebase can occasionally assign a new device token. When that happens, Ensemble automatically save a copy of the latest token, accessible via `ensemble.device.deviceToken`.

- To update your server with the latest token, you can usually add the logic inside your home screen (where the user has been authenticated). Below is a example:
```yaml
## Home screen:
View:
  onLoad:
    invokeAPI:
      name: updateDeviceToken
    
API:
  updateDeviceToken:
    url: <my server>
    headers:
      Authorization: Bearer <my_bearer_token>
    body:
      newToken: ${ensemble.device.deviceToken}
    

```

## Handling Notifications
Ensemble provides multiple ways to handle notifications to suit your use cases.
1. **[Notification Handler](#creating-a-script-and-handler-function)**: Define a notification handler (see below) in JavaScript to be executed on every notification received. You can run logic then return a payload to navigate to a screen.
2. **[Navigating to a Screen](#navigating-to-a-screen)**: If a handler is not specified but you want to navigate to a screen upon the user tapping on the notification, simply provide either the screenId or screenName in the notification payload.
3. If neither of the above is specified, the app will simply open up the app (if it is currently not on the foreground).

#### Creating a Script and Handler Function
Navigate to or create a script in the Scripts section. For example, you might have a script called Common.
In the script, create a function that will be called whenever a notification is received. For example:
```js
function handle_notification(notification) {
    // Your notification handling logic here
}
```
The notification parameter contains the message data in JSON format.

Inside this function, you can:

- Write your routing logic
- Access ensemble.storage
- Perform one action: navigation
To navigate, simply return the payload of a navigationScreen action. The framework will handle the navigation.

Example:

```js
function handle_notification(notification) {
    console.log(notification);
    
    // Assuming the screen name is in the FCM data section
    var payload = {
        "name": notification['data']['screen'],
        // You can also pass inputs that will be accessible on the destination screen
    };
    
    return payload;
}
```
If you don't want to navigate, simply don't return anything.

Marking the Function as a Notification Handler
To designate your function as the notification handler:

- Go to `Settings` -> `Environment Variables`
- Add a new variable called `ensemble_notification_handler`
- Set its value to `scriptName.handlerName`
For our example, it would be `Common.handle_notification`.

Once set, `Common.handle_notification` will be called every time a notification is received.

#### Navigating to a Screen
Instead of creating a handler function in Javascript, you can specify the screenId or screenName in the notification payload. This will navigate to the specified screen when the user taps on the notification.

Here is an example notification payload sent from the server. Note the screenId / screenName (you should specify one or the other, but not both) in the data section.
```yaml
{
  "token": "<your device token>",
  "notification": {
    "title": "Hi from Ensemble",
    "body": "Hello this is a sample notification"
  },
  "apns": {
    "payload": {
      "aps": {
        # update the badge count on iOS
        "badge": 5  
      }
    }
  },
  # custom data sent to Ensemble
  "data": {
    "screenId": "<ensemble_screen_id>",
    "screenName": "<ensemble_screen_name>",
    "hello": "world"
  }
}
```

Upon receiving this notification, Ensemble will navigate to the screen specified, and pass along the notification title/body, along with the data payload to the screen. You can access this data in the screen using `notificationPayload.*`. Here is an example of the screen the notification will redirect to:
```yaml
View:
  body:
    Text:
      text: |-
        Notification redirected me here:
        Notification title: ${notificationPayload.title}
        Notification body: ${notificationPayload.body}
        Notification payload: ${notificationPayload.data.hello}
```