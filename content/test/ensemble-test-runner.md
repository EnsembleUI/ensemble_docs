# Ensemble Test Runner

The Ensemble Test Runner lets app developers test real Ensemble screens with readable YAML instead of writing Flutter widget-test code. Tests run inside Flutter's test environment and can combine user actions, assertions, API mocks, local state, screenshots, and CI reports.

Use it for repeatable app behavior such as login, onboarding, device setup, error recovery, and navigation. Use regular Flutter integration tests when you need a physical device, platform services, or testing outside the Flutter test process.

## Project Layout

A typical local app suite looks like this:

```text
your_app/
  ensemble/
    ensemble-config.yaml
    apps/your_app/
      tests/
        config.yaml
        login.test.yaml
        home.test.yaml
        mocks/
          common.mock.json
```

Each `*.test.yaml` file is one test definition. `tests/config.yaml` contains settings shared by the whole suite.

## Prerequisites

- A Flutter app that loads Ensemble definitions from local YAML.
- Flutter and Dart installed on the machine or CI agent.
- The [Ensemble CLI](https://www.npmjs.com/package/@ensembleui/cli).
- `ensemble_test_runner` in `dev_dependencies`.
- Stable `testId` values on widgets that tests interact with or assert against.

The runner is a development tool. Do not include it in a production app build.

## Installation

### Install the Ensemble CLI

Install the CLI globally with npm:

```bash
npm install --global @ensembleui/cli
```

Verify that it is available:

```bash
ensemble --version
```

The CLI provides the `ensemble test` command used throughout this guide.

### Configure local definitions

In the app's `ensemble/ensemble-config.yaml`, point the local definition provider at the app definitions:

```yaml
definitions:
  local:
    path: ensemble/apps/your_app
    appHome: screens
    i18n:
      path: translations
```

The exact path depends on your project layout. The configured directory must contain the screens and `tests/` directory used by the suite.

### Add the dependency

Add the published runner package under `dev_dependencies`:

```yaml
dev_dependencies:
  ensemble_test_runner: ^latest
```

See the [`ensemble_test_runner` package on pub.dev](https://pub.dev/packages/ensemble_test_runner) for the latest published version.

Then run:

```bash
flutter pub get
```

A published runner version can be used instead when it matches your Ensemble release.

## Add Test IDs

Tests find widgets by `testId`. Use stable semantic names that describe the widget's role, not its position or translated label:

```yaml
Button:
  testId: login_button
  label: Log in
  onTap:
    navigateScreen:
      name: Home
```

```yaml
TextInput:
  testId: email_field
  label: Email
```

For custom widgets, put `testId` on the custom widget instance. The runner treats it as the test-facing identifier and does not expose internal custom-widget representations in normal diagnostics.

Good IDs include `login_button`, `home_title`, `device_card`, and `setup_apply_button`. Avoid generated IDs, translated text, array indexes, and implementation names.

## Your First Test

Create `tests/hello-home.test.yaml`:

```yaml
id: hello_home_renders
description: The home screen displays the configured user's greeting.
feature: home
tags: [smoke]
startScreen: Hello Home

initialState:
  storage:
    helloApp:
      name:
        first: John
        last: Doe

steps:
  - expectVisible:
      id: greeting_text
```

Run from the wrapper or app root:

```bash
ensemble test
```

The runner discovers `tests/*.test.yaml`, prepares the app, executes the steps, and writes artifacts under `build/ensemble_test_runner/`.

## Test File Reference

Every test requires `id`, `startScreen`, and `steps`.

### Metadata

```yaml
id: devices_empty_state
type: regression
feature: devices
tags: [smoke, devices]
description: Devices shows the empty state when no devices are available.
owner: networking-team
priority: high
parallel: true
retry: 1
```

- `id`: unique stable identifier used by selection, reports, and history.
- `type`: optional team classification.
- `feature`: feature name used by `--feature` and the HTML filter.
- `tags`: free-form labels used by `--tag`.
- `description`: explains the behavior and why it matters; shown in the HTML report.
- `owner`: optional responsible team or person.
- `priority`: `p0`, `p1`, `p2`, `p3`, `critical`, `high`, `medium`, or `low`.
- `parallel`: defaults to `true`. Set `false` only for tests that mutate shared state and cannot be isolated.
- `retry`: additional attempts after failure. Keep this low so retries do not hide flaky tests.

### Start screen and inputs

```yaml
startScreen: Home
startScreenInputs:
  userId: test-user
```

`startScreenInputs` is passed to the screen when it is created. A test can restore state captured by another successful test with `session`:

```yaml
id: devices_from_authenticated_home
session: signin
startScreen: Home
steps:
  - tap:
      id: devices_button
```

Keep session tests small and deterministic.

### Initial state

Set state before the screen mounts:

```yaml
initialState:
  storage:
    apiUrl: http://ensemble.test/api
    featureFlags:
      deviceManagement: true
  keychain:
    adminPassword: test-password
  env:
    APP_LOCALE: en
```

The supported namespaces are `storage`, `keychain`, and `env`. Suite-level values from `config.yaml` apply first; test values override matching values.

### Setup

`setup` runs before the start screen mounts. It is useful for resetting a local stub or preparing external state:

```yaml
setup:
  - httpRequest:
      method: POST
      url: ${services.mockServer.url}/api/reset
      expectStatus: 200
      body:
        scenario: empty_catalog
```

Setup supports headless `httpRequest`, `group`, and `optional` actions.

### Steps

Steps execute in order:

```yaml
steps:
  - tap:
      id: login_button
  - waitForNavigation:
      screen: Home
  - expectText:
      text: Welcome
```

The complete machine-readable contract is the [test schema](https://cdn.ensembleui.com/schemas/ensemble_tests_schema.json). The [step vocabulary](https://github.com/EnsembleUI/ensemble/blob/main/tools/ensemble_test_runner/STEP_VOCABULARY.md) is the canonical list of supported actions.

## Suite Configuration

Create one `tests/config.yaml` for shared settings. Missing config is valid and uses safe defaults.

```yaml
mocks:
  - mocks/common.mock.json

initialState:
  storage:
    apiUrl: http://ensemble.test/api
  env:
    APP_LOCALE: en

services:
  - name: mockServer
    command: .venv/bin/python
    arguments: [mock_server/app.py]
    workingDirectory: tools
    readyUrl: /ping

profiles:
  default: standard
  definitions:
    standard:
      mocks:
        - mocks/common.mock.json
        - mocks/standard.mock.json
    alternate:
      mocks:
        - mocks/alternate.mock.json
  groups:
    primary:
      - standard

devices:
  - id: android_en
    platform: android
    model: Samsung Galaxy S20
    locale: en
    theme: light
  - id: iphone_en
    platform: ios
    model: iPhone 15 Pro
    locale: en
    theme: dark

screenshots:
  enabled: true
  includeSteps: []
  excludeSteps: []

performance:
  enabled: true
timers:
  enabled: true
  maxStartAfterSeconds: 1
  maxRepeatIntervalSeconds: 1
dumpTree:
  enabled: true
logApiCalls:
  enabled: true
logStorage:
  enabled: true
```

The config schema is [ensemble_test_config_schema.json](https://cdn.ensembleui.com/schemas/ensemble_test_config_schema.json). Add this editor hint when useful:

```yaml
# yaml-language-server: $schema=https://cdn.ensembleui.com/schemas/ensemble_test_config_schema.json
```

### Config properties

| Property | Purpose |
| --- | --- |
| `mocks` | Shared mock JSON files or inline API definitions. |
| `initialState` | Shared `storage`, `keychain`, and `env` values. |
| `services` | Local processes such as a mock server; the runner waits for readiness and exposes `${services.name.url}`. |
| `profiles` | App/data variants. Profiles can add mocks and initial state; groups expand to multiple profiles. |
| `devices` | Platform/model/locale/theme matrix. Each test runs once per device. |
| `screenshots` | Automatic step screenshots and contact sheets. |
| `performance` | App frame-performance collection. |
| `timers` | Timer validation thresholds. |
| `dumpTree` | Widget-tree diagnostics. |
| `logApiCalls` | API diagnostics attached to results. |
| `logStorage` | Local storage snapshots attached to results. |

These are suite/app settings. Keep test-specific behavior in the test file.

## Devices, Profiles, and Scenarios

### Device matrix

When `devices` is present, every test runs once per device. Expanded IDs look like `test_id[device_id]` and can be selected with `--device`.

`platform` is `android` or `ios`. `model` controls the device preview frame and viewport. `locale` sets `APP_LOCALE`; `theme` is `light` or `dark`.

### Profiles

Profiles are useful when one flow must run against different app data:

```yaml
profiles:
  default: standard
  definitions:
    standard:
      mocks:
        - mocks/common.mock.json
        - mocks/standard.mock.json
    alternate:
      mocks:
        - mocks/alternate.mock.json
  groups:
    all_profiles:
      - standard
      - alternate
```

Select one in a test:

```yaml
id: alternate_setup
profiles: alternate
startScreen: Setup_Start
steps:
  - expectVisible:
      id: setup_start_button
```

Or select several:

```yaml
profiles: [standard, alternate]
```

At the CLI, `--profile` selects matching expanded runs; it does not disable worker sharding.

### Scenarios

Scenarios keep a common flow in one file while varying data:

```yaml
id: device_signal_recovery
feature: device-setup
startScreen: DeviceSetup_Start

scenarios:
  - id: weak_then_good
    description: The device recovers after the signal improves.
    vars:
      initialSignal: weak
      finalSignal: good
  - id: strong_then_good
    vars:
      initialSignal: strong
      finalSignal: good

steps:
  - expectText:
      text: ${scenario.initialSignal}
  - tap:
      id: device_setup_start_button
  - expectText:
      text: ${scenario.finalSignal}
```

Each scenario becomes an independently reported run. Variables are available as `${scenario.name}` in initial state, mocks, and steps. Use scenarios when the workflow is genuinely shared; use separate files when setup or expected behavior is different enough to become hard to read.

## API Mocks

Mocks can be inline or reusable `.mock.json` files:

```yaml
mocks:
  getDevices:
    statusCode: 200
    body:
      devices: []
    delayMs: 250
```

A JSON file uses the API name as its key:

```json
{
  "getDevices": {
    "statusCode": 200,
    "body": {
      "devices": []
    }
  },
  "getFirmwareUpdate": {
    "statusCode": 200,
    "body": {
      "available": false
    }
  }
}
```

Reference it from config or a test:

```yaml
mocks:
  - mocks/common.mock.json
```

### Stateful responses

Use `responses` for successive API calls:

```yaml
mocks:
  getItems:
    responses:
      - body:
          items: []
      - body:
          items:
            - id: item-1
              device: device-1
```

Use `$extends` for a base response and `$merge` to patch selected values:

```json
{
  "getItems": {
    "$extends": "./common.mock.json",
    "$merge": {
      "body.items[0].device": "device-1"
    }
  }
}
```

Keep common responses in a base file and put device/profile differences in profile files. Use `delayMs` to model latency; the API remains in its loading state during the delay.

For workflows where responses change after user actions, a stateful local stub started through `services` is often better than a large static response sequence. Reset it in `setup`.

## Step Catalog

| Family | Steps |
| --- | --- |
| Lifecycle | `openScreen`, `reloadScreen`, `restartApp`, `resetAppState`, `trigger`, `launchApp` |
| Interaction | `tap`, `doubleTap`, `longPress`, `enterText`, `clearText`, `replaceText`, `submitText`, `focus`, `unfocus` |
| Forms | `select`, `selectIndex`, `check`, `uncheck`, `toggle`, `setSlider`, `chooseDate`, `chooseTime` |
| Gestures | `scroll`, `scrollUntilVisible`, `swipe`, `drag`, `pullToRefresh` |
| Synchronization | `wait`, `pump`, `settle`, `waitFor`, `waitForText`, `waitForGone`, `waitForApi`, `waitForNavigation` |
| UI assertions | `expectVisible`, `expectNotVisible`, `expectExists`, `expectNotExists`, `expectText`, `expectNoText`, `expectTextContains`, `expectEnabled`, `expectDisabled` |
| Value assertions | `expectValue`, `expectChecked`, `expectSelected`, `expectProperty`, `expectStyle`, `expectCount`, `expectListCount`, `expectListContains`, `expectListItem`, `expectEmpty`, `expectNotEmpty` |
| Navigation assertions | `expectScreen`, `expectNavigateTo`, `expectVisited`, `expectNotVisited`, `expectBackStack`, `expectCanGoBack`, `goBack` |
| APIs and mocks | `mocks`, `httpRequest`, `resetApiCalls`, `expectApiCalled`, `expectApiNotCalled`, `expectApiCallOrder`, `expectLastApiCall`, `logApiCalls` |
| State | `setStorage`, `expectStorage`, `removeStorage`, `clearStorage`, `setEnv`, `setAuth`, `clearAuth`, `setPermission`, `setDevice`, `setLocale`, `setTheme` |
| Diagnostics | `runScript`, `expectScript`, `expectScriptResult`, `expectConsoleLog`, `expectNoConsoleErrors`, `expectNoRenderErrors`, `expectError`, `expectNoErrors`, `expectAccessible`, `expectSemanticsLabel`, `expectNoOverflow` |
| Control flow | `group`, `repeat`, `optional`, `ifVisible` |

Common example:

```yaml
steps:
  - enterText:
      id: email_field
      text: user@example.com
  - tap:
      id: login_button
  - waitForNavigation:
      screen: Home
  - expectVisible:
      id: home_title
  - expectEnabled:
      id: devices_button
```

Wait for a specific API with a timeout:

```yaml
- waitForApi:
    name: getDevices
    times: 1
    timeoutMs: 15000
```

`wait`/ `pump` advances the Flutter test clock. `settle` waits for pending frames and animations to settle. Neither means “wait for every network request”; use `waitForApi` or an app-visible assertion.

Optional branches handle genuinely optional prompts:

```yaml
- optional:
    steps:
      - tap:
          id: close_tip_button
```

Do not hide required regression assertions inside `optional`.

## Inputs and Variables

Pass repeatable CLI inputs:

```bash
ensemble test \
  --input adminPassword='s4C>M7U6t~' \
  --input expectedDeviceCount=2
```

Use them in YAML:

```yaml
initialState:
  keychain:
    adminPassword: ${inputs.adminPassword}

steps:
  - expectText:
      text: ${inputs.expectedDeviceCount}
```

Inputs are also available in mocks, setup requests, `startScreenInputs`, and scenario variables. Keep secrets in the CI secret store and mask command output.

## CLI Reference

```bash
ensemble test
```

| Option | Purpose |
| --- | --- |
| `--verbose` | Stream app and runner diagnostics. |
| `--app-dir PATH` | Run against a different app directory. |
| `--id ID` | Select test IDs. |
| `--feature NAME` | Select by `feature`. |
| `--profile NAME` | Select profile or profile-group runs. |
| `--tag NAME` | Select by tag. |
| `--path GLOB` | Select test files by path. |
| `--device ID` | Select device-matrix runs. |
| `--input KEY=VALUE` | Supply a repeatable input. |
| `--timeout 30s` | Set suite timeout; seconds, minutes, or hours. |
| `--jobs auto` | Choose worker parallelism; `1` disables workers. |
| `--doctor` | Inspect prerequisites and app configuration. |
| `--validate-only` | Parse and validate without executing. |
| `--report=json` | Emit a machine-readable report. |
| `--report=junit` | Emit JUnit XML. |
| `--report-file PATH` | Write the selected report to a file. |

Selection options can be repeated or comma-separated. A selection matching no expanded run is a configuration error.

CI exit codes are stable: `0` all selected tests passed, `1` test failures, `2` setup/validation/configuration failure, and `3` internal runner failure.

## Reports and Artifacts

Artifacts are written under `build/ensemble_test_runner/`:

- `report/index.html`: interactive static report.
- `report/results.json.gz`: compressed structured results used by the report and CI tools.
- `report/screenshots/`: device-framed screenshot assets when enabled.
- `report/ensemble_test_history.db`: compact local history of recent runs.
- `test_durations.json`: duration cache used to balance future worker shards.

The history database stores bounded recent-run summaries, not the full screenshot set. Publish the HTML report and its screenshots together because the HTML references local assets. Optional artifact failures produce warnings and do not replace the real test result.

Screenshots are captured at step boundaries and assembled into per-test contact sheets. `includeSteps` and `excludeSteps` belong in `config.yaml`. Disable screenshots for fast local validation when visual evidence is not needed.

## CI Usage

A minimal CI job checks out the app, installs dependencies, and runs the same command as developers:

```bash
flutter pub get
ensemble test \
  --report=json \
  --report-file=build/ensemble_test_runner/report/results.json
```

Publish `build/ensemble_test_runner/report/` as a pipeline artifact. For a PR comment, use a concise CI summary rather than the verbose log.

For a faster PR check, select a smoke feature or profile:

```bash
ensemble test --feature=smoke --device=android
```

Keep the full matrix in a scheduled or manual pipeline if it is too expensive for every change.

## Best Practices

1. Test user-visible behavior, not implementation details.
2. Give every interactive or asserted widget a stable semantic `testId`.
3. Keep one behavior per test. Use scenarios only when steps are genuinely shared.
4. Put shared mocks and initial state in `config.yaml`; keep differences in tests or profiles.
5. Prefer a stateful local stub for workflows where responses change after user actions.
6. Use `delayMs` only when loading behavior matters.
7. Wait for meaningful conditions rather than arbitrary sleeps.
8. Reset mutable stub state in `setup`.
9. Keep retries at zero unless a transient failure is understood.
10. Use `feature`, tags, profiles, and descriptions so CI and HTML remain useful.
11. Keep secrets in CLI/CI inputs, never committed YAML or mock files.
12. Run `--validate-only` before opening a pull request.

## Troubleshooting

### No tests are discovered

Check that definitions use `local`, the configured path contains `tests/`, files end in `.test.yaml`, each test has required fields, and profile/device selection did not filter out every run.

```bash
ensemble test --doctor
ensemble test --validate-only
```

### A widget cannot be found

Confirm the widget's `testId`, the current screen, and the preceding navigation/loading condition. Prefer `waitForNavigation`, `waitFor`, or `waitForText` before increasing timeouts.

### A mock is not used

Confirm the API name, the `.mock.json` path relative to the tests asset root, and the selected profile. Enable `logApiCalls.enabled` to inspect observed calls.

### Parallel runs are flaky

Remove shared state, reset the stub in `setup`, or set `parallel: false` only for tests that truly require serial execution. Do not disable all parallelism first.

### A screenshot is missing

Check `screenshots.enabled`, `includeSteps`, and `excludeSteps`. Screenshots are taken after the step's settled state; add a meaningful wait/assertion when the state is short-lived.

### Need exact syntax

Use the version-matched [test schema](https://cdn.ensembleui.com/schemas/ensemble_tests_schema.json), [config schema](https://cdn.ensembleui.com/schemas/ensemble_test_config_schema.json), and [step vocabulary](https://github.com/EnsembleUI/ensemble/blob/main/tools/ensemble_test_runner/STEP_VOCABULARY.md).
