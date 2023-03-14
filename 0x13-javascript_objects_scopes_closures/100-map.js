#!/usr/bin/node
const list = require('./100-data.js').list;
let count = 0;
const doubled = list.map((n) => n * count++);
console.log(list);
console.log(doubled);
