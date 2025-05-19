# clearKeychain

The `clearKeychain` action removes previously stored data from the device's secure keychain (iOS) or equivalent secure storage (Android), allowing you to clean up sensitive information with the highest level of security when it's no longer needed.

## Properties

| Property   | Type   | Description                                                                               |
| :--------- | :----- | :---------------------------------------------------------------------------------------- |
| key        | string | The key to remove from the keychain                                                       |
| onComplete | action | Execute an Action when the data has been successfully removed                             |
| onError    | action | Execute an Action when an error occurs. The error reason is available under 'event.error' |

## Example

```yaml
Button:
    label: Clear Keychain Data
    onTap:
        clearKeychain:
            key: apiKey
            onComplete:
                showToast:
                    message: API key removed from keychain
                    options:
                        type: success
            onError:
                showToast:
                    message: ${event.error}
                    options:
                        type: error
```

## JavaScript Usage

You can also use this action in JavaScript:

```javascript
// Clear a stored keychain value
ensemble.clearKeychain({
    key: "apiKey",
    onComplete: () => {
        console.log("API key removed from keychain");
    },
    onError: (error) => {
        console.error("Failed to clear from keychain: " + error);
    },
});
```

## Notes

-   This action removes data from the device's secure keychain or equivalent OS security storage.
-   This operation completely removes the specified key and its associated value from the keychain.
-   If the key doesn't exist, the action may trigger an error depending on the platform.
-   Use this action for cleanup when sensitive data is no longer needed (e.g., after logout).
-   For security best practices, always clear sensitive data when it's no longer required.
-   This action works with data stored using [saveKeychain](/actions/save-keychain).
-   Unlike `clearSecureStorage`, this operates at the OS-level security layer.
