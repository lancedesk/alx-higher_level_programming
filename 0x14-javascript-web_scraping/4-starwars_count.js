#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.error(error);
        return;
    }

    const data = JSON.parse(body);
    let total_count = 0;

    for (const film of data.results) {
        const characters_with_wedge = film.characters.filter(character => character.includes('18'));
        total_count += characters_with_wedge.length;
    }
    console.log(total_count);
});
