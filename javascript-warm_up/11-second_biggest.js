#!/usr/bin/node
const numbers = process.argv.slice(2).map(Number).sort((a, b) => b - a);
console.log(numbers[1] ?? 0);
