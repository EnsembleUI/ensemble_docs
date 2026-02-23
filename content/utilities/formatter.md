# Formatter

Ensemble provide convenience formatter utilities for handling date/time and common tasks.

Access these formatters with prefix `ensemble.formatter.*`.

### prettyDate()
Accepts an ISO date-time string and output the most common user-friendly format based on the user's detected locale.
- `ISO string`: the string to convert to a user-friendly date string. 

```yaml
Text:
  # output "Dec 2, 2022" or "2 Dec 2022" depending on detected locale.
  text: ${ensemble.formatter.prettyDate("2022-12-02T14:20:05-0700")}

Button:
  onTap: |-
    // same output in Javascript.
    console.log(ensemble.formatter.prettyDate("2022-12-02"));
```
For a more complete Date operations, see [Date](../javascript-reference/Date.md)

### prettyTime()
Accepts an ISO date-time string and outputs the most common user-friendly time format based on the user's detected locale.
- ISO string: The string to convert to a user-friendly time string.

```yaml
Text:
  # output "2:20 PM" or "14:20" depending on detected locale.
  text: ${ensemble.formatter.prettyTime("2022-12-02T14:20:05-0700")}
```

### prettyDateTime()
Accepts an ISO date-time string and outputs the most common user-friendly date and time format based on the user's detected locale.
- ISO string: The string to convert to a user-friendly date and time string.

```yaml
Text:
  # output "Dec 2, 2022, 2:20 PM" or "2 Dec 2022, 14:20" depending on detected locale.
  text: ${ensemble.formatter.prettyDateTime("2022-12-02T14:20:05-0700")}
```

### customDateTime()
Accepts an ISO date-time string and a pattern that, then outputs the date and time formatted according to the provided pattern (user locale will be ignored).
- ISO string: The string to convert to a formatted date and time string.
- Pattern: The pattern to use for formatting the date and time string.

```yaml
Text:
  # output 2022-12-02 14:20" for all locales
  text: ${ensemble.formatter.customDateTime('2022-12-02T14:20:05-0700', 'yyyy-MM-dd HH:mm')}
```
