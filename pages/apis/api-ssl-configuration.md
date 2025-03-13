# SSL Configuration

SSL (Secure Sockets Layer) configuration in Ensemble allows you to secure your API communications through certificate pinning and verification controls. This guide explains the available SSL configuration options and their proper usage.

## Available Configuration Options

### ssl_pinning_enabled

- **Type:** Environment Variable
- **Purpose:** Controls whether SSL certificate pinning is active
- **Behavior:** When set to 'true', the app will only trust connections with certificates matching the provided certificate
- **Availability:** Only supported in native apps (not available for web apps)
- **Default:** false

### ssl_pinning_certificate

- **Type:** Secret
- **Purpose:** Provides the certificate for SSL pinning verification
- **Format:** Must be Base64 encoded
- **Behavior:** The app will only trust servers presenting this certificate
- **Dependencies:** Requires `ssl_pinning_enabled` to be 'true'

### bypass_ssl_pinning

- **Type:** Environment Variable
- **Purpose:** Allows bypassing SSL certificate verification
- **Warning:** Should only be used in development environments, never in production
- **Behavior:** When 'true', bypasses all SSL certificate verification
- **Default:** false

## Security Considerations

1. Certificate pinning provides protection against man-in-the-middle attacks
2. SSL bypass shouldn't be used in production environments as it will create security concerns.
3. Web applications cannot use SSL pinning and rely on browser-based verification
