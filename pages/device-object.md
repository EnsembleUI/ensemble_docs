# Device object

You have access to the following properties of the device.

## device.platform

Returns the device platform, such as `web`, `ios`, `android`, `windows`, and `mac`.

```yaml
View:
  body:
    Text:
      text: ${device.platform}
```


## device.width and device.height

Returns the device width and height as integers.

```yaml
View:
  body:
    Text:
      text: Current device is ${device.height} by ${device.width}
```

## Safe area

A safe area defines the area within a view that isn’t covered by a navigation bar, tab bar, toolbar, etc. Safe areas are essential for avoiding a device’s interactive and display features, like the Dynamic Island on iPhone. 

[See Apple Guidelines](https://developer.apple.com/design/human-interface-guidelines/layout)

[Android Guidelines](https://developer.android.com/develop/ui/views/layout/display-cutout)

It is only relevant if your view does not have a `header` and uses `useSafeAra: false`.


```yaml
View:
  styles:
    useSafeArea: false

  body:
    Column:
      styles:
        padding: 40
      children:
        - Text:
            text: Size of top area used by device is ${device.safeAreaTop}
        - Text:
            text: Size of bottom area used by device is ${device.safeAreaBottom}
```

## device.wakelockEnabled

Returns a boolean indicating whether the device's screen wakelock is currently active. When the wakelock is enabled (`true`), the screen will not automatically turn off due to inactivity. When disabled (`false`), the device follows its normal screen timeout settings.

```yaml
View:
  body:
    Column:
      styles: { gap: 16, padding: 24 }
      children:
        - Text:
            text: Wakelock is ${device.wakelockEnabled ? 'enabled' : 'disabled'}
        - Button:
            label: Toggle Wakelock
            onTap:
              wakelock:
                enable: ${!device.wakelockEnabled}
```

This property is useful for checking the current wakelock state before toggling it or displaying the status to users. See the [wakelock action](/actions/wakelock) for controlling the wakelock state.
