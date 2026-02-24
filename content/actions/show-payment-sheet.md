# showPaymentSheet

The `showPaymentSheet` action displays Stripe's Payment Sheet, allowing users to securely enter payment information and complete transactions within your Ensemble app.

### Properties

| Property      | Type   | Description                                                                              |
| :------------ | :----- | :--------------------------------------------------------------------------------------- |
| clientSecret  | string | The Stripe PaymentIntent client secret that identifies the payment to be completed.      |
| configuration | object | Optional configuration for the payment sheet. [see properties](#propertiesconfiguration) |
| onSuccess     | action | Execute an Action when the payment is successfully completed.                            |
| onError       | action | Execute an Action when the payment fails or is cancelled.                                |

#### properties.configuration

| Property                   | Type   | Description                                                                  |
| :------------------------- | :----- | :--------------------------------------------------------------------------- |
| merchantDisplayName        | string | The merchant display name shown in the payment sheet.                        |
| preferredNetworks          | array  | Preferred card networks (e.g., ["visa", "mastercard"]).                      |
| customerId                 | string | Stripe customer ID (for returning customers).                                |
| customerEphemeralKeySecret | string | Ephemeral key for the customer.                                              |
| returnURL                  | string | Return URL after payment.                                                    |
| primaryButtonLabel         | string | Label for the primary button.                                                |
| applePay                   | object | Apple Pay configuration. [see properties](#propertiesapplepay)               |
| googlePay                  | object | Google Pay configuration. [see properties](#propertiesgooglepay)             |
| style                      | string | Payment sheet style: 'light', 'dark', or 'system'.                           |
| billingDetails             | object | Billing details for the payment. [see properties](#propertiesbillingdetails) |

#### properties.configuration.applePay

| Property            | Type   | Description                      |
| :------------------ | :----- | :------------------------------- |
| merchantCountryCode | string | Apple Pay merchant country code. |

#### properties.configuration.googlePay

| Property            | Type    | Description                             |
| :------------------ | :------ | :-------------------------------------- |
| merchantCountryCode | string  | Google Pay merchant country code.       |
| testEnv             | boolean | Enable test environment for Google Pay. |

#### properties.configuration.billingDetails

| Property | Type   | Description                                            |
| :------- | :----- | :----------------------------------------------------- |
| email    | string | Customer email address.                                |
| phone    | string | Customer phone number.                                 |
| name     | string | Customer name.                                         |
| address  | object | Customer address. [see properties](#propertiesaddress) |

#### properties.configuration.billingDetails.address

| Property   | Type   | Description      |
| :--------- | :----- | :--------------- |
| city       | string | City name.       |
| country    | string | Country code.    |
| line1      | string | Address line 1.  |
| line2      | string | Address line 2.  |
| postalCode | string | Postal/ZIP code. |
| state      | string | State/Province.  |

### Example

Here's a basic example of how to implement Stripe payments in your Ensemble app:

```yaml
View:
  header:
    title: Payment Example
  body:
    Column:
      styles:
        padding: 24
        gap: 16
      children:
        - Text:
            text: Complete your purchase
            styles:
              fontSize: 18
              fontWeight: bold
        - Text:
            text: Total: $29.99
            styles:
              fontSize: 16
        - Button:
            label: Pay with Stripe
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
                    message: "Payment failed or cancelled"
```

### Advanced Configuration Example

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

### Error Handling

The `showPaymentSheet` action provides error handling through the `onError` callback. Common failure scenarios include:

- User cancels the payment
- Invalid payment method
- Insufficient funds
- Network connectivity issues
- Invalid payment intent

### Testing

For testing, use Stripe's test mode with test card numbers:

- **Success**: 4242 4242 4242 4242
- **Decline**: 4000 0000 0000 0002
- **Requires Authentication**: 4000 0025 0000 3155

### Complete Example

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
              fontSize: 18
              fontWeight: bold
        - Text:
            text: |
              Product: Premium Widget
              Quantity: 1
              Total: $29.99
        - Button:
            label: Pay $29.99
            styles:
              backgroundColor: 0xff6772E5
              color: white
            onTap:
              showPaymentSheet:
                clientSecret: ${paymentIntentClientSecret}
                configuration:
                  merchantDisplayName: "Widget Store"
                  style: "system"
                  primaryButtonLabel: "Pay $29.99"
                  billingDetails:
                    email: ${userEmail}
                    name: ${userName}
                onSuccess:
                  navigateScreen:
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
```

This implementation provides a complete Stripe payment flow with proper error handling and user feedback. 