#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        if (c) {
          row += c;
        } else {
          row += 'X';
        }
      }
      console.log(row);
    }
  }
};
