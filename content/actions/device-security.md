# Device Security

The `deviceSecurity` action checks if the device is rooted, debugged, or running on an emulator. It executes corresponding actions based on the results of these checks, enhancing security awareness and control within your application

## Properties

| Property  | Type   | Description                                                                      |
| :-------- | :----- | :------------------------------------------------------------------------------- |
| onSuccess | action | Action to be executed on successful security check with data on device status    |
| onError   | action | Action to be executed on error during the security check                         |

### Event Data

When the `onSuccess` action is executed, the following data is available under `event.data`:

- **debugged**: Indicates if the device is in debug mode.
- **rooted**: Indicates if the device is rooted.
- **emulator**: Indicates if the device is an emulator.

When the `onError` action is executed, the following data is available under `event.error`:

- **error**: Error message describing the issue.

**Example**

```yaml
View:
  header:
    titleText: "Device Security Example"

  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
        - Button:
            label: Check Device Security
            onTap:
              deviceSecurity:
                onSuccess:
                  executeConditionalAction:
                    conditions:
                      - if: ${event.data.debugged}
                        action:
                          showDialog:
                            body:
                              Text:
                                text: "The device is in debug mode."
                      - elseif: ${event.data.rooted}
                        action:
                          showDialog:
                            body:
                              Text:
                                text: "The device is rooted."
                      - elseif: ${event.data.emulator}
                        action:
                          showDialog:
                            body:
                              Text:
                                text: "The device is an emulator."
                      - else:
                        action:
                          showDialog:
                            body:
                              Text:
                                text: "The device is secure."
                onError:
                  showDialog:
                    body:
                      Text:
                        text: ${event.error}
```

**Kitchen Sink**

You can find a complete example of using the deviceSecurity action in the [Ensemble Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/RLWeYjfVwopcTqhWo6mX). This example demonstrates how to integrate the action within a screen, handle the success and error cases, and display relevant information to the user based on the device's security status.

### Platform Based Configurations

- **Android**: No additional configurations are required.
- **iOS**: Add following lines to the `Info.plist` file in /ios/Runner/ folder:

```xml
<key>LSApplicationQueriesSchemes</key>
    <array>
        <string>undecimus</string>
        <string>sileo</string>
        <string>zbra</string>
        <string>filza</string>
        <string>activator</string>
    </array>
```

---
**NOTE**

This action only works for native applications (Android and iOS), on web it will always return false.

---
