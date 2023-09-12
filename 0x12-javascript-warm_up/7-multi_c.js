#!/usr/bin/node

const argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argument; i++) {
    console.log('C is fun');
  }
}
