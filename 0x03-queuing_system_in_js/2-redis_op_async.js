import redis from 'redis';
const promisify = require('util').promisify;

import { utils } from 'mocha';
const client = redis.createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const getSchool = promisify(client.get);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getSchool(schoolName);
    if (value) {
      console.log(value);
    } else {
      console.log('Not Found');
    }
  } catch (err) {
    console.log(err);
  }
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
