# openAppSettings
Applicable on iOS/Android only. Opens the app settings page where the user can manage app permissions and settings. If `target` (optional) is provided and supported on the current running platform, it will open the specific setting page, otherwise the "Settings" screen will be opened.

**Inputs**:

`target (optional)`: the specific setting screen (see below) to open.

### Properties
| Target | Supported Platforms | Description |
| ------ | ------------------- | ----------- |
| accessibility       | Android                 | Open the accessibility settings |
| alarm               | Android                 | Open the alarm settings |
| apn                 | Android                 | Open the APN settings |
| appLocale           | Android 13+             | Open the app language settings. This setting is only available on Android 13+ |
| batteryOptimization | Android                 | Open the Battery Optimization settings |
| bluetooth           | Android                 | Open the Bluetooth settings |
| dataRoaming         | Android                 | Open the Data Roaming settings |
| date                | Android                 | Open the date settings |
| developer           | Android                 | Open the Developer settings |
| device              | Android                 | Open the device settings |
| display             | Android                 | Open the display settings |
| hotspot             | Android                 | Open the Hotspot settings |
| internalStorage     | Android                 | Open the internal storage settings |
| location            | Android                 | Open the location settings |
| lockAndPassword     | Android                 | Open the Lock And Password settings |
| nfc                 | Android                 | Open the NFC settings |
| notification        | Android, iOS 16+        | Open the notification settings |
| security            | Android                 | Open the security settings |
| settings            | Android, iOS            | Open the app settings |
| sound               | Android                 | Open the audio settings |
| subscriptions       | iOS 15+                 | Open the subscription settings |
| vpn                 | Android                 | Open the VPN settings |
| wifi                | Android                 | Open the wifi settings |
| wireless            | Android                 | Open the wireless settings |