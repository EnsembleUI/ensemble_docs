# setSecureStorage

The `setSecureStorage` action securely stores sensitive information in an encrypted format on the device, ensuring that sensitive data like tokens, user credentials, or personal information remains protected from unauthorized access.

## Properties

| Property   | Type   | Description                                                                               |
| :--------- | :----- | :---------------------------------------------------------------------------------------- |
| key        | string | The key to store the value under                                                          |
| value      | any    | The value to store securely. Can be a string, number, boolean, or complex object          |
| onComplete | action | Execute an Action when the data has been successfully stored                              |
| onError    | action | Execute an Action when an error occurs. The error reason is available under 'event.error' |

## Example

```yaml
Button:
    label: Save Secure Data
    onTap:
        setSecureStorage:
            key: userToken
            value: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyfQ
            onComplete:
                showToast:
                    message: Token stored securely
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
ensemble.setSecureStorage({
    key: "userToken",
    value: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
});

// Store a complex object
ensemble.setSecureStorage({
    key: "userProfile",
    value: {
        id: 123,
        name: "John Doe",
        isActive: true,
        permissions: ["read", "write"],
    },
});
```

## Notes

-   This action requires an encryption key to be set in your secrets configuration.
-   The value can be any type of data - strings, numbers, booleans, or complex objects.
-   All data is encrypted before storage using AES encryption.
-   To retrieve the value later, use the [getSecureStorage](/actions/get-secure-storage) action.
-   To remove the value, use the [clearSecureStorage](/actions/clear-secure-storage) action.
