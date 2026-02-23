
# Script with JavaScript

Scripts can provide a powerful way to enhance your app's functionality and customize its behavior beyond what can be achieved with declarative configurations alone.

## When to Use Scripts

Global Scripts are ideal for situations where you need:

- **Reusable Logic:** Define functions or variables that can be used across multiple screens or widgets in your app. For example, a function to format dates or calculate totals could be placed in a Global Script for easy access.
- **Data Storage:** Store pre-defined data like user details, color palettes, or API endpoints in a Global Script for consistent use throughout your app. This simplifies updates and avoids code duplication.
- **Custom Logic:** Scripts allow you to Implement complex logic, manipulate data, perform calculations, and interact with external services and APIs.

## Create a Script
In Ensemble Studio, navigate to your app and select `Scripts` from the left menu. Click the button `Create new script` present at the top right corner of the studio.

![add language](/images/scripts/create-script.png)

Now open the script file and you can use standard JavaScript syntax to define variables and functions and then save the file.

![add language](/images/scripts/Add-script-content.png)

> Ensemble currently supports JavaScript syntax up to ES5.

## Import the script
In the YAML code for your screen or widget, use the `Import` section to reference the script file. For example:
```yaml
Import:
  - Common
```
## Use the Script
The code example shows how to access variables and functions defined in the Global Script from your screen's YAML code.
```yaml
Import:
  - Common

View:
  styles:
    backgroundColor: ${colors.snowGrey} # Here we have used color imported from the Common Script.
  header:
    title: Global scripts
  body:
    Column:
      styles:
        padding: 24
        gap: 8
      children:
        - Button:
          label: Run function from Common
          styles:
            backgroundColor: ${colors.red} # Here we have used color imported from the Common Script.
          onTap:
            executeCode:
              body: |
                // Import the getUserFromScript function from the Common script
                var thisUser = getUserFromScript();

                // Now assigning text to the Fields
                nameText.text = "Name: " + thisUser.name;
                companyText.text = "Company: " + thisUser.company;

        - Column:
          children:
            - Text:
              text: User Details
              styles:
                textStyle:
                  color: ${colors.green}
                  fontSize: 21
                  fontWeight: bold
                  isItalic: true
            - Text:           # Display user's name
              id: nameText
            - Text:           #  Display user's company
              id: companyText
```
**Explanation:**
1. Accessing Variables from the Script:
   + The `backgroundColor` of the view is set using `${colors.snowGrey}`. This references the snowGrey variable defined in the colors object within the Common Script.
Similarly, the `backgroundColor` of the button is set using `${colors.red}`.
2. Accessing Functions from the Script:
   + Clicking the button triggers the `onTap` event, which calls the `executeCode` block. Inside the block, the `getUserFromScript()` function (defined in Common Script) is called to retrieve user information.
   + The returned data is stored in the `thisUser` variable. To display the user's name, the code constructs a string by combining `"Name: "` with the `name` property of the `thisUser` object.
