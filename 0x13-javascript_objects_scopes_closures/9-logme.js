#!/usr/bin/node

exports.logMe = (function () {
  let count = 0;

  return function logMe (item) {
    console.log(count, ':', item);
    count++;
  };
})();
