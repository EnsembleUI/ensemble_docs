## getNetworkInfo

**Works on native iOS and Android apps only. In the browser, `onError` (if specified) will be called with error `Network info is not supported on the web`.**

Action to retrieve the following network information -

- wifiName
- wifiBSSID
- wifiIPv4
- wifiIPv6
- wifiGatewayIP
- wifiBroadcast
- wifiSubmask

If successful, the network information will be available as event.data.networkInfo object with the property names as shows above, for example event.data.networkInfo.wifiName.

In case of error, the error message will be available as event.error.

For all other cases, check the event.data.status property for details

## Properties for getNetworkInfo

| Property   | Type | Description |
| :-------   | :--- | :---------- |
| onSuccess  | action  | (Required) call an Action when the network info has been retrieved successfully. Network info will be available under event.data.networkInfo object with properties wifiName, wifiBSSID, wifiIPv4, wifiIPv6, wifiGatewayIP, wifiBroadcast, wifiSubmask |
| onError | action  | (Optional) call an Action when unable to retrieve networkInfo. This could be because the location or wifiinfo is not enabled in the app or the module has not been included. Error is available as `event.error` property |
| onDenied | action | (Optional) call an Action when the user has denied access to the location. Location access is required to get the wifi data. The status could either be `denied` or `deniedForever`. `deniedForver` means that the user has denied the location access and has selected the option to never ask again. |
| onLocationDisabled | action | (Optional) call an Action when the location is disabled. This could be because the location is disabled in the device settings. |

## How to enable the `getNetworkInfo` action for your app

**When using the build system in the [Ensemble Studio](https://studio.ensembleui.com) the following configurations are automatically added for you and your app is automatically built and made available on the appstore and google play for you to then test or submit for approval.**

1. First enable the `ensemble_network_info` module as follows -
- open starter/pubspec.yaml and search for `Uncomment to enable NetworkInfo` and uncomment the `ensemble_network_info` module reference -
```yaml
  ensemble_network_info:
   git:
     url: https://github.com/EnsembleUI/ensemble.git
     ref: main
     path: modules/ensemble_network_info
```
Run `pub get` to get the latest

- open `starter/lib/generated/ensemble_modules.dart` and ...
. uncomment import 'package:ensemble_network_info/network_info.dart';
. set `useNetworkInfo = true;`
. uncomment `GetIt.I.registerSingleton<NetworkInfoManager>(NetworkInfoImpl());`  

2. Configure permissions for iOS and/or Android as follows

### Browser
Note that `getNetworkInfo` action is available only on iOS and Android. On the web, `onError` (if specified) will be called with error `Network info is not supported on the web`. 

### iOS
**Location**
Location and `Precise Location` is required to get the `wifiName` and `wifiBSSID`. Other properties can be retrieved without location permission. When location is not enabled. `wifiName` and `wifiBSSID` will return null. 

Open the `starter/ios/Runner` directory. There you will find the following two files that we need to modify - `info.plist` and `Runner.entitlements`

`info.plist`: add the following.

Add either `NSLocationWhenInUseUsageDescription` or  `NSLocationAlwaysUsageDescription` depending on what your apps needs. 
Make sure to adjust the message to meet your requirements. `PreciseLocation` is a must to get the wifiName and wifiBSSID.

```xml
	<key>NSLocationWhenInUseUsageDescription</key>
	<string>We need your location to provide better services.</string>
	<key>NSLocationAlwaysUsageDescription</key>
	<string>We need your location to provide continuous tracking even when the app is in the background.</string>
	<key>NSLocationUsageDescription</key>
	<string>using location</string>
	<key>NSLocationTemporaryUsageDescriptionDictionary</key>
	<dict>
		<key>PreciseLocation</key>
		<string>We need your precise location to provide location-based services and ensure accurate tracking.</string>
	</dict>
```

`Runner.entitlements`: add the following

```xml
	<key>com.apple.security.personal-information.location</key>
	<true/>
	<key>com.apple.developer.networking.wifi-info</key>
	<true/>
```
You can do the above changes by using the XCode graphical interface as well. Make sure to do a clean build after making the above changes. 

### Android
Android just needs the `Fine Location` permission as follows. 

Under `starter/android/app/src/main`

`AndroidManifest.xml` 

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

## Example

```yaml
View:
  styles:
    useSafeArea: true
    scrollableView: true

  # Optional - set the header for the screen
  header:
    titleText: Home

  # Specify the body of the screen
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
        - TextInput:
            id: wifiName
            label: wifiName
        - TextInput:
            id: wifiBSSID
            label: wifiBSSID
        - TextInput:
            id: wifiIPv4
            label: wifiIPv4
        - TextInput:
            id: wifiIPv6
            label: wifiIPv6
        - TextInput:
            id: wifiGatewayIP
            label: wifiGatewayIP
        - TextInput:
            id: wifiBroadcast
            label: wifiBroadcast 
        - TextInput:
            id: wifiSubmask
            label: wifiSubmask                                    
        - TextInput:
            id: status
            label: status
            multiline: true
            maxLines: 10
            minLines: 4
        - Button:
            label: get wifi info
            onTap:
              getNetworkInfo:
                onSuccess:
                  executeCode:
                    body: |
                      status.value = event.data.status;
                      wifiName.value = event.data.networkInfo.wifiName;
                      wifiBSSID.value = event.data.networkInfo.wifiBSSID;
                      wifiIPv4.value = event.data.networkInfo.wifiIPv4;
                      wifiIPv6.value = event.data.networkInfo.wifiIPv6;
                      wifiGatewayIP.value = event.data.networkInfo.wifiGatewayIP;
                      wifiBroadcast.value = event.data.networkInfo.wifiBroadcast;
                      wifiSubmask.value = event.data.networkInfo.wifiSubmask;
                onError:
                  executeCode:
                    body: |
                      status.value = event.error;
```
