#!/usr/bin/node
let argumentsList = process.argv.slice(2);
function secondBiggest(numbers) {
    if (numbers.length <= 1) {
        return 0;
    }

    let sortedNumbers = numbers.map(Number).sort((a, b) => b - a);
    return sortedNumbers[1];
}

console.log(secondBiggest(argumentsList));
