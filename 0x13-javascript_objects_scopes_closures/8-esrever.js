#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    const val = list[i];
    rev.push(val);
  }
  return rev;
};
