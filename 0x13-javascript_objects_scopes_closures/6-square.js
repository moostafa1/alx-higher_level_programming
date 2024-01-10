#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          row += 'X';
        } else {
          row += c;
        }
      }
      console.log(row);
    }
  }
};
