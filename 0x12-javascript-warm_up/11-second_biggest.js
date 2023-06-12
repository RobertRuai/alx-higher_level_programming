#!/usr/bin/node

const ag = process.argv;
if (ag.length <= 3) {
  console.log(0);
} else {
  const sd = ag.sort(function (a, b) { return b - a; })[3];
  console.log(sd);
}
