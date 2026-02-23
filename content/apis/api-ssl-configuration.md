# SSL Configuration

SSL (Secure Sockets Layer) configuration in Ensemble allows you to secure your API communications through certificate pinning and verification controls. This guide explains both global and per-API SSL configuration options and their proper usage.

## Configuration Levels

Ensemble supports SSL configuration at two levels:

1. **Global Configuration** - Applied to all APIs by default using environment variables and secrets
2. **Per-API Configuration** - Overrides global settings for specific APIs using the `sslConfig` property

## Global SSL Configuration

### Environment Variables

These settings apply to all APIs unless overridden by per-API configuration:

#### ssl_pinning_enabled
- **Type:** Environment Variable
- **Purpose:** Controls whether SSL certificate pinning is active globally
- **Values:** 'true' or 'false'
- **Default:** false
- **Availability:** Only supported in native apps (not available for web apps)

#### bypass_ssl_pinning
- **Type:** Environment Variable
- **Purpose:** Allows bypassing SSL certificate verification globally
- **Values:** 'true' or 'false'
- **Default:** false
- **Warning:** Should only be used in development environments, never in production

#### bypass_ssl_pinning_with_validation
- **Type:** Environment Variable
- **Purpose:** Bypass SSL pinning while validating against stored certificate fingerprints
- **Values:** 'true' or 'false'
- **Default:** false
- **Usage:** Compares current certificate fingerprint with stored fingerprint from secure storage

### Secrets

#### ssl_pinning_certificate
- **Type:** Secret
- **Purpose:** Provides the certificate for SSL pinning verification
- **Format:** Must be Base64 encoded
- **Behavior:** The app will only trust servers presenting this certificate
- **Dependencies:** Requires `ssl_pinning_enabled` to be 'true'

## Per-API SSL Configuration

For more granular control, you can override global SSL settings for individual APIs using the `sslConfig` property in your API definition.

### Basic Syntax

```yaml
API:
  mySecureAPI:
    uri: https://api.example.com/data
    method: GET
    sslConfig:
      pinningEnabled: true
      bypassPinning: false
      bypassPinningWithFingerprint: false
      fingerprintKey: "api_example_com_fingerprint"
    headers:
      Authorization: Bearer ${token}
```

### sslConfig Properties

#### pinningEnabled
- **Type:** Boolean
- **Purpose:** Enable/disable SSL certificate pinning for this specific API
- **Values:** true or false
- **Overrides:** Global `ssl_pinning_enabled` environment variable
- **Example:** `pinningEnabled: true`

#### bypassPinning
- **Type:** Boolean
- **Purpose:** Bypass SSL certificate verification for this specific API
- **Values:** true or false
- **Overrides:** Global `bypass_ssl_pinning` environment variable
- **Warning:** Use only in development
- **Example:** `bypassPinning: true`

#### bypassPinningWithFingerprint
- **Type:** Boolean
- **Purpose:** Bypass SSL pinning while validating against stored certificate fingerprints
- **Values:** true or false
- **Overrides:** Global `bypass_ssl_pinning_with_validation` environment variable
- **Example:** `bypassPinningWithFingerprint: true`
- **Requirement:** `fingerprintKey` should be set with the same key given in API defination as secureStorage.

#### fingerprintKey
- **Type:** String
- **Purpose:** Specifies the key in secure storage where the certificate fingerprint is stored
- **Default:** "bypass_ssl_fingerprint"
- **Usage:** Used with `bypassPinningWithFingerprint` to retrieve the stored certificate fingerprint for validation
- **Example:** `fingerprintKey: "api_example_com_fingerprint"`

## Certificate Fingerprint Management

When using `bypassPinningWithFingerprint`, you need to store the certificate fingerprint in secure storage. There are two main approaches:

### Method 1: Using Ensemble's setSecureStorage Action

Store the certificate fingerprint manually using Ensemble's secure storage:

```yaml
Button:
  label: Store Certificate Fingerprint
  onTap:
    setSecureStorage:
      key: "api_example_com_fingerprint"
      value: "a1b2c3d4e5f6..." # SHA256 fingerprint of the certificate
      onComplete:
        showToast:
          message: Certificate fingerprint stored
```

### Method 2: Using External Methods (Dynamic Certificate Capture)

For dynamic certificate capture, you can expose external methods from your host application:

#### Host Application Setup (Flutter/Dart Example)

```dart
// In your main.dart or wherever you initialize EnsembleApp
Future<Map<String, dynamic>> captureCertificateForHost({
  required String host, 
  int port = 443
}) async {
  HttpClient httpClient = HttpClient();
  httpClient.connectionTimeout = const Duration(seconds: 10);
  
  String sha256Certificate = '';
  
  httpClient.badCertificateCallback = (X509Certificate cert, String certHost, int certPort) {
    if (certHost.toLowerCase() == host.toLowerCase()) {
      sha256Certificate = sha256.convert(cert.der).toString();
      return true;
    }
    return false;
  };
  
  try {
    HttpClientRequest request = await httpClient.getUrl(Uri.parse('https://$host:$port/'));
    HttpClientResponse response = await request.close();
    await response.drain();
    httpClient.close();
    
    if (sha256Certificate != '') {
      await StorageManager().writeSecurely(
        key: 'bypass_ssl_certificate',
        value: sha256Certificate,
      );
      return {'status': true, 'fingerprint': sha256Certificate};
    } else {
      return {'success': false, 'error': 'Failed to capture certificate'};
    }
  } catch (e) {
    return {'success': false, 'error': e.toString()};
  }
}

// Register the external method
EnsembleApp(
  externalMethods: const {
    'captureCertificateForHost': captureCertificateForHost,
  },
  // ... other properties
)
```

#### Using External Method in Ensemble EDL

```yaml
View:
  onLoad:
    callExternalMethod:
        name: captureCertificateForHost
        payload:
            host: ${HOST}
            port: ${PORT_NUMBER}
        onComplete:
            invokeAPI:
                name: secureAPI
        onError:
            showToast:
            message: "Failed to capture certificate: ${response.error}"
            options:
                type: error

API:
  secureAPI:
    uri: ${HOST}/endpoint
    method: GET
    sslConfig:
      bypassPinningWithFingerprint: true
      fingerprintKey: "api_fingerprint"
    headers:
      Authorization: Bearer ${token}
```



## Configuration Examples

### Example 1: High-Security API with Certificate Pinning

```yaml
API:
  paymentAPI:
    uri: https://secure-payment.example.com/process
    method: POST
    sslConfig:
      pinningEnabled: true
      bypassPinning: false
      bypassPinningWithFingerprint: false
    headers:
      Authorization: Bearer ${paymentToken}
      Content-Type: application/json
    body:
      amount: ${amount}
      currency: USD
```

### Example 2: Development API with SSL Bypass

```yaml
API:
  devTestAPI:
    uri: https://dev-server.example.com/test
    method: GET
    sslConfig:
      pinningEnabled: false
      bypassPinning: true  # Only for development!
      bypassPinningWithFingerprint: false
    headers:
      Authorization: Bearer ${devToken}
```

## Security Best Practices

1. **Production Environment**: Always use certificate pinning (`pinningEnabled: true`) for production APIs
2. **Development Environment**: Use `bypassPinning: true` only during development
3. **Dynamic Environments**: Use `bypassPinningWithFingerprint: true` when dealing with dynamic certificates or multiple environments
4. **Certificate Storage**: Store certificate fingerprints securely using `setSecureStorage` or external methods
