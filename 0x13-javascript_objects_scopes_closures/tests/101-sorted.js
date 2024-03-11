// Import the dictionary from the file
const { dict } = require('./101-data');

// Initialize an empty dictionary to store user ids by occurrence
const userDict = {};

// Iterate over the original dictionary
for (const userId in dict) {
    const occurrences = dict[userId];
    // If the number of occurrences is not a key in the new dictionary, initialize it with an empty array
    if (!userDict[occurrences]) {
        userDict[occurrences] = [];
    }
    // Add the user id to the list of user ids for the current number of occurrences
    userDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(userDict);
