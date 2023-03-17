#!/usr/bin/node
const arg = process.argv[2];
const num = Number(arg);
let i = 0;
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
