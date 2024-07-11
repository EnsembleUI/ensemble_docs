# Object
Any property of a javascript object may be accessed using either the parenthesis `['propname']` or the dot `myObj.propname`. 

- It the property does not exist on the object, it will return null. Exception will *not* be thrown. 
- Let us know on our [Discord server](https://discord.gg/k4CJeuRc) if you need any of other capabilities
- or open a [ticket](https://github.com/EnsembleUI/ensemble/issues)

## Constructor

```js
var obj = {a: 1, b: 'abc'};//creates a new object with properties a and b
var obj2 = new Object(); //creates a new empty object
obj2['a'] = 1; //adds property a to the object
obj2['b'] = 'abc';
```

## Static Methods
### Object.keys(value)
See Object.keys in javascript. Returns an array of a given object's own enumerable property names.

Example - 
```js
var result = Object.keys({a: 1, b: 2, c: 3});
// result: ['a', 'b', 'c']
```
### Object.values(value)
See Object.values in javascript. Returns an array of a given object's own enumerable property values.
Example - 
```js
var result = Object.values({a: 1, b: 2, c: 3});
// result: [1, 2, 3]
```
### Object.entries(value)
See Object.entries in javascript. Returns an array of a given object's own enumerable property [key, value] pairs.
Example - 
```js
var result = Object.entries({a: 1, b: 2, c: 3});
// result: [['a', 1], ['b', 2], ['c', 3]]
```

### Object.getOwnPropertyNames(value)
See Object.getOwnPropertyNames(value) in javascript. Returns an array of all properties (including non-enumerable properties except for those which use Symbol) found directly in a given object.
Example - 
```js
var result = Object.getOwnPropertyNames({a: 1, b: 2, c: 3});
// result: ['a', 'b', 'c']
```

## Instance Methods
### keys()
Just like the Object.keys() method in javascript. Returns an array containing the keys (propery names) of an object. 

#### Returns
Returns an array containing the keys (propery names) of an object. 

Example - 
```js
var headers = {};
headers['abc'] = 'xyz';
headers['def'] = 123;
headers['ghi'] = '456';      
var keys = headers.keys();
keys.forEach(function(key) {
  console.log(key + ':' + headers[key]);
});
/* outputs
abc:xyz
def:123
ghi:456
*/
```
### values()
Just like the Object.values() method in javascript. Returns an array containing the values (propery values) of an object. 

#### Returns
Returns an array containing the values (propery values) of an object. 

Example - 
```js
var headers = {};
headers['abc'] = 'xyz';
headers['def'] = 123;
headers['ghi'] = '456';      
headers.values().forEach(function(val) {
  console.log(val);
});
/* outputs
xyz
123
456
*/
```
### entries()
Just like the Object.entries() method in javascript. Returns an array containing the entries  of an object where each entry is an object - {key:<key>,value:<value>} 

#### Returns
Returns an array containing the values (propery values) of an object. 

Example - 
```js
var headers = {};
headers['abc'] = 'xyz';
headers['def'] = 123;
headers['ghi'] = '456';      
headers.entries().forEach(function(entry) {
  console.log(entry.key + ':' + entry.value);
});  
/* outputs
abc:xyz
def:123
ghi:456
*/
```
### path(jsonPath,mapFunction)
The `path` method is a function that takes a JSON path as a string and an optional mapping function as arguments. The function traverses the object using the provided path and returns a list of the values found at that path.

The optional mapFunction argument is a function that transforms the values found at the JSON path. If a mapFunction is provided, it is applied to each value found at the path.

#### Parameters
jsonPath (String): The JSON path at which to look for values.</br>
mapFunction (Function, optional): A function to transform the values found at the path. This function is called with one argument: a list containing the current value. Pass `null` if not needed

#### Returns
A list of values found at the specified JSON path. If mapFunction is provided, the list will contain the transformed values.

Example - 
```js
var obj = {
  'name': 'John',
  'age': 30,
  'city': 'New York'
};

var result = obj.path('$.name', (val) => val[0].toUpperCase());
console.log(result); // Outputs: ["J"]
```
# Array
Arrays behave exactly as they would in regular javascript. You can access an item in the array with the index e.g. `myArray[0]`
- Let us know on our [Discord server](https://discord.gg/k4CJeuRc) if you need any of other capabilities
- or open a [ticket](https://github.com/EnsembleUI/ensemble/issues)

## Properties
### length
Returns the length of the array. Works exactly like the javascript arrays. 

**Example:**

```javascript
var numbers = [1, 4, 9];
console.log(roots.length); // 3
```

## Methods
### map

The `map()` method creates a new array populated with the results of calling a provided function on every element in the calling array.

**Parameters:**

- `callback`: Function that produces an element of the new array, taking two arguments:
  - `currentValue`: The current element being processed in the array.
  - `index`: The index of the current element being processed in the array.

**Return value:**

A new array with each element being the result of the callback function.

**Example:**

```javascript
var numbers = [1, 4, 9];
var squares = numbers.map(function(num, index) {
  return num * num;
});
console.log(squares); // [1, 16, 81]
```

### forEach

Executes a provided function once for each array element.

**Parameters:**

- `callback`: Function to execute on each element, taking two arguments:
  - `currentValue`: The current element being processed.
  - `index`: The index of the current element being processed.

**Return value:**

`undefined`.

**Example:**

```javascript
var numbers = [1, 2, 3];
numbers.forEach(function(num, index) {
  console.log('Number:', num, 'at index:', index);
});
```

### reduce

The `reduce()` method executes a reducer function on each element of the array, resulting in a single output value.

**Parameters:**

- `callback`: A function to execute on each element in the array (except for the first, if no initialValue is provided), taking four arguments:
  - `accumulator`: The accumulator accumulates the callback's return values.
  - `currentValue`: The current element being processed.
- `initialValue` (optional): A value to use as the first argument to the first call of the callback.

**Return value:**

The single value that results from the reduction.

**Example:**

```javascript
var numbers = [1, 2, 3, 4];
var sum = numbers.reduce(function(total, num) {
  return total + num;
}, 0);
console.log(sum); // 10
```

### indexOf

Returns the first index at which a given element can be found in the array, or -1 if it is not present.

**Parameters:**

- `searchElement`: The element to locate in the array.

**Return value:**

The first index of the element in the array; -1 if not found.

**Example:**

```javascript
var fruits = ['apple', 'banana', 'cantaloupe', 'blueberry'];
var index = fruits.indexOf('banana');
console.log(index); // 1
```

### join

Joins all elements of an array into a string.

**Parameters:**

- `separator` (optional): Specifies a string to separate each pair of adjacent elements of the array. The separator is converted to a string if necessary. If omitted, the array elements are separated with a comma.

**Return value:**

A string with all array elements joined.

**Example:**

```javascript
var elements = ['Fire', 'Air', 'Water'];
console.log(elements.join());      // "Fire,Air,Water"
console.log(elements.join(''));    // "FireAirWater"
console.log(elements.join('-'));   // "Fire-Air-Water"
```

### pop

Removes the last element from an array and returns that element. This method changes the length of the array.

**Parameters:**

None.

**Return value:**

The removed element from the array; `undefined` if the array is empty.

**Example:**

```javascript
var plants = ['broccoli', 'cauliflower', 'cabbage', 'kale', 'tomato'];
console.log(plants.pop()); // "tomato"
console.log(plants); // ["broccoli", "cauliflower", "cabbage", "kale"]
```

### push

Adds one or more elements to the end of an array and returns the new length of the array.

**Parameters:**

- `elementN`: The elements to add to the end of the array.

**Return value:**

The new length of the array.

**Example:**

```javascript
var animals = ['pigs', 'goats', 'sheep'];
var count = animals.push('cows');
console.log(count);  // 4
console.log(animals); // ["pigs", "goats", "sheep", "cows"]
```

### slice

The `slice()` method returns a shallow copy of a portion of an array into a new array object selected from `start` to `end` (end not included) where `start` and `end` represent the index of items in that array. The original array will not be modified.

**Parameters:**

- `start`: Zero-based index at which to start extraction.
- `end` (optional): Zero-based index before which to end extraction. The slice extracts up to but not including `end`.

**Return value:**

A new array containing the extracted elements.

**Example:**

```javascript
var fruits = ['Banana', 'Orange', 'Lemon', 'Apple', 'Mango'];
var citrus = fruits.slice(1, 3);
console.log(citrus); // ['Orange', 'Lemon']
```

### some

The `some()` method tests whether at least one element in the array passes the test implemented by the provided function. It returns a Boolean value.

**Parameters:**

- `callback`: Function to test for each element, taking one argument:
  - `currentValue`: The current element being processed in the array.

**Return value:**

`true` if the callback function returns a truthy value for any array element; otherwise, `false`.

**Example:**

```javascript
var array = [1, 2, 3, 4, 5];
var even = function(element) {
  return element % 2 === 0;
};
console.log(array.some(even)); // true
```

### every

The `every()` method tests whether all elements in the array pass the test implemented by the provided function. It returns a Boolean value.

**Parameters:**

- `callback`: Function to test for each element, taking one argument:
  - `currentValue`: The current element being processed in the array.

**Return value:**

`true` if the callback function returns a truthy value for every array element; otherwise, `false`.

**Example:**

```javascript
var isBelowThreshold = function(currentValue) {
  return currentValue < 40;
};
var array = [1, 30, 39, 29, 10, 13];
console.log(array.every(isBelowThreshold)); // true
```

### findIndex

The `findIndex()` method returns the index of the first element in the array that satisfies the provided testing function. Otherwise, it returns -1, indicating that no element passed the test.

**Parameters:**

- `callback`: Function to execute on each value in the array, taking one argument:
  - `currentValue`: The current element being processed.

**Return value:**

The index of the first element in the array that passes the test; otherwise, -1.

**Example:**

```javascript
var array = [5, 12, 8, 130, 44];
var isLargeNumber = function(element) {
  return element > 13;
};
console.log(array.findIndex(isLargeNumber)); // 3
```

### fill

The `fill()` method changes all elements in an array to a static value, from a start index (default zero) to an end index (default array.length). It returns the modified array.

**Parameters:**

- `value`: Value to fill the array with.
- `start` (optional): Start index, default 0.
- `end` (optional): End index, default array length.

**Return value:**

The modified array.

**Example:**

```javascript
var array = [1, 2, 3, 4];
console.log(array.fill(0, 2, 4)); // [1, 2, 0, 0]
console.log(array.fill(5, 1)); // [1, 5, 5, 5]
console.log(array.fill(6)); // [6, 6, 6, 6]
```

### shift

The `shift()` method removes the first element from an array and returns that removed element. This method changes the length of the array.

**Parameters:**

None.

**Return value:**

The removed element from the array; `null` if the array is empty.

**Example:**

```javascript
var myFish = ['angel', 'clown', 'mandarin', 'surgeon'];
console.log('Before:', JSON.stringify(myFish));
var shifted = myFish.shift();
console.log('After:', JSON.stringify(myFish));
console.log('Removed:', shifted);
// Before: ["angel", "clown", "mandarin", "surgeon"]
// After: ["clown", "mandarin", "surgeon"]
// Removed: angel
```

### unshift

The `unshift()` method adds one or more elements to the beginning of an array and returns the new length of the array.

**Parameters:**

- `...elements`: The elements to add to the front of the array.

**Return value:**

The new length of the array.

**Example:**

```javascript
var myArray = [1, 2, 3];
console.log(myArray.unshift(4, 5)); // 5
console.log(myArray); // [4, 5, 1, 2, 3]
```

### splice

The `splice()` method changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.

**Parameters:**

- `start`: The index at which to start changing the array.
- `deleteCount`: The number of elements in the array to remove from `start`.
- `...items`: The elements to add to the array, beginning from `start`.

**Return value:**

An array containing the deleted elements.

**Example:**

```javascript
var myFish = ['angel', 'clown', 'drum', 'mandarin', 'sturgeon'];
var removed = myFish.splice(3, 2);
console.log(myFish); // ["angel", "clown", "drum"]
console.log(removed); // ["mandarin", "sturgeon"]
```

### find

The `find()` method returns the value of the first element in the provided array that satisfies the provided testing function. If no values satisfy the testing function, `-1` is returned.

**Parameters:**

- `callback`: A function to execute on each value in the array until the function returns true, indicating that the satisfying element was found.

**Return value:**

The first element in the array that passes the test; `-1` if no elements pass the test.

**Example:**

```javascript
var array = [5, 12, 8, 130, 44];
var found = array.find(function(element) {
  return element > 10;
});
console.log(found); // 12
```

### includes

The `includes()` method determines whether an array includes a certain value among its entries, returning true or false as appropriate.

**Parameters:**

- `searchElement`: The element to search for.

**Return value:**

`true` if the array includes the element, and `false` otherwise.

**Example:**

```javascript
var array = [1, 2, 3];
console.log(array.includes(2)); // true
console.log(array.includes(4)); // false
```
