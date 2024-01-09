#!/usr/bin/node
const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

try {
  const contentA = fs.readFileSync(fileA, 'utf-8');
  const contentB = fs.readFileSync(fileB, 'utf-8');
  const concatenatedContent = `${contentA}${contentB}`;

  fs.writeFileSync(fileC, concatenatedContent);
} catch (err) {
  console.error(`Error: ${err.message}`);
  process.exit(1);
}
