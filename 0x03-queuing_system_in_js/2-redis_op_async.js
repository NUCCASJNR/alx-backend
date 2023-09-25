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
  } finally {
    client.quit();
  }
};

// Call the functions to interact with Redis
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
