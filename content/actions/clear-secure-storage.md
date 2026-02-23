# clearSecureStorage

The `clearSecureStorage` action removes previously stored encrypted data from the device's secure storage, allowing you to clean up sensitive information when it's no longer needed, enhancing security by minimizing data exposure.

## Properties

| Property   | Type   | Description                                                                               |
| :--------- | :----- | :---------------------------------------------------------------------------------------- |
| key        | string | The key to remove from secure storage                                                     |
| onComplete | action | Execute an Action when the data has been successfully removed                             |
| onError    | action | Execute an Action when an error occurs. The error reason is available under 'event.error' |

## Example

```yaml
Button:
    label: Clear Secure Data
    onTap:
        clearSecureStorage:
            key: userToken
            onComplete:
                showToast:
                    message: Secure data removed successfully
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
// Clear a stored secure value
ensemble.clearSecureStorage("userToken");

// With error handling
try {
    ensemble.clearSecureStorage("userToken");
    console.log("Token removed successfully");
} catch (error) {
    console.error("Failed to clear token: " + error);
}
```

## Notes

-   This action requires an encryption key to be set in your secrets configuration.
-   This action completely removes the specified key and its associated value from secure storage.
-   If the key doesn't exist, the action completes successfully without any error.
-   Use this action for cleanup when sensitive data is no longer needed (e.g., after logout).
-   For security best practices, always clear sensitive data when it's no longer required.
-   This action works with data stored using [setSecureStorage](/actions/set-secure-storage).
