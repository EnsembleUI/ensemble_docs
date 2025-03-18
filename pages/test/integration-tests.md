# Automated Testing

Ensemble apps support automated testing using Flutter's integration testing framework. You can easily find and interact with widgets in your tests using the `testId` property.

## Adding testIds to your widgets

Add `testId` properties to widgets in your YAML to make them findable in tests:

```yaml
Button:
  testId: navigate_button
  label: Navigate to Goodbye Screen
  onTap:
    navigateScreen:
      name: Goodbye
```

## Writing integration tests

The [starter project](https://github.com/EnsembleUI/ensemble/tree/main/starter) includes an example integration test at [`integration_test/app_test.dart`](https://github.com/EnsembleUI/ensemble/blob/main/starter/integration_test/app_test.dart) that demonstrates:

- Finding widgets by testId using `find.byKey(ValueKey('testId'))`
- Interacting with widgets (tap, enter text, etc.)
- Navigating between screens
- Verifying widget states

Here's a simplified example:

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:ensemble_starter/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  group('Ensemble App Testing', () {
    testWidgets('Test navigation flow', (WidgetTester tester) async {
      app.main();
      await tester.pumpAndSettle();

      // Find widgets by testId
      final buttonFinder = find.byKey(ValueKey('navigate_button'));
      expect(buttonFinder, findsOneWidget);

      // Interact with widgets
      await tester.tap(buttonFinder);
      await tester.pumpAndSettle();
      
      // Verify navigation worked
      final secondScreenTextFinder = find.byKey(ValueKey('goodbye_title'));
      expect(secondScreenTextFinder, findsOneWidget);
    });
  });
}
```

## Running tests

Run your integration tests with:

```bash
flutter test integration_test/app_test.dart
```

For more information on Flutter integration tests, see the [Flutter Testing documentation](https://docs.flutter.dev/testing/integration-tests).
