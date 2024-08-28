# Stack

The Stack Widget allows you to visually stack items on top of each other, providing a flexible and layered approach to layout and design within your application.

[Test in Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/572ecf3b-b9f2-46f4-960f-ff438e5fa1dc)

## Properties

| Property | Type   | Description               |
| :------- | :----- | :------------------------ |
| children | array  | List of widgets           |
| styles   | object | [See properties](#styles) |

### styles

| Property      | Type   | Description                                                                                                                                                                                                                                                                                      |
| :------------ | :----- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alignChildren | string | How to align the children within the stack such that their alignment points will be the same (default is topStart). Each child can override this with alignment property. `topLeft`, `topCenter`, `topRight`, `centerLeft`, `center`, `centerRight`, `bottomLeft`, `bottomCenter`, `bottomRight` |
| enableSplashFeedback                      | boolean                                                    | Toggles splash effect feedback for the widget when        `true`.                                                                                                            |
| splashColor                      | string                                                    | Defines the color of the splash effect when `enableSplashFeedback` is true.                                                                                                                                                         |
| splashDuration                      | integer                                                    | This is the duration it takes to fill the widget surface with the splashColor.The duration in ms when tap and release on the widget.                                                                                                                                                         |
| splashFadeDuration                      | integer                                                    | The duration it takes to fade out once tapped. Since a typical tap starts and ends immdiately, this splashFadeDuration executes almost at the same time as the splashDuration, so ideally it should be equal or longer than splashDuration to see the entire effect.                                                                                                                                                         |
| unconfirmedSplashDuration                      | integer                                                    | This happens when the user tap and hold (not yet released). It is called unconfirmed since the tap will be cancelled if the user moves out of the tap area and release. Usually this should be longer (around 1 secs) to signify that the user has not confirmed the tap.                                                                                                                                                         |