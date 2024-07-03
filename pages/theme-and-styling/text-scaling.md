# Text scaling

iOS and Android users can use the accessibility features to change the weight, size, and darkness of text to make it easier to read on their devices.

Ensemble apps adhere to user selected preference by default. You can either disable text scaling, or set minimum and maximum factors you like to support in your app. 


## Disable text scaling

To disable text scaling globally across your app, go to your app's theme, and add the following:

```yaml
App:
  textScale:
    enabled: false
```

## Set max and min text scaling

You can continue supporting text scaling, but set max and min for the scaling factor:

## Disable text scaling

To disable text scaling globally across your app, go to your app's theme, and add the following:

```yaml
App:
  textScale:
    enabled: true  # this is the default behavior
    maxFactor: 1.2
    minFactor: 0.8
```

In the above example, text size will be increase by max 20%. E.g. if user selects a scaling factor of 1.5 in the OS settings, the text will no be increased more than 20%.
