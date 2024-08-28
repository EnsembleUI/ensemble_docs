# executeActionGroup
Executing a group of Actions, either in parallel (default) or sequentially with each waiting for the other to complete before executing.

## Usage
- The most common use case for this is calling APIs in parallel using the `invokeAPI` action. Since APIs are asynchronous, multiple APIs will be triggered one after the other in parallel. The parallism is governed by the underlying operating system.
- Use `executeInOrder: true` when certain actions depend on the previous action to complete before executing. An example is closing the current dialog before opening up the new one. Dialog lifecycles are asynchronous, so calling close followed immediately by open will not work as expected. Using `executeInOrder: true` will ensure that the close action completes before the open action is executed.

## Caveats
- Note that while `executeCode` action can execute asynchronous code, it will not wait and will immediately return. This means that even if it is used inside `executeActionGroup` with `executeInOrder: true`, the next action will be executed immediately after the `executeCode` action is called. 

| Property       | Type     | Description                                                                          |
|:---------------|:---------|:-------------------------------------------------------------------------------------|
| executeInOrder | boolean  | If true, the actions will be executed in order, one after the other. (default false) |
| actions        | Action[] | The list of Actions to be executed                                                   |


See [Kitchen Sink Example](https://studio.ensembleui.com/app/e24402cb-75e2-404c-866c-29e6c3dd7992/screen/VJQun4rJ91mATTBopsNy#)

## Example
```yaml
          - Button:
              label: Round
              onTap:
                executeActionGroup:
                  actions:
                    - invokeAPI:
                        name: callDelayedAPI
                        inputs:
                          num: 1
                    - showToast:
                        message: second action - 2
                        options:
                          duration: 4
                    - executeCode:
                        body: |- 
                          console.log('executed code - 2');
                    - invokeAPI:
                        name: callDelayedAPI
                        inputs:
                          num: 3
                        onResponse: |-
                          console.log('inline onResponse - 3');
                    - invokeAPI:
                        name: callDelayedAPI
                        inputs:
                          num: 4
                    - showToast:
                        message: number 5
                        options:
                          duration: 3
                    - executeCode:
                        body: |- 
                          console.log('executed code - 5');
```
