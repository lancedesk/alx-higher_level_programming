#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const file_path = process.argv[2];

fs.readFile(file_path, 'utf-8', (err, data) => {
	if (err) {
		console.log(err);
		return;
	}
	console.log(data);
});
