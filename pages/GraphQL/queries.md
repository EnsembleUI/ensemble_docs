# GraphQL Queries


In the realm of GraphQL, queries play a pivotal role as they facilitate client requests aimed at retrieving precise and tailored data from a GraphQL API. These queries empower clients to articulate their data requirements by specifying the exact fields and data structure they seek in the response. This granularity in data fetching not only enhances efficiency but also ensures that clients receive only the data they need, eliminating any unnecessary data overhead.

The structure of a GraphQL query is meticulously designed to encapsulate these data retrieval specifications. It commences with the 'query' keyword, signaling the initiation of a data-fetching operation. Following this keyword, clients articulate their data needs by specifying the fields, nested structures, and relationships they wish to include in the response. This structured approach to query construction allows for a clear and concise expression of data requirements, fostering a streamlined and optimized data-fetching process within the GraphQL ecosystem.

## Field Selection

GraphQL queries allow clients to specify exactly which fields they want to retrieve. This is in contrast to REST APIs where the server
determines the structure of the response.

Here is an instance of utilizing Ensemble for dispatching a GraphQL query:

```
API:
  getData:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: eS2vHbx9568eJsXCTzrc57Mc2QfGNn387i4pNOAqVP7cE4nTOLTJYAiduo0a72GK
    body:
      query: '{profiles {id name}}'
```


This GraphQL API operates on Hasura's platform. To submit a query, we send a POST request to the correct URL, along with the required 
headers. The request payload includes the data and its fields to be retrieved from the API. 

Let's say that within each profile object, there is also a posts object that includes the id and title fields. We have the option to include
them in our query as well.

```
API:
  getData:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: eS2vHbx9568eJsXCTzrc57Mc2QfGNn387i4pNOAqVP7cE4nTOLTJYAiduo0a72GK
    body:
      query: '{profiles {id name posts{id title}}}'
```
The response will include the data object, which in turn will have each profile object containing their id, name, and posts fields. 
Additionally, it will provide the id and title associated with each posts object.

## Aliases

Aliases in GraphQL are used to rename the fields in the response to a different name than the one defined in the schema. They are 
particularly useful when there is a naming conflict or when the client wants to use a more descriptive or convenient name for a field 
in the response.

In the example above, both the profile and posts have an id field. We can use aliases to differentiate them in the response. 

```
API:
  getData:
    url: https://regular-satyr-34.hasura.app/v1/graphql
    method: POST
    headers:
      Content-Type: application/json
      x-hasura-admin-secret: eS2vHbx9568eJsXCTzrc57Mc2QfGNn387i4pNOAqVP7cE4nTOLTJYAiduo0a72GK
    body:
      query: 'query myQuery{profiles {profileID:id name posts{postID:id title}}}'
```
The response will consist of a data object containing multiple profile objects, each of which will include a post object. The id for each 
profile will be labeled as profileID, and the id for the posts will be labeled as postID.
