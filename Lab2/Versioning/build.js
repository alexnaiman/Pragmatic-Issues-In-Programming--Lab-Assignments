#!/usr/bin/env node

const pack = require('./package.json');
console.log(process.argv);
var fs = require('fs');
console.log('Incrementing build number...');

const position = {
  major: 0,
  minor: 1,
  patch: 2,
};

require('child_process').exec('git rev-parse HEAD', function(err, hash) {
  console.log('Last commit hash on this branch is:', hash);
  try {
    // eslint-disable-next-line handle-callback-err
    fs.readFile('./package.json', function(err, content) {
      const type = process.argv[2] || 'patch';
      pack.sha = hash;
      pack.version = pack.version
        .split('.')
        .map((item, k) => Number(item) + (k === position[type] ? 1 : 0))
        .reduce((a, b) => `${a}.${b}`);
      fs.writeFile(
        './package.json',
        JSON.stringify(pack),
        function(err) {
          if (err) {
            throw err;
          }
          console.log('Current build number: ' + pack.version);
        },
        () => {
          require('child_process').exec(
            `git add . && git commit -m "increased build number ${pack.version}" && git push origin`,
          );
        },
      );
    });
  } catch (e) {
    console.log(e);
  }
});
