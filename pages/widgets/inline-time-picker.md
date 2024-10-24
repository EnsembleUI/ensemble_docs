Here's the updated documentation for the `InlineTimePicker` widget with the correct link to the Kitchen Sink:

# InlineTimePicker Widget

The InlineTimePicker widget provides an intuitive, iOS-style time selection interface that allows users to select hours, minutes, and optionally seconds, all within the same view. It is designed to offer a smooth and customizable time-picking experience directly within the interface, without the need for opening a dialog.

[Test in Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/HGdWHF4G23mpkHBV8o3F)

## Key Concepts

- **mode**: Defines the format of the time picker. You can choose between hours and minutes (`hm`), minutes and seconds (`ms`), or hours, minutes, and seconds (`hms`).
- **selectedTime**: Retrieves the current selected time as a formatted string, including hours, minutes, and seconds if applicable.
- **onTimeChanged**: Executes an action when the selected time is changed by the user. This allows developers to perform tasks such as updating other parts of the UI or triggering business logic.
- **minuteInterval**: Sets the interval for minute selection, allowing for customization of the granularity of minute steps.
- **secondInterval**: Sets the interval for second selection, providing control over how precisely seconds can be selected.
- **onTimeChangedHaptic**: Allows the addition of haptic feedback when the time is changed, enhancing the tactile interaction experience for users.
- **initialTime**: Specifies the initial time that the picker will display when it is first rendered.

## Example

Here’s an example of how to use the InlineTimePicker widget in a YAML configuration:

```yaml
View:
  header:
    title: InlineTimePicker
  styles:
    scrollableView: true
  body:
    Column:
      children:
        - InlineTimePicker:
            id: timePicker
            initialTime: "11:44"
            mode: hms
            showHourLabel: false

        - Button:
            label: Get Time
            onTap: |
              //@code
              console.log(timePicker.selectedTime);
```

In this example:
- The `InlineTimePicker` is configured to use the `hms` mode, which allows the selection of hours, minutes, and seconds.
- The `initialTime` is set to `"11:44"`, which is the time the picker will display when first rendered.
- The `showHourLabel` is set to `false`, hiding the hour label from the picker.
- The button logs the selected time in the format `hh:mm:ss a` to the console when pressed.

## Reference
#### Properties

| Property            | Type                                   | Description                                                                                               |
| :------------------ |:---------------------------------------|:----------------------------------------------------------------------------------------------------------|
| mode                | enum | Defines the format of the time picker. Options are `hm` (hours and minutes), `ms` (minutes and seconds), or `hms` (hours, minutes, and seconds). |
| selectedTime        | string | Returns the selected time as a formatted string, including hours, minutes, and seconds if the `hms` mode is used. |
| onTimeChanged       | action | Executes a specified action whenever the time selection changes.                                               |
| minuteInterval      | int | Sets the interval for minute selection (e.g., 1, 5, 10). This determines the steps in which minutes can be selected. |
| secondInterval      | int | Sets the interval for second selection (e.g., 1, 10, 15). This determines the steps in which seconds can be selected. |
| onTimeChangedHaptic | string | Adds haptic feedback when the time is changed, providing a tactile response for the user.                       |
| initialTime         | string | Sets the initial time displayed by the picker when it is first rendered (formatted as `HH:mm`).                 |
| showHourLabel       | bool | Controls whether the hour label is displayed in the time picker.                                                |

## Example Usage
This widget is ideal for scenarios where you want users to pick a specific time within the app, without having to open a new screen or dialog. It is particularly useful in settings such as alarm clocks, event schedulers, or any application that requires precise time input.

### Mode Examples
- **hm (Hours and Minutes)**: Useful for scenarios where second precision is not required, such as setting a meeting time.
- **ms (Minutes and Seconds)**: Ideal for countdowns or timers.
- **hms (Hours, Minutes, and Seconds)**: Provides the full range of time selection, perfect for more detailed scheduling needs.

By customizing the `minuteInterval` and `secondInterval`, developers can control how fine-grained the time selection is, ensuring that users can quickly and accurately select the desired time.

This widget can be fully integrated with other actions and components in your app, offering flexibility and ease of use in time-based interactions.