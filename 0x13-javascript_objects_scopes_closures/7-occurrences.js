#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Use the reduce function to count occurrences
  return list.reduce(function (count, element) {
    // Check if the current element is equal to the searchElement
    if (element === searchElement) {
      // Increment the count if a match is found
      count++;
    }
    return count;
  }, 0); // Initialize count to 0
};
