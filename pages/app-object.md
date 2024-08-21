# AppInfo object

Get metadata (information) about your app from Ensemble and from Appstore/Google Play. Does not apply to webapps. 

- appId - Ensemble AppId (ex: GJ4nZIEFlZTv2HQGw)
- appName - App name from Appstore/Google Play
- packageName - Android package name or iOS bundleId
- version - app's version from Appstore/Google Play
- bundleNumber - app's Build Number from Appstore/Google Play
- theme - The app's current theme
- themes - List of all configured themes

See the [themes docs](/theme-and-styling/theme) for more details.

```yaml
View:
  styles:
    scrollableView: true
  header:
    title: AppInfo
  body:
    Column:
      styles:
        gap: 16
        padding: 24
      children:
        - Text:
            text: "${appInfo.appId}"
        - Text:
            text: "${appInfo.appName}"
        - Text:
            text: "${appInfo.packageName}"
        - Text:
            text: "${appInfo.version}"
        - Text:
            text: "${appInfo.buildNumber}"
```
