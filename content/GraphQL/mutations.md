# GraphQL Mutations

In the realm of GraphQL, mutations serve as pivotal tools utilized to enact alterations to data residing on the server. These alterations encompass a spectrum of actions ranging from the creation of new records to updating existing ones or even removing records altogether. Unlike queries, which are primarily geared towards retrieving data, mutations are tailored for operations that induce modifications in the fundamental data structure.

The structure of mutations bears resemblance to queries, maintaining a familiar syntax and format. However, their distinct purpose lies in effecting changes within the data rather than solely fetching it. To define a mutation in GraphQL, one employs the 'mutation' keyword, followed by the operation's designated name, and any requisite input variables necessary for the operation to execute seamlessly. This systematic approach not only ensures clarity in defining mutation operations but also provides a robust framework for implementing data modifications in a controlled and organized manner within the GraphQL ecosystem. 

In Hasura GraphQL, when we want to perform a mutation, we send a POST request to the correct URL with the required headers. Inside the request body, we include details such as the type of operation (in this case, a mutation), the exact method for carrying out the mutation (which matches the server's method name), the input values for the data we're adding or modifying, and the specific fields we want to receive in the response.

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


In the scenario described within Hasura GraphQL, our objective is to initiate a mutation aimed at creating a new record within the database schema. To achieve this, the method specified in the request body corresponds precisely to the method name expected by the Hasura GraphQL server.

Within the request body, we provide essential inputs necessary for creating the new record. These inputs include the ID, set as 24, and the name, designated as "chad," serving as the initial data values for the newly created record. By incorporating these inputs into the mutation operation, we effectively signal to the Hasura GraphQL server our intent to generate a new record with specific attributes, fostering a structured and controlled approach to data creation within the GraphQL ecosystem.

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


In the context of Hasura GraphQL, the example illustrates a successful deletion operation targeting a record identified by the ID 12. This deletion was accomplished by specifying the ID as an input value to the appropriate method, effectively instructing the system to remove the corresponding record from the database.

Upon completion of the deletion process, the response from the system includes not only confirmation of the deletion but also additional information requested in the response. Specifically, the response contains the ID and name of the deleted record, aligning with the fields we specified to be included in the response. This inclusion of requested fields in the response ensures that the outcome of the deletion operation is transparent and comprehensive, providing us with the necessary details regarding the deleted record for further analysis or tracking purposes.

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


In the provided example within the context of Hasura GraphQL, we engage in a process that involves supplying two distinct input values to a specified method. The first input pertains to 'pk_columns', which denotes the primary key columns within a database schema. These primary keys hold the critical function of uniquely identifying each row within a table, ensuring precise record identification and management. In our scenario, where the 'id' field serves as the primary key for our records, we pass this field as the value for 'pk_columns'. This action effectively signifies the specific record within the database that we intend to update, streamlining the targeting process for our mutation operation.

Moving forward, the second input value is designated for '_set', which embodies a unique input object commonly utilized in mutations to facilitate the modification of specific fields within an object. Within this 'set' input, we strategically include the fields that we wish to update within the targeted record. By delineating the fields to be updated within this structured input, we ensure precision and clarity in our mutation operation, focusing solely on the specified fields without affecting other aspects of the record. This approach enhances the efficiency and effectiveness of our data modification process, aligning with best practices in database management and GraphQL mutation conventions.

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
