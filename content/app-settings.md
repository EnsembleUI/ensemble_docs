# App Settings

Navigate to your app in Ensemble Studio to use the following settings:

1. [Environment variables](#environment-variables)
2. [Secrets](#secrets)

## Environment variables

Add variables you intend to use throughout your app here. We recommend to use this for:

- API endpoints
- 3rd-party service variables, such as service configs and URLs

### Using environment variables

Throughout your app, you can reference the environment variable with `${env.key_name}`. For instance, the API definitions can reference a variable:

```yaml
API:
    getUser:
        url: ${env.apiEndpoint}
        method: GET
```

## Secrets

Your app may require using sensitive values for managing access to remote data. Ensemble supports configuring development secrets easily and securely during runtime, and the ability to inject separate production secrets when deploying.

<img src="/images/secrets_config.png" alt="Add Secret" style="border: solid 1px lightgrey" />

Only application owners and editors can add or change secret values due to their sensitive nature.

### Using secrets

Any screens can reference the variable with `${secrets.key_name}`. Here we are simply displaying the secret value in a text field.

<img src="/images/secrets_usage.png" alt="Use Secret" style="border: solid 1px lightgrey" />

### Inject production secrets for deployment

You can override your secrets for deployment from the .env file in your Ensemble project by using the same key with a different value.

We do not recommend version controlling your .env file as this will expose your secrets. Consider removing your .env file from version control or injecting secrets at build time.