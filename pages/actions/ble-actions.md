### BLE Client

Ensemble bluetooth modules allows you to create BLE client on ensemble platform. 


### SETUP

#### Android
Add permissions for Android (With Fine Location)
```xml
<!-- Tell Google Play Store that your app uses Bluetooth LE
     Set android:required="true" if bluetooth is necessary -->
<uses-feature android:name="android.hardware.bluetooth_le" android:required="false" />

<!-- New Bluetooth permissions in Android 12
https://developer.android.com/about/versions/12/features/bluetooth-permissions -->
<uses-permission android:name="android.permission.BLUETOOTH_SCAN"/>
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

<!-- legacy for Android 11 or lower -->
<uses-permission android:name="android.permission.BLUETOOTH" android:maxSdkVersion="30" />
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" android:maxSdkVersion="30" />

```

When release `project/android/app/proguard-rules.pro` add following:-

> `-keep class com.lib.flutter_blue_plus.* { *; }`


#### IOS

In the `ios/Runner/Info.plist` let’s add:
```plist
    <key>NSBluetoothAlwaysUsageDescription</key>
    <string>This app needs Bluetooth to function</string>
```


### Action References

* Note that the event.data is exactly set of characters that the device is sending. It will be a string. If the device is sending JSON data, that will *not* be automatically converted. You will need to call `JSON.parse(event.data)` to convert it to JSON *

`bluetoothInit` : Turns on the bluetooth (Android only) and Stream of on & off states of the bluetooth.
```yaml
Icon:
    name: bluetooth_fill
    library: remix
    onTap:
    bluetoothInit:
        onDataStream: |
        bluetoothStatus.text = event.data;
```
`bluetoothStartScan` : Starts a scan for Ble devices
```yaml
Button:
    label: Device scan
    onTap:
        bluetoothStartScan:
        onDataStream: |
            ensemble.storage.devices = event.data
```

`bluetoothConnect` : Establishes a connection to the Bluetooth Device and listen to connection stream
```yaml
Button:
    label: Connect
    onTap: 
        bluetoothConnect:
        deviceId: ${device.deviceId}
        timeout: 60
        onConnectionStream: |
            status.text = event.data.status;
        onDataStream: |
            ensemble.storage.services = event.data;
```

`bluetoothDisconnect`: Disconnect connection to Bluetooth Device.
```yaml
Button:
    label: Disconnect
    onTap: 
        bluetoothDisconnect:
        deviceId: ${device.deviceId}
```

`bluetoothSubscribeCharacteristic`: Listen and Retrieves the value of the characteristic.
```yaml
Button:
    label: Subscribe
    onTap:  
        bluetoothSubscribeCharacteristic:
        id: ${characteristic.id}
        onDataStream: |
            data.text = event.data
```
`bluetoothUnsubscribeCharacteristic`: Stop listening to a given characteristics
```yaml
Button:
    label: UnSubscribe
    onTap:  
        bluetoothUnsubscribeCharacteristic:
        id: ${characteristic.id}
```

