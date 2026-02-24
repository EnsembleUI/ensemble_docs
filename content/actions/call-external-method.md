# callExternalMethod

*Note this is relevant for developers who are integrating Ensemble with their flutter apps* 

Utilize the `callExternalMethod` action to call a method in your Flutter app. Ensemble allows you to pass Flutter methods into the framework at the time you instantiate `EnsembleApp`.

## Example of registering openApp method that's implemented in Flutter

See how to [embed](https://github.com/EnsembleUI/ensemble/blob/main/starter/lib/main.dart) Ensemble platform in your [existing flutter app](https://github.com/EnsembleUI/ensemble/tree/main/starter)

```dart
  //assuming you have a flutter method called openApp
  Map<String, Function> methods = {
    //appId, screenId and props will be provided by the EDL code when invoking the callExternalMethod action
    'openApp': ({appId, screenId, props}) => openApp(appId!, screenId, props)
  };

//following code is from https://github.com/EnsembleUI/ensemble/blob/main/starter/lib/main.dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  initErrorHandler();
  await EnsembleModules().init();
  runApp(EnsembleApp(
      externalMethods: methods //this is how you can specify one or more Flutter methods that could be invoked from within EDL
    ));
}
```
Here's how to invoke the `openApp` method we registered earlier. 

```yaml
View:
  Column:
    children:
      - Button:
          label: Open App
          onTap:
            callExternalMethod:
              name: openApp
              payload:
                appId: appId
                screenId: screenId
```
Alternatively you can call it in code as follows - 

```js
            ensemble.callExternalMethod({
              name: "openApp",
              payload: {
                appId: appId,
                screenId: screenId
              },
            });
```
