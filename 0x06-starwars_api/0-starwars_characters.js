#!/usr/bin/node

const request = require('request');
const arg = process.argv.slice(2);

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

// Usage:
async function main () {
  try {
    const response = await doRequest(`https://swapi-api.alx-tools.com/api/films/${arg[0]}/`);
    const a = JSON.parse(response).characters;// `response` will be whatever you passed to `resolve()` at the top
    try {
      for (const i of a) {
        const res = await doRequest(i);
        console.log(JSON.parse(res).name);
      }
    } catch (error) {
      console.error(error);
    }
  } catch (error) {
    console.error(error); // `error` will be whatever you passed to `reject()` at the top
  }
}

main();
