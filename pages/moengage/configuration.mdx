import { Callout } from 'nextra/components'

# MoEngage Integration

MoEngage is a powerful customer engagement platform that enables real-time, personalized messaging across multiple channels. Ensemble provides native integration with MoEngage offering:
- Push Notifications (iOS & Android)
- In-App Messaging
- Event Tracking & Analytics
- User Attribute Management


## MoEngage Dashboard Setup

The following setup on MoEngage Dashboard is required regardless of whether you're enabling MoEngage through Ensemble Studio or local development. This establishes the core configuration needed for MoEngage integration.

1. Get MoEngage Workspace ID:
     - Navigate to MoEngage Dashboard → Settings → General Settings → Basic Details
     - Copy your Workspace ID from the displayed information

2. Configure Firebase for Android Push:
     - Follow the complete [FCM Authentication Guide](https://developers.moengage.com/hc/en-us/articles/16909296490644-FCM-Authentication)
     - This guide walks you through:
       a. Creating a Firebase project
       b. Generating FCM Server Key
       c. Adding the key to MoEngage Dashboard
       d. Enabling necessary FCM APIs

3. Configure APNS for iOS Push (Choose one):
     - Option 1: [APNS Authentication Key](https://developers.moengage.com/hc/en-us/articles/8484447635348-APNS-Authentication-Key) (Recommended)
     - Option 2: [APNS Certificate](https://developers.moengage.com/hc/en-us/articles/4403944011028-APNS-Certificate-PEM-file)

4. Create Platform Apps:
     - Create corresponding apps in Firebase Console for Android/iOS
     - Ensure the application ID matches your Ensemble app configuration
     - Download required configuration files:
       - Android: google-services.json
       - iOS: GoogleService-Info.plist
       - Web: Firebase configuration object

## Enable MoEngage in Ensemble Studio

If you're using Ensemble Studio for building your application, follow these steps to enable MoEngage. No additional local configuration will be required.

1. Navigate to Build & Deploy → Build Settings
2. Enable MoEngage toggle in the Modules section
3. Enter Configuration Details:
     - MoEngage Workspace ID obtained from dashboard
     - Add Firebase Web Configuration
4. Upload Platform Configuration Files:
     - Upload google-services.json for Android
     - Upload GoogleService-Info.plist for iOS
5. Click Update to save your configuration


## Handling Notifications

Ensemble provides multiple ways to handle MoEngage notifications to suit your use cases:

1. **Notification Handler**: Define a notification handler in JavaScript to be executed on every notification received. You can run logic then return a payload to navigate to a screen.

2. **Default Behavior**: If notification handler is not specified, the app will simply open up (if not in foreground).

### Creating a Script and Handler Function

1. Navigate to or create a script in the Scripts section, for example Common.js.

2. Create a handler function that will be called when notifications are received:

```javascript
function handle_notification(notification) {
   // Your notification handling logic here
}
```

The notification parameter will contain:

#### For Push Notifications:
```javascript
{
  "payload": {...}, // Original push payload data received from MoEngage
  "clickedAction": Map<String, dynamic>, // Button action details if clicked
  "platform": "android/ios",
  'notificationType': 'push',
  "isDefaultAction": true/false, // For Android only
}
```

For complete push notification payload details, see [Push Callback Payload Documentation](https://developers.moengage.com/hc/en-us/articles/11652033989396-Push-Callback#h_01H1RX45YD2A06V7SM4TYZWF3V)

#### For In-App Messages:
```javascript
{
  "campaignId": "campaign_id",
  "campaignName": "campaign_name", 
  "platform": "android/ios",
  'notificationType': 'inApp',
  "data": {
    "navigationType": "deeplink/screen", // present only if action is `NavigationAction`
    "navigationUrl": "url", // present only if action is `NavigationAction`
    "keyValuePairs": {} // Custom data
  }
}
```

For complete in-app message payload structure, see [In-App Callback Payload Documentation](https://developers.moengage.com/hc/en-us/articles/4404365619092-InApp-NATIV#h_01H96BKP4MZAJTSRZ58FM3Z3XZ)

Inside your handler function, you can:
- Write custom routing logic
- Access ensemble.storage
- Return a navigation payload

Example handler:
```javascript
function handle_notification(notification) {
    console.log("Received notification:", notification);
    
    // Assuming the screen name is in the data section
    var payload = {
        "name": notification['data']['screen'],
        // You can also pass inputs that will be accessible on the destination screen using `notificationPayload.*`
    };
    
    return payload;
}
```

If you don't want to navigate, simply don't return anything.

### Setting up the Handler

1. Go to Settings -> Environment Variables
2. Add new variable: `ensemble_notification_handler` 
3. Set value to `scriptName.handlerName` (e.g. `Common.handle_notification`)

Once configured, your handler function will be called for all received notifications.

<Callout emoji="💡">
  MoEngage integration in Ensemble enables comprehensive user engagement tracking and campaign management capabilities. You can track custom analytics events, manage user profiles with rich attributes, control push notifications and in-app messages, and configure SDK behavior. All these operations are available through the [`logEvent` action](actions/log_events.md) which provides detailed documentation of supported operations and their implementations.
</Callout>


## Enable MoEngage in Local Project

If you're developing locally without using Ensemble Studio build system, follow these configuration steps. You can skip the Ensemble Studio setup section above.

#### Ensemble Files (Required)

**1.** Update `ensemble_modules.dart`
Import required modules and initialize Firebase and MoEngage. Add this at the start of file:
```dart
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:ensemble_moengage/moengage.dart';
import 'package:firebase_core/firebase_core.dart';
```
Replace default Firebase initialization with platform-specific options

```dart
// Initialize Firebase with platform-specific options
FirebaseOptions? androidPayload = const FirebaseOptions(
  apiKey: "YOUR_ANDROID_API_KEY",
  appId: "YOUR_ANDROID_APP_ID",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID", 
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_STORAGE_BUCKET"
);

// Add similar configurations for iOS and Web platforms
FirebaseOptions? iosPayload = ...
FirebaseOptions? webPayload = ...

FirebaseOptions? selectedPayload;
if (Platform.isAndroid) {
  selectedPayload = androidPayload;
} else if (Platform.isIOS) {
  selectedPayload = iosPayload;
}
if (kIsWeb) {
  selectedPayload = webPayload;
}

await Firebase.initializeApp(options: selectedPayload);
```
Initialize MoEngage with your workspace ID and logging preferences by replace this `GetIt.I.registerSingleton<MoEngageModule>(MoEngageImpl());` with below code:
```dart
// Register MoEngage
GetIt.I.registerSingleton<MoEngageModule>(
  MoEngageImpl(
    workspaceId: 'YOUR_WORKSPACE_ID', // dont forget to replace workspace id.
    enableLogs: true
  )
);
```

**2.** Update `ensemble.properties`:
```yaml
moengageAppId=YOUR_WORKSPACE_ID
```
#### Android Configuration
**1.** Add MoEngage and Firebase dependencies in `android/app/build.gradle` and also Configure Google Services plugin:
```gradle
dependencies {
    // MoEngage Core dependencies
    implementation("androidx.core:core:1.6.0")
    implementation("com.moengage:moe-android-sdk:12.8.01")
    implementation("com.google.firebase:firebase-messaging:23.4.1")
    implementation("androidx.lifecycle:lifecycle-process:2.7.0")
    implementation("androidx.appcompat:appcompat:1.3.1")
    implementation("com.github.bumptech.glide:glide:4.9.0")
}

apply plugin: 'com.google.gms.google-services'
```

**2.** Update `AndroidManifest.xml` to add required permissions, MoEngage services and set up deep linking configurations, also change application level `android:name`:
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!-- Required Permissions -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>

    <application
        android:name=".MyApplication">
        
        <activity>
            <!-- Add MoEngage Deep Linking -->
            <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data
                    android:host="your.domain.com"
                    android:scheme="moengage" />
            </intent-filter>
        </activity>

        <!-- MoEngage Push Service -->
        <service
            android:name="com.moengage.firebase.MoEFireBaseMessagingService"
            android:exported="false">
            <intent-filter>
                <action android:name="com.google.firebase.MESSAGING_EVENT" />
            </intent-filter>
        </service>

        <!-- Push Tracker Activity -->
        <activity
            android:name="com.moengage.pushbase.activities.PushTracker"
            android:launchMode="singleInstance"
            tools:replace="android:launchMode" />
    </application>
</manifest>
```

**3.** Create `CustomPushListener.kt` to handle push notification interactions:
```kotlin
package your.package.name

import android.app.Activity
import android.os.Bundle
import com.moengage.core.internal.logger.Logger
import com.moengage.core.model.AccountMeta
import com.moengage.plugin.base.push.PluginPushCallback

class CustomPushListener(accountMeta: AccountMeta) : PluginPushCallback(accountMeta) {
    private val tag = "CustomPushListener"

    override fun onNotificationClick(activity: Activity, payload: Bundle): Boolean {
        Logger.print { "$tag onNotificationClick() : " }
        return super.onNotificationClick(activity, payload)
    }
}
```

**4.** Create `MyApplication.kt`:
```kotlin
package your.package.name

import com.moengage.core.DataCenter
import com.moengage.core.MoEngage
import com.moengage.core.config.FcmConfig
import com.moengage.core.config.NotificationConfig
import com.moengage.flutter.MoEInitializer
import android.app.Application

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
    
        val moEngage = MoEngage.Builder(this, BuildConfig.MOENGAGE_WORKSPACE_ID, DataCenter.DATA_CENTER_1)
            .configureFcm(FcmConfig(true))
            .configureNotificationMetaData(
                NotificationConfig(
                    R.drawable.icon,
                    R.drawable.launcher,
                    notificationColor = -1,
                    isMultipleNotificationInDrawerEnabled = false,
                    isBuildingBackStackEnabled = true,
                    isLargeIconDisplayEnabled = true
                )
            )

        MoEInitializer.initialiseDefaultInstance(this, moEngage)
    }
}
```

**5.** Update `MainActivity.kt`:
```kotlin
package your.package.name

import android.content.Intent
import android.content.res.Configuration
import android.os.Bundle
import com.moengage.flutter.MoEFlutterHelper
import io.flutter.embedding.android.FlutterActivity

class MainActivity : FlutterActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        processIntent(intent)
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        MoEFlutterHelper.getInstance().onConfigurationChanged()
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        processIntent(intent)
    }

    private fun processIntent(intent: Intent?) {
        if (intent == null) return
    }
}
```

**6.** Add Platform Configuration Files:
   - Place `google-services.json` in `android/app/`
   - Add to `android/build.gradle`:
```gradle
buildscript {
    dependencies {
        classpath 'com.google.gms:google-services:4.3.15'
    }
}
```

#### iOS Configuration
Te be added.


