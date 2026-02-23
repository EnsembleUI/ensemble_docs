# readKeychain

The `readKeychain` action retrieves previously stored data from the device's secure keychain (iOS) or equivalent secure storage (Android), allowing access to sensitive information that was stored with the highest level of OS security protection.

## Properties

| Property   | Type   | Description                                                                                                |
| :--------- | :----- | :--------------------------------------------------------------------------------------------------------- |
| key        | string | The key to retrieve the value from                                                                         |
| onComplete | action | Execute an Action when the data has been successfully retrieved. The value is available under 'event.data' |
| onError    | action | Execute an Action when an error occurs. The error reason is available under 'event.error'                  |

## Example

```yaml
Button:
    label: Read from Keychain
    onTap:
        readKeychain:
            key: apiKey
            onComplete:
                executeCode:
                    body: |
                        //@code
                        console.log("Retrieved API key: " + event.data);
                        apiKeyInput.value = event.data;
            onError:
                showToast:
                    message: ${event.error}
                    options:
                        type: error
```

## JavaScript Usage

It is only available in YAML, as this calls a async function whose return type is Future and we use callbacks to handle the result. Our JS is sync and we cannot use async/await in JS.

## Notes

-   This action reads from the device's secure keychain or equivalent OS security storage.
-   Unlike the `getSecureStorage` action, this operation is asynchronous and must use callbacks even in JavaScript.
-   The retrieved data is converted back to its original data type (string, number, boolean, or object).
-   If no data exists for the given key, the onError callback will be triggered.
-   Data stored using [saveKeychain](/actions/save-keychain) can be retrieved with this action.
-   The value is available in the `onComplete` action under `event.data`.
-   This action provides access to data with OS-level security protection.
