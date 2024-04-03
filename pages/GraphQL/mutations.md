# GraphQL Mutations

GraphQL mutations are used to modify data on the server, such as creating, updating, or deleting records. They are similar to queries in
structure but are used for operations that cause changes in the underlying data rather than just fetching data. In GraphQL, mutations are 
defined using the mutation keyword followed by the operation name and any required input variables. 

## Creating a new record

Here is an example of a GraphQL mutation using Ensemble as the client to add a new entry to the database:

```
API:
  getData:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: eS2vHbx9568eJsXCTzrc57Mc2QfGNn387i4pNOAqVP7cE4nTOLTJYAiduo0a72GK
    body:
      query:  'mutation {insert_profiles_one(object: {name: "chad", id: 24}) {id name}}'
```

This GraphQL API runs on Hasura's platform. To execute a mutation, we submit a POST request to the appropriate URL with the necessary headers.
The request body contains information about the type of operation (mutation in this case), the specific method for performing the mutation 
(matching the server's method name), input values for the data being inserted, and the desired fields to be returned in the response. 

## Deleting a record

Deleting a record using GraphQL mutations involves specifying the record you want to delete and providing the necessary input values. 

```
API:
  getData:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: eS2vHbx9568eJsXCTzrc57Mc2QfGNn387i4pNOAqVP7cE4nTOLTJYAiduo0a72GK
    body:
      query:  'mutation {delete_profiles_by_pk(id: 12){id name}}'
```

In the provided example, we successfully deleted the record with the id 12 by providing it as an input value to the relevant method. The 
response contains the id and name of the deleted record, which are the fields we requested to receive in the response.

## Updating a record

Updating a record using GraphQL mutations involves specifying the data you want to update and providing the necessary input values. 

```
API:
  getData:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: eS2vHbx9568eJsXCTzrc57Mc2QfGNn387i4pNOAqVP7cE4nTOLTJYAiduo0a72GK
    body:
      query:  'mutation {update_profiles_by_pk(pk_columns: {id: 25}, _set: {id: 38, name: "pam"}){id name}}'
```

In the example above, we supply two input values to the specified method. The first input is for 'pk_columns', which indicates the primary 
key columns in a database schema. Primary keys uniquely identify each row in a table. Since our id serves as the primary key, we passed 
that as the value. This value signifies the record in the database that we intend to update. The second input is for _set, which represents
a unique input object utilized in mutations to modify particular fields of an object. Within this input, we include the fields that we wish
to update in the record.


