# openAppSettings

Applicable on iOS/Android only. Opens the app settings page where the user can manage app permissions and settings. If `target` (optional) is provided and supported on the current running platform, it will open the specific setting page, otherwise the "Settings" screen will be opened.

**Inputs**:

`target (optional)`: the specific setting screen (see below) to open. Defaults to "settings" if not specified.

### Properties

| Target                           | Supported Platforms | Description                                                   |
| -------------------------------- | ------------------- | ------------------------------------------------------------- |
| settings                         | Android, iOS        | Open the main settings page                                   |
| accessibility                    | Android, iOS        | Open the accessibility settings                               |
| bluetooth                        | Android, iOS        | Open the Bluetooth settings                                   |
| date                             | Android, iOS        | Open the date and time settings                               |
| display                          | Android, iOS        | Open the display settings                                     |
| location                         | Android, iOS        | Open the location settings                                    |
| sound                            | Android, iOS        | Open the sound/audio settings                                 |
| wifi                             | Android, iOS        | Open the WiFi settings                                        |
| security                         | Android, iOS        | Open the security settings                                    |
| hotspot                          | Android, iOS        | Open the personal hotspot settings                            |
| appSettings                      | Android, iOS        | Open the app-specific settings                                |
| notification                     | Android, iOS 16+    | Open the notification settings                                |
| apn                              | Android             | Open the APN (Access Point Name) settings                     |
| batteryOptimization              | Android             | Open the Battery Optimization settings                        |
| dataRoaming                      | Android             | Open the Data Roaming settings                                |
| developer                        | Android             | Open the Developer options                                    |
| device                           | Android             | Open the device information settings                          |
| internalStorage                  | Android             | Open the internal storage settings                            |
| lockAndPassword                  | Android             | Open the lock screen and password settings                    |
| nfc                              | Android             | Open the NFC settings                                         |
| memoryCard                       | Android             | Open the memory card settings                                 |
| addAccount                       | Android             | Open the add account screen                                   |
| airplaneMode                     | Android             | Open the airplane mode settings                               |
| applicationDetails               | Android             | Open the application details screen                           |
| applicationNotification          | Android             | Open the application notification settings                    |
| applicationSettings              | Android             | Open the application settings                                 |
| applicationWriteSettings         | Android             | Open the application write settings                           |
| batterySaver                     | Android             | Open the battery saver settings                               |
| captioning                       | Android             | Open the captioning settings                                  |
| cast                             | Android             | Open the cast settings                                        |
| dataUsage                        | Android             | Open the data usage settings                                  |
| appNotificationBubble            | Android             | Open the app notification bubble settings                     |
| appNotification                  | Android             | Open the app notification settings                            |
| search                           | Android             | Open the search settings                                      |
| biometricEnroll                  | Android             | Open the biometric enrollment screen                          |
| hardwareKeyboard                 | Android             | Open the hardware keyboard settings                           |
| home                             | Android             | Open the home screen settings                                 |
| ignoreBackgroundDataRestrictions | Android             | Open the background data restriction settings                 |
| inputMethod                      | Android             | Open the input method settings                                |
| inputMethodSubtype               | Android             | Open the input method subtype settings                        |
| locale                           | Android             | Open the locale settings                                      |
| manageAllApplications            | Android             | Open the manage all applications screen                       |
| manageApplication                | Android             | Open the manage application screen                            |
| manageDefaultApps                | Android             | Open the manage default apps screen                           |
| manageExternalSources            | Android             | Open the manage external sources screen                       |
| manageOverlay                    | Android             | Open the manage overlay settings                              |
| vpn                              | Android             | Open the VPN settings                                         |
| wireless                         | Android             | Open the wireless settings                                    |
| icloud                           | iOS                 | Open the iCloud settings                                      |
| privacy                          | iOS                 | Open the privacy settings                                     |
| cellular                         | iOS                 | Open the cellular settings                                    |
| siri                             | iOS                 | Open the Siri settings                                        |
| photos                           | iOS                 | Open the photos and camera settings                           |
| keyboard                         | iOS                 | Open the keyboard settings                                    |
| general                          | iOS                 | Open the general settings                                     |
| about                            | iOS                 | Open the about device screen                                  |
| accountSettings                  | iOS                 | Open the account settings                                     |
| autoLock                         | iOS                 | Open the auto-lock settings                                   |
| battery                          | iOS                 | Open the battery settings                                     |
| dictionary                       | iOS                 | Open the dictionary settings                                  |
| facetime                         | iOS                 | Open the FaceTime settings                                    |
| healthKit                        | iOS                 | Open the HealthKit settings                                   |
| music                            | iOS                 | Open the music settings                                       |
| keyboards                        | iOS                 | Open the keyboards settings (for managing multiple keyboards) |
| languageAndRegion                | iOS                 | Open the language and region settings                         |
| phone                            | iOS                 | Open the phone settings                                       |
| profilesAndDeviceManagement      | iOS                 | Open the profiles and device management screen                |
| softwareUpdate                   | iOS                 | Open the software update screen                               |
| storageAndBackup                 | iOS                 | Open the storage and backup settings                          |
| wallpapers                       | iOS                 | Open the wallpapers settings                                  |
| subscriptions                    | iOS 15+             | Open the subscription settings                                |
