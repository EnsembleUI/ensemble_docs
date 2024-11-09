# Exception Handling in Javascript

Ensemble supports try/catch/finally in ES5 and the throw clause as well. In JavaScript ES5, the try/catch/finally structure, along with the throw statement, provides robust error-handling capabilities. These constructs allow developers to handle runtime errors gracefully, ensuring that code can respond to unexpected issues without crashing. 

The try block contains code that might throw an error, and if an error occurs, control immediately moves to the catch block, where the error can be handled. 

The finally block, which is optional, executes regardless of whether an error was caught, making it useful for cleanup tasks (like closing connections or freeing up resources). 

The throw statement allows you to generate custom errors by “throwing” an error that can be caught by catch. This is particularly useful for input validation and other scenarios where specific conditions need to be enforced.

In the following example, the function `divide` is throwing an error that is then caught in the catch clause and a toast message is shown.

```yaml
View:
  styles:
    useSafeArea: true

  # Optional - set the header for the screen
  header:
    titleText: Home

  # Specify the body of the screen
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
        - Text:
            text: Hi there!
        - Button:
            label: Checkout Ensemble Kitchen Sink
            onTap:
              executeCode:
                body: |-
                  try {
                    console.log(divide(10, 0)); // Will throw an error
                  } catch (error) {
                    console.log("Caught an error: " + error.message);
                    var payload = {
                      message: error.message,
                      options: {
                        type: 'error',
                        duration: 3,
                        alignment: 'bottomRight'
                      }
                    };
                    ensemble.showToast(payload);
                  } finally {
                    console.log("Execution completed.");
                  }

Global: |-
  // Javascript code
  function divide(a, b) {
    if (b === 0) {
        throw new Error("Division by zero is not allowed"); // Custom error, you can just throw a string as well i.e. throw "Division by zero is not allowed";
    }
    return a / b;
  } 

```

