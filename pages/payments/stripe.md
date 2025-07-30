# Stripe Integration

Ensemble provides seamless integration with Stripe for processing payments in your mobile apps. The Stripe module allows you to accept credit card payments, digital wallets, and other payment methods through Stripe's secure Payment Sheet.

## Overview

The Stripe integration in Ensemble consists of:

- **Payment Sheet**: A pre-built UI component for collecting payment information
- **Payment Intent Management**: Client-side payment intent handling
- **Error Handling**: Comprehensive error handling for payment failures
- **Security**: PCI-compliant payment processing

## Configuration

### Build Configuration

1. Go to Build & Deploy > Build Settings
2. Enable Stripe Module
3. Add your Stripe publishable key in Stripe Attributes. You also need to add Apple Pay Merchant Identifier for Apple Pay.

## Basic Implementation

### Simple Payment Flow

Here's a basic example of implementing Stripe payments:

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
        - Text:
            text: Order Total: $29.99
            styles:
              fontSize: 18
              fontWeight: bold
        - Button:
            label: Pay Now
            onTap:
              showPaymentSheet:
                clientSecret: ${paymentIntentClientSecret}
                configuration:
                  merchantDisplayName: "My Store"
                  style: "system"
                  primaryButtonLabel: "Pay $29.99"
                onSuccess:
                  showToast:
                    message: "Payment successful!"
                onError:
                  showToast:
                    message: "Payment failed"
```

### Advanced Configuration

You can customize the payment sheet with various configuration options:

```yaml
showPaymentSheet:
  clientSecret: ${paymentIntentClientSecret}
  configuration:
    merchantDisplayName: "Premium Store"
    preferredNetworks: ["visa", "mastercard", "amex"]
    customerId: ${stripeCustomerId}
    customerEphemeralKeySecret: ${ephemeralKeySecret}
    returnURL: "myapp://payment-return"
    primaryButtonLabel: "Complete Payment"
    style: "dark"
    applePay:
      merchantCountryCode: "US"
    googlePay:
      merchantCountryCode: "US"
      testEnv: true
    billingDetails:
      email: ${userEmail}
      name: ${userName}
      address:
        city: ${userCity}
        country: "US"
        line1: ${userAddress}
        postalCode: ${userPostalCode}
        state: ${userState}
  onSuccess:
    showToast:
      message: "Payment successful!"
  onError:
    showToast:
      message: "Payment failed"
```

### Handle Payment Success

When payment is successful, you can navigate to a confirmation screen:

```yaml
onSuccess:
  navigateScreen:
    name: OrderConfirmation
    inputs:
      orderId: ${orderId}
```

### Handle Payment Failure

Implement proper error handling for failed payments:

```yaml
onError:
  showDialog:
    widget:
      Column:
        styles:
          gap: 16
          padding: 20
        children:
          - Text:
              text: Payment Failed
              styles:
                fontSize: 18
                fontWeight: bold
          - Text:
              text: "There was an issue processing your payment. Please try again."
          - Button:
              label: Try Again
              onTap: 
                dismissDialog:
```

## Configuration Options

### Payment Sheet Style

You can customize the appearance of the payment sheet:

- `"light"`: Light theme
- `"dark"`: Dark theme  
- `"system"`: Follows system theme (default)

### Digital Wallets

Configure Apple Pay and Google Pay:

```yaml
configuration:
  applePay:
    merchantCountryCode: "US"
  googlePay:
    merchantCountryCode: "US"
    testEnv: true  # Set to false for production
```

### Billing Details

Pre-fill customer information:

```yaml
configuration:
  billingDetails:
    email: ${userEmail}
    name: ${userName}
    phone: ${userPhone}
    address:
      city: ${userCity}
      country: "US"
      line1: ${userAddress}
      postalCode: ${userPostalCode}
      state: ${userState}
```

## Security Best Practices

### 1. Secure Payment Intent Handling

- Ensure payment intents are created securely
- Validate payment amounts before processing
- Use HTTPS for all API calls
- Implement proper error handling

### 2. Configuration Security

- Use environment variables for sensitive data
- Never expose secret keys in client-side code
- Use test account for development

## Testing

### Test Card Numbers

Use these test card numbers for development:

| Card Number | Description |
|-------------|-------------|
| 4242 4242 4242 4242 | Successful payment |
| 4000 0000 0000 0002 | Declined payment |
| 4000 0025 0000 3155 | Requires authentication |
| 4000 0000 0000 9995 | Insufficient funds |

### Test Mode

Always use test mode during development:

- Use `pk_test_` keys for publishable keys
- Test with various scenarios before going live

## Production Checklist

Before going live with Stripe payments:

- [ ] Switch to live API keys
- [ ] Configure fraud detection
- [ ] Test with real payment methods
- [ ] Implement proper error handling
- [ ] Set up monitoring and logging
- [ ] Configure customer support processes
- [ ] Review compliance requirements

## Related Actions

- [showPaymentSheet](../actions/show-payment-sheet.md) - Display the Stripe Payment Sheet 