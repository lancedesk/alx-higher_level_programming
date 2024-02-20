#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file_path = process.argv[3];

request.get(url, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        fs.writeFile(file_path, body, 'utf-8', (err) => {
            if (err) {
                console.error(err);
            } else {
                console.log(`Contents of ${url} saved to ${file_path}`);
            }
        });
    }
});
