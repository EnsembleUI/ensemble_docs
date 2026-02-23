## authenticateByBiometric

It helps to authenticate user based on biometrics such as face and fingerprint based on sensor available on user's device. 


> [Note]  
> It only works in native devices which has biometric sensors.


### Native Configuration

#### iOS Configuration 

The action works with both Touch ID and Face ID. However, to use the latter, you need to add following in `info.plist`

```plist
<key>NSFaceIDUsageDescription</key>
<string>Why is my app authenticating using face id?</string>
```

#### Android Configuration

Update your `MainActivity.java`:

```java
import io.flutter.embedding.android.FlutterFragmentActivity;

public class MainActivity extends FlutterFragmentActivity {
}
```

or `MainActivity.kt`:

```kt
import io.flutter.embedding.android.FlutterFragmentActivity

class MainActivity: FlutterFragmentActivity() {
}
```

Permissions

In your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.USE_BIOMETRIC"/>
```

### Sample EDL

```yaml
Button:
  label: Biometric Auth
  onTap:
    authenticateByBiometric:
      label: Authenticate to see your balance

      # if device has pin configurated but not biometric sensor be it face or finger, setting allowConfiguration to true will popup user to first configure the settings.
      allowConfiguration: true
      onAuthenticated: |
        //@code
        ensemble.debug('Successfully authenticated');

      onAuthenticationFailed: |
        //@code
        ensemble.debug('Failed to authenticate');

      onSensorNotConfigured: |
        //@code
        ensemble.debug('sensor is not configured');

      onSensorNotAvailable: |
        //@code
        ensemble.debug('sensor not available');

      onError: |
        //@code
        ensemble.debug('on unknown error');

```

