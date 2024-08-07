# Device

Ensemble provides convenient access to device information and capabilities. This includes device information, such as the device model, operating system, and screen size.

Access these properties/methods with prefix `ensemble.device.*`.

## Media Query
Ensemble uses logical pixels which are based on the device's screen density. This allows for a consistent user interface across different devices.

Below are some media query properties that can be used to create responsive designs for mobile and web apps.

#### width
Returns the width of the device's screen in logical pixels.

#### height
Returns the height of the device's screen in logical pixels.

#### safeAreaTop
Returns the height of the screen's safe area at the top (e.g. iPhone's notch) in logical pixels. This value will be 0 if it is not applicable. You can use this to avoid placing important UI elements in this safe area.

#### safeAreaBottom
Returns the height of the screen's safe area at the bottom (e.g. iPhone's home swiper) in logical pixels. This value will be 0 if it is not applicable.


## Platform
Ensemble comes with convenient utilities/getters to help with platform-specific logic.

#### platform
Returns the platform name the app is running on. Possible values are `ios`, `android`, `web`, `macos`, `windows`, and `other`.

#### isIOS()
Returns `true` if the app is running on an iOS device, otherwise `false`.

#### isAndroid()
Returns `true` if the app is running on an Android device, otherwise `false`.

#### isWeb()
Returns `true` if the app is running on a web browser, otherwise `false`.

#### isMacOS()
Returns `true` if the app is running on a macOS device, otherwise `false`.

#### isWindows()
Returns `true` if the app is running on a Windows device, otherwise `false`.


## Browser Info (web)
Applicable on Web platform only, the following keys can be used to get browser information.
#### browserInfo.browserName
Returns the name of the browser.

#### browserInfo.appCodeName
Returns the app code name of the browser.

#### browserInfo.appName
Returns the name of the application (browser).

#### browserInfo.appVersion
Returns the version information of the browser.

#### browserInfo.deviceMemory
Returns the amount of device memory in gigabytes.

#### browserInfo.language
Returns the preferred language of the user.

#### browserInfo.languages
Returns the languages known to the user, as an array.

#### browserInfo.platform
Returns the platform on which the browser is running.

#### browserInfo.product
Returns the product name of the browser.

#### browserInfo.productSub
Returns the product sub-version number.

#### browserInfo.userAgent
Returns the user agent string of the browser.

#### browserInfo.vendor
Returns the vendor name of the browser.

#### browserInfo.vendorSub
Returns the vendor sub-version number.

#### browserInfo.hardwareConcurrency
Returns the number of logical processors available to run threads.

#### browserInfo.maxTouchPoints
Returns the maximum number of simultaneous touch points supported by the device.


## Capabilities

#### deviceToken
If notification is enabled, returns the latest device token that can be used to send push notifications to this device. 

#### lastLocation.latitude
Returns the latitude of the last known location of the device. This value will only be populated if the action [getLocation](/actions/get-location.md) has been used previously and the user has granted location permission to the app.

#### lastLocation.longitude
Returns the longitude of the last known location of the device. This value will only be populated if the action [getLocation](/actions/get-location.md) has been used previously and the user has granted location permission to the app.
