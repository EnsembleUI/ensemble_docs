# initializeStripe

Initialize Stripe with custom configuration. This is the primary way to initialize Stripe in your application.

## Properties

| Property           | Type   | Description                                                                              |
| :----------------- | :----- | :--------------------------------------------------------------------------------------- |
| publishableKey     | string | Your Stripe publishable key (required)                                                   |
| stripeAccountId    | string | Your Stripe account ID for Connect applications (optional)                               |
| merchantIdentifier | string | Your merchant identifier for Apple Pay (optional)                                         |
| onSuccess          | action | Action to execute when initialization succeeds (optional)                                 |
| onError            | action | Action to execute when initialization fails (optional)                                    |

### Example

Here's a basic example of how to initialize Stripe in your Ensemble app:

```yaml
View:
  header:
    title: Payment Setup
  body:
    Column:
      styles:
        padding: 24
        gap: 16
      children:
        - Text:
            text: Initialize Stripe
            styles:
              fontSize: 18
              fontWeight: bold
        - Button:
            label: Initialize Stripe
            onTap:
              initializeStripe:
                publishableKey: "pk_test_your_publishable_key_here"
                merchantIdentifier: "merchant.com.yourapp"
                onSuccess:
                  showToast:
                    message: "Stripe initialized successfully"
                onError:
                  showToast:
                    message: "Failed to initialize Stripe"
```

### Advanced Configuration

For Connect applications or when you need more control:

```yaml
initializeStripe:
  publishableKey: "pk_test_your_publishable_key_here"
  stripeAccountId: "acct_optional_account_id"
  merchantIdentifier: "merchant.com.yourapp"
  onSuccess:
    - showToast:
        message: "Stripe initialized successfully"
    - navigateScreen:
        name: PaymentScreen
  onError:
    showDialog:
      widget:
        Column:
          styles:
            gap: 16
            padding: 20
          children:
            - Text:
                text: Initialization Failed
                styles:
                  fontSize: 18
                  fontWeight: bold
            - Text:
                text: "Failed to initialize Stripe. Please check your configuration and try again."
            - Button:
                label: Try Again
                onTap: 
                  dismissDialog:
```

### Usage with Payment Flow

Initialize Stripe before showing the payment sheet:

```yaml
View:
  header:
    title: Checkout
  body:
    Column:
      styles:
        padding: 24
        gap: 16
      children:
        - Button:
            label: Pay Now
            onTap:
              initializeStripe:
                publishableKey: "pk_test_your_publishable_key_here"
                merchantIdentifier: "merchant.com.yourapp"
                onSuccess:
                  showPaymentSheet:
                    clientSecret: ${paymentIntentClientSecret}
                    configuration:
                      merchantDisplayName: "My Store"
                      style: "system"
                    onSuccess:
                      showToast:
                        message: "Payment successful!"
                    onError:
                      showToast:
                        message: "Payment failed"
                onError:
                  showToast:
                    message: "Failed to initialize payment system"
```

### Configuration

- **publishableKey**: Your Stripe publishable key (starts with `pk_test_` for test mode, `pk_live_` for live mode)
- **stripeAccountId**: Required only for Connect applications
- **merchantIdentifier**: Required for Apple Pay integration (format: `merchant.com.yourapp`)

### Error Handling

The `initializeStripe` action provides error handling through the `onError` callback. Common failure scenarios include:

- Invalid publishable key
- Network connectivity issues
- Invalid merchant identifier
- Stripe service unavailable

### Testing

For testing, use test mode keys:

- Use `pk_test_` keys for development
- Use `pk_live_` keys for production
- Test with various scenarios before going live 