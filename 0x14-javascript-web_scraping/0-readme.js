#!/usr/bin/node
const fs = require('fs');

const file_path = process.argv[2];
fs.readFile(file_path, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
