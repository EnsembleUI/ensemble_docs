# getSecureStorage

The `getSecureStorage` action retrieves previously stored encrypted data from the device's secure storage, decrypting it for use within your application while maintaining security of sensitive information.

## Properties

| Property   | Type   | Description                                                                                                |
| :--------- | :----- | :--------------------------------------------------------------------------------------------------------- |
| key        | string | The key to retrieve the value from                                                                         |
| onComplete | action | Execute an Action when the data has been successfully retrieved. The value is available under 'event.data' |
| onError    | action | Execute an Action when an error occurs. The error reason is available under 'event.error'                  |

## Example

```yaml
Button:
    label: Retrieve Secure Data
    onTap:
        getSecureStorage:
            key: userToken
            onComplete:
                executeCode:
                    body: |
                        //@code
                        console.log("Retrieved token: " + event.data);
                        // Use the token for an API call
                        apiHeaders.value = { "Authorization": "Bearer " + event.data };
            onError:
                showToast:
                    message: ${event.error}
                    options:
                        type: error
```

## JavaScript Usage

When used in JavaScript, this action returns the value directly, making it useful in code blocks:

```javascript
// Retrieve a stored value directly
const userToken = ensemble.getSecureStorage("userToken");
console.log("Token: " + userToken);

// Use the retrieved value in an API call
ensemble.invokeAPI({
    name: "fetchUserData",
    inputs: {},
    headers: {
        Authorization: "Bearer " + ensemble.getSecureStorage("userToken"),
    },
});
```

## Notes

-   This action requires an encryption key to be set in your secrets configuration.
-   The retrieved data is automatically decrypted and converted back to its original data type (string, number, boolean, or object).
-   If no data exists for the given key, `null` will be returned.
-   Data stored using [setSecureStorage](/actions/set-secure-storage) can be retrieved with this action.
-   The value is available in the `onComplete` action under `event.data` when used in YAML.
-   When used in JavaScript, the value is returned directly from the function call.
