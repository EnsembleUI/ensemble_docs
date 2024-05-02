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

This GraphQL API runs on Hasura's platform. To execute a mutation, we submit a POST request to the appropriate URL with the necessary headers.The request body contains information about the type of operation (mutation in this case), the specific method for performing the mutation (matching the server's method name), input values for the data being inserted, and the desired fields to be returned in the response. 

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

## Inserting multiple records at once

```
addFourProfiles:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    inputs:
      - profileId
      - profileName
      - profileIdTwo
      - profileNameTwo
      - profileIdThree
      - profileNameThree
      - profileIdFour
      - profileNameFour
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: ${secrets["hasura-admin-secret"]}
    body:
      query:  'mutation {insert_profiles(objects: [{name: "${profileName}", id: ${profileId}}, {id: ${profileIdTwo}, name: "${profileNameTwo}"}, {id: ${profileIdThree}, name: "${profileNameThree}"}, {id: ${profileIdFour}, name: "${profileNameFour}"}]) {returning {id}}}' 
```

In this specific context within Hasura GraphQL, our goal is to execute a batch insertion of multiple records into the database simultaneously. To achieve this, we supply the IDs and names of these records as input parameters, which are subsequently forwarded to the mutation query for processing and execution. Adhering to Hasura GraphQL conventions, each pairing of an ID and a name is treated as a distinct entity or object, forming the basis of the "objects" clause during the processing phase.

Furthermore, as part of this insertion process, we not only add the records to the database but also retrieve and return the IDs of each newly inserted record. This practice ensures that we have a comprehensive understanding of the outcome of the insertion operation, allowing us to track and manage the newly created records effectively.

## Deleting multiple records at once

```
deleteTwoProfiles:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    inputs:
      - firstID
      - secondID
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: ${secrets["hasura-admin-secret"]}
    body:
      query:  'mutation {delete_profiles(where: {id: {_in: [${firstID},${secondID}]}}){affected_rows}}'
```

In this scenario within Hasura GraphQL, our objective is to perform a batch deletion of multiple records from the database concurrently. We supply the IDs of the records slated for deletion as inputs to the API, which are subsequently forwarded to the mutation query for processing. Hasura GraphQL employs the where clause as a pivotal component in deletion operations, guiding the system to discern which records are slated for deletion based on predefined criteria. By leveraging the where clause in Hasura GraphQL mutations designed for deletion, you can effectively filter and target specific records for removal, enhancing precision and control over the deletion process.

Upon successful completion of the deletion operation, we furnish feedback regarding the impact of this action by providing information regarding the number of rows affected, offering a comprehensive view of the changes made to the database as a result of the deletion process.
