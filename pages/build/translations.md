# Translations

Ensemble supports localization of app content so that your app users can view the app in their preferred language.

## Set up languages

In Ensemble Studio, navigate to your app and select Translations from the left menu. Add new language to start with.

![add language](/images/translations/add-language.png)

## Add content

Language content is created in YAML. Add key/value pairs for each text.

![add language](/images/translations/add-language-content.png)

#### Organize the content

To make it easier to find and update the text, you can create a hierarchy within language files. For instance, you can have common text under `common` and text related to login screen under `login`

```yaml
common:
    submit: Submit
    error: Something went wrong. Try again.

login:
    login_button: Sign in
    login_error: Incorrect username or password. Please try again.

```


## Reference the translation

In any screen or widget, reference the translations. E.g. for a button, assign the reference to the `label` property.

When refrencing translations, prepend `r@` before the key assigned to the text:


```yaml
- Button:
    label: r@login.login_button
```


## Test in Preview

Use the 🌎 icon on top of the preview to select a language. The preview updates and shows the UI in the selected language.

![add language](/images/translations/test-language.png)