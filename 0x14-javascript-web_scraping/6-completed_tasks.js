#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const res = {};
    const jsn = JSON.parse(body);
    for(let i = 0; i < jsn.length; i++) {
      if (jsn[i].completed == true) {
        if (!res[jsn[i].userId]) res[jsn[i].userId] = 1;
        else res[jsn[i].userId]++;
      }
    }
    console.log(res);
  }
});
