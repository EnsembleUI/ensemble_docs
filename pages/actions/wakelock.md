# wakelock

The wakelock action controls the device's screen wakelock, preventing the screen from automatically turning off while the app is in use. This is particularly useful for apps that display information users need to view continuously without interaction, such as recipe apps, navigation, or presentation modes.

### Properties

| Property   | Type    | Description                                                                                           |
| :--------- | :------ | :---------------------------------------------------------------------------------------------------- |
| enable     | boolean | Controls the wakelock state. `true` to keep screen on, `false` to allow normal screen timeout. (default: true) |
| onComplete | action  | Callback Action executed after the wakelock state is successfully changed                              |
| onError    | action  | Callback Action if wakelock operation fails. Error details available under 'error' field               |

**Example**

```yaml
View:
  header:
    title: Wakelock Control
  body:
    Column:
      styles: { gap: 16, padding: 24 }
      children:
        - Button:
            label: Enable Wakelock
            onTap:
              wakelock:
                enable: true
                onComplete: |
                  //@code
                  status.text = 'Wakelock enabled - screen will stay on';
                onError: |
                  //@code
                  status.text = 'Error: ' + error;
        - Button:
            label: Disable Wakelock
            onTap:
              wakelock:
                enable: false
                onComplete: |
                  //@code
                  status.text = 'Wakelock disabled - normal screen timeout';
        - Button:
            label: Check Wakelock Status
            onTap: |
              //@code
              status.text = 'Wakelock is ' + (device.wakelockEnabled ? 'enabled' : 'disabled');
        - Text:
            id: status
            text: Press a button to control wakelock
```

### Use Cases

- **Recipe/Cooking Apps**: Keep the screen on while users are following cooking instructions
- **Navigation**: Prevent screen timeout during route guidance
- **Presentations**: Keep display active during slideshows or demonstrations
- **Reading Apps**: Allow continuous reading without screen dimming
- **Fitness Apps**: Keep workout instructions visible during exercise sessions

### Note

The wakelock state can be checked at any time using `device.wakelockEnabled`, which returns `true` if the wakelock is currently active and `false` otherwise.
