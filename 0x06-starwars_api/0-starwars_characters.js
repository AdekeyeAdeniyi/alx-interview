#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

if (!filmId || isNaN(filmId)) {
  process.exit(1);
}

const API_ADDRESS = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
const setOption = (url) => {
  return {
    url: url,
    headers: {
      'User-Agent': 'request'
    }
  };
};

request(setOption(API_ADDRESS), (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const { characters } = JSON.parse(body);
    Requestcharacters(characters);
  }
}
);

const Requestcharacters = (characters) => {
  [...characters].forEach(url => {
    request(setOption(url), (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const { name } = JSON.parse(body);
        console.log(name);
      }
    });
  });
};
