#!/usr/bin/node

const fs = require('node:fs');
const request = require('request');
const url = process.argv[2];
const file_path = process.argv[3];

request(url, function (error, response, body) {
  if (error) console.log(error);
  fs.writeFile(file_path, body, 'utf-8', (err) => {
    if (err) console.log(err);
  });
});
