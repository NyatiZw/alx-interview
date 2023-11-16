#!/usr/bin/node
const API_URL = 'https://swapi-api.hbtn.io/api';
const request = require('request');

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, _, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

      Promise.all(charactersName)
        .then(names => console.log(names.join('\n')))
        .catch(allErr => console.log(allErr));
    });
}
