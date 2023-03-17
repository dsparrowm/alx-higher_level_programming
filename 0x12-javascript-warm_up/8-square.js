#!/usr/bin/node
const arg = process.argv[2];
const num = Number(arg);
let i = 0;
let j = 0;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    let r = '';
    for (j = 0; j < num; j++) r += 'X';
    console.log(r);
  }
}
