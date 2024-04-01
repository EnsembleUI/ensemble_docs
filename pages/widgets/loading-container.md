# LoadingContainer widget

The LoadingContainer widget is designed to simplify the process of displaying a loading indicator while content is being fetched or processed. It provides a convenient abstraction layer for managing loading states in your app, allowing developers to easily toggle between the loading state and the state where content is available.

[Test in Kitchen Sink](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/3wNZSfVkdi56zmTtFeBT)

## Key Concepts

- **loadingWidget**: Specify a widget to display while loading content. This can point to a custom widget, such as a column of shapes to represent what the loaded content might look like.
- **widget**: This is the widget to display when content is available.
- **isLoading**: This is typically an expression that returns true or false. When true, the `loadingWidget` is displayed. When false, the `widget` will display.


## Example

Typically LoadingContainer is used in combination with an API call so that you can show a loading state while waiting for the API to respond.

```yaml
View:

  header:
    title: "API: Handle loading state"

  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
        - Button:
            label: Invoke API
            onTap:
              executeActionGroup:
                actions:
                  - invokeAPI:
                      name: getData
                  - executeCode:
                      body: |
                        content.visible = truel

        - LoadingContainer:
            id: content
            visible: false
            isLoading: ${ getData.isLoading }
            widget:
              Text:
                text: Data is ready
            loadingWidget:
              Shape:
                type: rectangle
                styles:
                  backgroundColor: grey
                  width: ${ device.width }
                  borderRadius: 8
                  height: 100
            useShimmer: true

API:
  getData:
    method: GET
    url: https://httpbin.org/delay/10

```

## Reference
#### Properties

| Property      | Type                                   | Description                                             |
| :------------ |:---------------------------------------|:--------------------------------------------------------|
| isLoading     | bool | Whether to display a loading widget. The default will be empty (without shimmer) or a default loading shimmer, unless a loadingWidget is specified. |
| useShimmer    | bool | A shining animation to designate that the content is loading. The animation can be over a defaults shimmer or the loadingWidget if specified. |
| loadingWidget | object | The widget to render during the loading state (i.e. while isLoading is true).
| widget        | object | The widget to render as the content of this container. |



