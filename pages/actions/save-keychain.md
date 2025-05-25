# saveKeychain

The `saveKeychain` action stores sensitive information in the device's secure keychain (iOS) or equivalent secure storage (Android), providing a high level of OS-level protection for critical data like authentication credentials, tokens, and other sensitive user information.

## Properties

| Property   | Type   | Description                                                                               |
| :--------- | :----- | :---------------------------------------------------------------------------------------- |
| key        | string | The key to store the value under                                                          |
| value      | any    | The value to store in the keychain                                                        |
| onComplete | action | Execute an Action when the data has been successfully stored                              |
| onError    | action | Execute an Action when an error occurs. The error reason is available under 'event.error' |

## Example

```yaml
Button:
    label: Save to Keychain
    onTap:
        saveKeychain:
            key: apiKey
            value: 3f8d9a72e5c6b1f0
            onComplete:
                showToast:
                    message: API key saved to keychain
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
// Store a simple string value
ensemble.saveKeychain({
    key: "apiKey",
    value: "3f8d9a72e5c6b1f0",
});

// Store a complex object
ensemble.saveKeychain({
    key: "accountDetails",
    value: {
        accountId: "ACC123456",
        accessLevel: "premium",
        lastAccess: "2023-05-19T14:30:00Z",
    },
});
```

## Notes

-   The keychain provides OS-level security for storing sensitive data.
-   On iOS, this uses the Keychain Services API.
-   On Android, this uses the Android Keystore System or equivalent secure storage.
-   Values stored in the keychain persist even when the app is uninstalled on iOS (not on Android).
-   To retrieve the value later, use the [readKeychain](/actions/read-keychain) action.
-   To remove the value, use the [clearKeychain](/actions/clear-keychain) action.
-   For less sensitive data that doesn't need OS-level security, consider using [setSecureStorage](/actions/set-secure-storage) instead.
