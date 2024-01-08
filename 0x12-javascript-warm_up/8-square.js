#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  let i = 0; let j = 0;
  for (i; i < number; i++) {
    let row = '';
    for (j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
