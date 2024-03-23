# Chaining APIs

Chaining APIs, i.e. making sequential API calls, is a practice in app development when you need to retrieve and use data from multiple APIs in a specific order. Chaining APIs allows you to build more complex workflows and gather the necessary information for your application.

```yaml
onLoad:
  invokeAPI:
    name: getuser
    onResponse:
      invokeAPI:
        name: getcurrentUserContacts
        inputs:
            userId: ${getUser.body.id}
```

**Sequential API Calls:**
The onResponse event for each API call specifies the next API call to be made after the current one is successfully completed.
For example, after the initial API call named "getuser", the onResponse event triggers the "getcurrentUserContacts" API call.
