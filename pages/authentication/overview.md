# Authentication
Ensemble supports Sign In with Google, Apple as well as with Auth0.

## Setup
By default Sign in is disabled. To enable it, follow the setup steps below.

### Enable the Auth module
- Go to `/starter/pubspec.yaml` and uncomment the `ensemble_auth`.
- Go to `/starter/lib/generated/EnsembleModules.dart`
  - Set `useAuth` to `true`.
  - Uncomment the `if` section to enable the AuthModuleImpl. You may also need to uncomment the import statement.

### Sign in with Apple
Note that if you are using Sign in with Google on iOS, Apple requires you to also support Sign in with Apple. To enable Sign in with Apple, follow these steps:
- Open XCode from the iOS project under `/starter/ios` in XCode.
- Select your `Runner` target and go to `Signing & Capabilities` tab.
- Click on the `+ Capability` button and select "Sign in with Apple".

## Implementation
- For Sign in with Google locally or with your server, go to [Social Sign In](/authentication/social-signin).
- To use Firebase instead of your server, go to [Firebase](/authentication/firebase).
- For Sign in with Auth0, go to [Auth0](/authentication/auth0).