# Managing Unnecessary Android Permissions

When we include Ensemble dependencies in our host project, the merged Android manifest file of APK can include permissions from all plugins, even those we're not actively using. This can lead to unnecessary permissions being requested from users and potential app store rejections.

## The Problem

For example, if we include Firebase Analytics in our dependencies, it might automatically add advertising-related permissions like:
- `com.google.android.gms.permission.AD_ID`
- `android.permission.ACCESS_ADSERVICES_ATTRIBUTION` 
- `android.permission.ACCESS_ADSERVICES_AD_ID`

Even if we're not using advertising features, these permissions will be included in our final APK.

## The Solution

we can explicitly remove unwanted permissions from our Android manifest using the `tools:node="remove"` attribute.

### Step 1: Add the tools namespace

Make sure our `android/app/src/main/AndroidManifest.xml` file includes the tools namespace in the root manifest tag:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
```

### Step 2: Remove unwanted permissions

Add the following permissions with `tools:node="remove"` to explicitly remove them from our final manifest:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!-- Remove ad-related permissions -->
    <uses-permission android:name="com.google.android.gms.permission.AD_ID" tools:node="remove" />
    <uses-permission android:name="android.permission.ACCESS_ADSERVICES_ATTRIBUTION" tools:node="remove" />
    <uses-permission android:name="android.permission.ACCESS_ADSERVICES_AD_ID" tools:node="remove" />

    <!-- our other permissions and application tag -->
    <application>
        <!-- our app content -->
    </application>
</manifest>
```

### Step 3: Verify the changes

After making these changes:

1. Clean our project: `flutter clean`
2. Rebuild our app: `flutter build apk --debug`
3. Verify the permissions oure removed by checking the final APK using tools like `aapt` or Android Studio's APK Analyzer

This approach ensures our Ensemble app only requests the permissions it actually needs, providing a better user experience and maintaining security best practices.