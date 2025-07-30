# Stripe Payment Example

This example demonstrates a complete Stripe payment flow in an Ensemble app.

## Complete Payment Flow

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
            text: Order Summary
            styles:
              fontSize: 20
              fontWeight: bold
        - Text:
            text: |
              Product: Premium Widget
              Quantity: 1
              Total: $29.99
            styles:
              fontSize: 16
        - Spacer:
            styles:
              size: 20
        - Button:
            label: Pay $29.99
            styles:
              backgroundColor: 0xff6772E5
              color: white
              padding: 16
            onTap:
              showPaymentSheet:
                clientSecret: ${paymentIntentClientSecret}
                configuration:
                  merchantDisplayName: "Widget Store"
                  style: "system"
                  primaryButtonLabel: "Pay $29.99"
                  preferredNetworks: ["visa", "mastercard", "amex"]
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
                  - showToast:
                      message: "Payment successful! Order confirmed."
                  - navigateScreen:
                      name: OrderConfirmation
                      inputs:
                        orderId: ${orderId}
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
                              text: "There was an issue processing your payment. Please try again or contact support."
                          - Button:
                              label: Try Again
                              onTap: 
                                dismissDialog:

# Order Confirmation Screen
OrderConfirmation:
  header:
    title: Order Confirmed
  body:
    Column:
      styles:
        padding: 24
        gap: 16
      children:
        - Icon:
            name: check-circle
            styles:
              fontSize: 64
              color: 0xff4CAF50
        - Text:
            text: Payment Successful!
            styles:
              fontSize: 24
              fontWeight: bold
        - Text:
            text: "Your order has been confirmed and payment processed successfully."
            styles:
              fontSize: 16
        - Text:
            text: "Order ID: ${orderId}"
            styles:
              fontSize: 14
              color: 0xff666666
        - Spacer:
            styles:
              size: 20
        - Button:
            label: Continue Shopping
            onTap:
              navigateScreen:
                name: Home
```

## Advanced Configuration Example

Here's an example with Apple Pay and Google Pay support:

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
      phone: ${userPhone}
      address:
        city: ${userCity}
        country: "US"
        line1: ${userAddress}
        line2: ${userAddressLine2}
        postalCode: ${userPostalCode}
        state: ${userState}
  onSuccess:
    showToast:
      message: "Payment successful!"
  onError:
    showToast:
      message: "Payment failed"
```

## App Configuration

Add your Stripe configuration to your app:

```yaml
App:
  name: My Store
  stripe:
    publishableKey: pk_test_your_publishable_key_here
```

## Testing

Use these test card numbers:

- **Success**: 4242 4242 4242 4242
- **Decline**: 4000 0000 0000 0002
- **Requires Authentication**: 4000 0025 0000 3155

## Key Points

1. **Security**: Never expose your secret key in client-side code
2. **Validation**: Always validate amounts before processing
3. **Error Handling**: Provide clear feedback for payment failures
4. **Testing**: Use test mode and test cards during development
5. **User Experience**: Show loading states and clear success/failure messages
6. **Configuration**: Use the configuration object to customize the payment experience 