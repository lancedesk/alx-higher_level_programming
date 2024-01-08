#!/usr/bin/node
const numbers = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
