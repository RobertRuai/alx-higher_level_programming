#!/usr/bin/node
if (isNaN(parseInt(process.argv[3]))) {
  console.log(NaN);
} else {
  function add (a, b) {
    return a + b;
  }
  const res = add.call(this, parseInt(process.argv[2]), parseInt(process.argv[3]));
  console.log(res);
}
