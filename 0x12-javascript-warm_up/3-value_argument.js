#!/usr/bin/node

let count = 0;

for (const arg in process.argv) {
  count++;
}

if (count <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
