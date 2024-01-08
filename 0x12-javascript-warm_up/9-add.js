#!/usr/bin/node
const number = parseInt(process.argv[2]);
const number1 = parseInt(process.argv[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}

add(number, number1);
