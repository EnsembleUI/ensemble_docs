# logEvent

logEvent action allows you to track analytics events and user interactions using Firebase Analytics, MoEngage, or Adobe Analytics.

## Properties
| Property | Type | Description | Default |
|:---------|:-----|:------------|:--------|
| provider | String | Analytics provider ("firebase", "moengage", "adobe") | "firebase" |
| operation | String | Operation to perform (see provider-specific operations) | "logEvent" |
| name | String | Name of the event to track (required for Firebase and MoEngage trackEvent) | - |
| parameters | Object | Additional parameters for events | {} |
| value | Any | Value for MoEngage operations (location, user attributes etc) | - |
| attributeKey | String | Key for MoEngage custom attributes | - |  
| logLevel | enum | Log level ("info", "debug", "fatal") | "info" |
| onSuccess | Action | Action to execute on success | - |
| onError | Action | Action to execute on error | - |
| userId | String | User ID for Firebase setUserId operation | - |

## Firebase Provider

Firebase provider enables basic analytics event tracking and user identification.

### Operations

#### logEvent (Default)
Logs an analytics event to Firebase. Requires name and optional parameters.

```yaml
Button:
  label: Track Purchase 
  onTap:
    logEvent:
      name: purchase_complete
      parameters:
        amount: 99.99
        currency: USD
```

#### setUserId 
Sets the user identifier for Firebase Analytics.

```yaml
logEvent:
  provider: firebase
  operation: setUserId
  userId: "user123" 
```

## MoEngage Provider
MoEngage provider enables comprehensive user engagement features including event tracking, user attributes, and in-app messaging.

### MoEngage User Profile Operations
| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| setUniqueId | Sets a unique identifier for a user. This should be a unique and consistent identifier for the user across sessions. | value (String) |
| setUserName | Tracks full name as a user attribute. | value (String) |
| setFirstName | Tracks first name portion as a separate user attribute. | value (String) |
| setLastName | Tracks last name portion as a separate user attribute. | value (String) |
| setEmail | Tracks user's email ID as attribute for communication and identification. | value (String) |
| setPhoneNumber | Tracks user's phone number as attribute for communication. | value (String) |
| setBirthDate | Sets user's birth date. Must be in ISO format: yyyy-MM-dd'T'HH:mm:ss.fff'Z' | value (ISO date string) |
| setGender | Sets user's gender for demographic data. | value (enum: male/female) |
| setAlias | Updates user's unique ID that was previously set via setUniqueId. Use this to migrate IDs. | value (String) |
| setLocation | Sets user's geographic location for location-based targeting. | value (Object: {latitude: number, longitude: number}) |
| setAppStatus | Indicates whether this is a fresh install or app update. | value (enum: install/update) |

### MoEngage Custom Attributes
| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| custom | Sets a custom user attribute. Supports primitive types (String, Number, Boolean), arrays of primitives, and valid JSON objects/arrays. Cannot be empty. | attributeKey (String), value (Any supported type) |
| timestamp | Sets a date/time attribute in ISO format. | attributeKey (String), value (ISO date string) |
| locationAttribute | Sets a location-based attribute for geo-targeting. | attributeKey (String), value ({latitude: number, longitude: number}) |

### MoEngage Event & Campaign Operations 
| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| trackEvent | Tracks an analytics event with optional properties. Properties support same types as custom attributes. | name (String), parameters (Object, optional) |
| showInApp | Shows an in-app message if one is available. | None |
| showNudge | Shows a non-intrusive nudge notification. If position not specified, uses default position. | value (enum: top, bottom, bottomLeft, bottomRight, any) | 
| setContext | Sets the current context for in-app message targeting. Contexts determine when messages can be shown. | value (String[]) |
| resetContext | Removes all previously set contexts for in-app targeting. | None |

### MoEngage Push Notification Operations
| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| registerForPush | Registers for push notifications (iOS only). | None |
| registerForProvisionalPush | Registers for provisional push notifications (iOS only). | None |
| passFCMToken | Passes Firebase Cloud Messaging token to SDK (Android only). | value (String - FCM token) |
| passPushKitToken | Passes PushKit token to SDK (Android only). | value (String - PushKit token) |
| passFCMPushPayload | Passes FCM push notification payload to SDK (Android only). | value (Object - FCM payload) |
| requestPushPermission | Requests push notification permission (Android 13+). | None |
| updatePermissionCount | Updates count of permission requests made. | value (Number) |
| pushPermissionResponse | Notifies SDK about push permission response. | value (Boolean) |

### MoEngage SDK Configuration Operations
| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| enableSdk | Enables all SDK features. By default enabled. | None |
| disableSdk | Disables all SDK features. | None |
| enableDataTracking | Enables analytics tracking. By default enabled. | None |  
| disableDataTracking | Disables all analytics tracking. No events/attributes will be tracked. | None |
| enableDeviceIdTracking | Enables device ID tracking (Android only). By default enabled. | None |
| disableDeviceIdTracking | Disables device ID tracking (Android only). | None |
| enableAndroidIdTracking | Enables Android ID tracking. By default disabled. | None |
| disableAndroidIdTracking | Disables Android ID tracking. | None |
| enableAdIdTracking | Enables advertising ID tracking. By default disabled. | None |
| disableAdIdTracking | Disables advertising ID tracking. | None |
| logout | Invalidates current user session and creates new one. | None |
| deleteUser | Deletes current user data from MoEngage (Android only). Returns UserDeletionData. | None |

### Examples

#### Track Event
```yaml
logEvent:
  provider: moengage
  operation: trackEvent
  name: "level_complete"
  parameters:
    level: 5
    score: 1000
```

#### Set User Profile
```yaml
logEvent:
  provider: moengage
  operation: setUserName
  value: "John Smith"
  onSuccess: |
    //@code
    console.log("User name updated")
```

#### Show In-App Message
```yaml
logEvent:
  provider: moengage
  operation: showInApp
```

## Adobe Analytics Provider

Adobe Analytics provider enables comprehensive analytics tracking, user identity management, consent management, and user profile management.

### Core Operations

| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| trackAction | Tracks user interactions and events. | name (String), parameters (Object with event details) |
| trackState | Tracks page views and screen states. | name (String), parameters (Object with state details) |
| sendEvent | Sends an Experience event to Adobe Experience Platform Edge Network. | name (String), parameters (Object with xdmData) |

### Identity Management Operations

| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| getExperienceCloudId | Retrieves the Experience Cloud ID (ECID). | None |
| getIdentities | Gets all identities in the Identity for Edge Network extension. | None |
| updateIdentities | Updates the currently known identities within the SDK. | parameters (Object with identities) |

### Consent Management Operations

| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| getConsents | Retrieves current consent preferences. | None |
| updateConsent | Merges existing consents with given consents. | parameters (Object with allowed boolean) |
| setDefaultConsent | Sets default consent for the SDK. | parameters (Object with allowed boolean) |

### User Profile Operations

| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| getUserAttributes | Gets user profile attributes matching provided keys. | parameters (Object with attributes array) |
| updateUserAttributes | Sets multiple user profile attributes. | parameters (Object with attributeMap) |
| removeUserAttributes | Removes user profile attributes matching provided keys. | parameters (Object with attributes array) |

### Adobe Assurance Operations

| Operation | Description | Required Properties |
|:----------|:------------|:-------------------|
| setupAssurance | Configures Adobe Assurance for debugging. | parameters (Object with url) |

For detailed examples of Adobe Analytics operations, see the [Adobe Analytics documentation](../adobe-analytics.mdx).
