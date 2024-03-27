# Mocking API responses to develop and test your app
A key to developing an app quickly is to build the user interface independently of the back-end. This allows the team building the UI to be unblocked and move fast while also providing actual API payloads to the back-end team to build. Another advantage of this approach is that app could be built quickly with mockdata and be demo'd to customers for feedback. 
Ensemble provides a framework for mockng API responses that allow you to do that. You can mock all APIs or some and test with mockdata by simply setting a property. 

- To get hands-on experience with mock APIs, check the live example on [Ensemble Studio](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/UmaRcuduyIZmvOfk9BJu)
  
## 1. Setting/unsetting `useMockResponse`
Firstly, to use mock data in your app, it's important to update the global script of the screen, making sure that the API calls are directed to the mock data instead of the actual URL.
```javascript
Global: |-
  app.useMockResponse = true;
```
this sets the `useMockResponse` in the persistent storage but namespaces it by the appId i.e. <appid>_useMockResponse. 

For example:
RaRwIu1NasUOUsuJ0OuO_useMockResponse = true;
will be set in storage automatically for an app with id = 'RaRwIu1NasUOUsuJ0OuO'

you can check the value by just doing - 
```javascript
if ( app.useMockResponse ) {...}
```
By namespacing it, we can ensure that in ensemble live (or studio preview), one app's `useMockResponse` setting is not leaked into another app. 

In theory, you can bind to it as well as it is just another value in the storage. Remember to bind to `<appid>_userMockResponse` where <appid> should be replaced by your app's id without the <>. for example - RaRwIu1NasUOUsuJ0OuO_useMockResponse

You can obtain appId for your app anytime by doing - 
```javascript
appInfo.appId
```

## 2. Specify mock data on the API definitions
Mock data can be specified in 2 different ways, each offering flexibility and customization options to meet your development and testing needs.
### Inline on the API
Below is an example of an API definition, where `mockResponse` property is utilized to specify the inline mock data, which includes a `body` object containing mock data elements such as `title` and `list`. Additionally, response `headers` can be defined to simulate various scenarios. This approach is useful for quickly defining and modifying mock data directly within the API definition.
```yaml
  slowAPI:
    inputs:
      - uniqueId    
    mockResponse:
      #inline mock response
      body: 
        title: I am mock data
        list:
          - name: mock first
          - name: mock second
          - name: mock third
          - name: ${uniqueId}
      #can set response headers as well
      headers:
        - authToken: absbsbxssjjs
    url: https://openlibrary.org/search.json?q=the+lord+of+the+rings
    onResponse: |-
      console.log('slowAPI='+uniqueId);
      response.body.list.push({name: 'adding in onResponse - '+uniqueId});
```

### Return mock data from a function
```yaml
  mockDataFromFunction:
    inputs:
      - uniqueId    
    mockResponse: ${getMockResponse()}
    url: https://openlibrary.org/search.json?q=the+lord+of+the+rings
    onResponse: |-
      console.log('mockDataFromFunction='+uniqueId);
      response.body.list.push({name: 'mockDataFromFunction adding in onResponse - '+uniqueId});
```
The above API `mockDataFromFunction` endpoint utilizes a function to generate and return mock data dynamically. The `mockResponse` property references the `getMockResponse()` function, which is responsible for generating the mock data. The function could be defined either in the `Global` script block on the current screen or in a separate script and imported in. This method offers greater flexibility and allows for more complex mock data generation logic.
```javascript
var abc = 'var abc';
function getMockResponse() {
  return {
    body: {
      title: 'hello from mockResponse' + abc,
      list: [
        {name: 'mockResponse1'},
        {name: 'mockResponse2'},
        {name: 'mockResponse3'},
        {name: 'mockResponse4'},
        {name: 'mockResponse5'}
      ]
    }
  };
}
```
- Response from mock API can be used in a similar way as real API. To understand the utilization of API responses, detailed documentation is available [here](access-api-response).
### Mocking an error response
You can simply set `statusCode` property of the error to a specified status code such as "500" and `reasonPhrase` property to provide bit of description related to the error.
```yaml
  mockError:
    inputs:
      - uniqueId    
    mockResponse:
      body:
      statusCode: 500
      reasonPhrase: mock bad request

    url: https://openlibrary.org/search.json?q=the+lord+of+the+rings
    onResponse: |-
      console.log('mockDataFromFunction='+uniqueId);
      response.body.list.push({name: 'mockDataFromFunction adding in onResponse - '+uniqueId});
    onError:
      showToast:
        message: error occurred ${response.statusCode} ${response.reasonPhrase}
        options:
          duration: 5
```
