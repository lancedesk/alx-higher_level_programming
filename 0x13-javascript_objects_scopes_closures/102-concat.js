#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const [, , fileA, fileB, fileC] = process.argv;

try {
  const contentA = fs.readFileSync(fileA, 'utf-8');
  const contentB = fs.readFileSync(fileB, 'utf-8');
  const concatenatedContent = `${contentA}${contentB}`;

  fs.writeFileSync(fileC, concatenatedContent);

  console.log(`Files ${fileA} and ${fileB} successfully concatenated to ${fileC}`);
} catch (err) {
  console.error(`Error: ${err.message}`);
  process.exit(1);
}
