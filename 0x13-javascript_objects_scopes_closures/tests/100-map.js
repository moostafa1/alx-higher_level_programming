const fs = require('fs');

// Read the array from the file
const { list } = require('./100-data');

// Compute a new array using map
const newList = list.map((value, index) => value * index);

// Print both arrays
console.log('Initial list:', list);
console.log('New list:', newList);
