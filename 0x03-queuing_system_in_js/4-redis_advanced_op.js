/*
* Advanced Redis
*/

import { createClient, print } from 'redis';
const redisPort = 6379;
const redisHost = 'localhost';
const client = createClient(redisPort, redisHost);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle any connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const data = {
  Portland: 20,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

Object.entries(data).forEach(([key, value]) => {
  client.HSET('HolbertonSchools', key, value, print);
});
client.HGETALL('HolbertonSchools', (err, response) => {
  if (err) {
    console.error(`Redis Error: ${err}`);
  } else {
    console.log(response);
  }
});

// client.DEL("HolbertonSchools", (err, response) => {
//   if (err) {
//     console.error(`Redis Error: ${err}`);
//   } else {
//     console.log(`Deleted key "HolbertonSchools"`);
//   }
// });

client.quit();
