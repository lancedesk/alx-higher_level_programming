#!/usr/bin/node

const request = require('request');

function print_characters(characters, index) {
    request(characters[index], function (error, response, body) {
        if (error) {
            console.error(error);
        } else {
            const character_info = JSON.parse(body);
            console.log(character_info.name);
            
            if (index + 1 < characters.length) {
                print_characters(characters, index + 1);
            }
        }
    });
}

const file_path = process.argv[2]
const url = 'https://swapi-api.alx-tools.com/api/films/' + file_path;

request(url, function (error, response, body) {
    if (error) {
        console.error(error);
    } else {
        const data = JSON.parse(body);
        
        print_characters(data.characters, 0);
    }
});
