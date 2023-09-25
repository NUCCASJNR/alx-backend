import redis from 'redis';
const { promisify } = require('util');

const redisPort = 6379;
const redisHost = 'localhost';
const client = redis.createClient(redisPort, redisHost);
const getAsync = promisify(client.get).bind(client);
// Establish a connection to the Redis server

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle any connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const response = await getAsync(schoolName);
    console.log(`${response}`);
  } catch (err) {
    console.error(`Redis Error: ${err}`);
  }
};

const main = async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
  client.quit();
};
main();
