#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const fs = require('fs');
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (error) console.log(error);
  });
});
