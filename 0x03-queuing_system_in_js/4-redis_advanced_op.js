import redis from 'redis';
// import { promisify } from 'util';

const client = redis.createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

// Create Hash
const schools = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

for (let [city, value] of Object.entries(schools)) {
  client.hset('HolbertonSchools', city, value, redis.print);
}

client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) console.log(err);
  console.log(obj);
});
