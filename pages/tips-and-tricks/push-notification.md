# Push Notification

So, you have built the app with ensemble but now you would like to increase the engagement and decided to implement push notification. 

At ensemble we are currently supporting push notification with firebase. Here are the following steps need to be taken to enable push notification.

- Initialize Notification manager
- IOS setup, (Android doesn't require any setup).

## Setup Notification manager

In `main.dart` inside `main()` initialize notification manager with your firebase payload and `backgroundNotificationHandler`.
- The firebase payload data can be found in Project Settings > Your apps.
- `backgroundNotificationHandler`'s purpose is to allow you write any business logic. Here in example we are updating the app icon badge but it can be set to any business logic.

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await NotificationManager().init(
      FirebasePayload(
        apiKey: '<your-api-key>',
        projectId: '<your-project-id>',
        messagingSenderId: '<your-messaging-sender-id>',
        appId: '<your-app-id>',
      ),
      backgroundNotificationHandler:_backgroundNotificationHandler,
);

@pragma('vm:entry-point')
Future<void> _backgroundNotificationHandler(RemoteMessage message) async {
  try {
    //  business logic
    await StorageManager().init();
    int badgeCount =
        Utils.getInt(await StorageManager().read('badgeCount'), fallback: 0);
    int count = badgeCount + 1;
    await StorageManager().write('badgeCount', count);
    if (await FlutterAppBadger.isAppBadgeSupported()) {
      return FlutterAppBadger.updateBadgeCount(count);
    }

  } catch (error) {
    debugPrint("Error running background handler ${error.toString()}");
  }
}

```

## IOS setup

####  Add push notification capability in xcode

#### Create an APNs key 
Here is the link to apple developer website to create APNs key and download it.[Apple developer key link](https://developer.apple.com/account/resources/authkeys/list)
![Developer portal key](/images/tips-and-tricks/assets/developer-apple-keys.png)

#### Upload APNs key to Firebase 

Now upload the APNs key to firebase console. 
So, under the firebase project settings > Cloud Messaging > Apple app configuration. You can upload the APNs key that we downloaded from the previous step.


---
That's all now you can go to your firebase messaging module and send a push notification and it will work for both the platform android and IOS. 


### Handling Notifications in JavaScript
Ensemble provides a way to centralize notification logic in a single JavaScript function. This function is called every time a notification is received.

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

