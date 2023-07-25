#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const res = JSON.parse(body).results;
  let count = 0;
  for (const r of res) {
    for (const c of r.characters) {
      if (c.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
