import redis from 'redis';
const redisPort = 6379;
const redisHost = 'localhost';
const client = redis.createClient(redisPort, redisHost);

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

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, response) => {
    if (err) {
      console.error(`Redis Error: ${err}`);
    } else {
      console.log(`${response}`);
    }
  });
};

// Call the functions to interact with Redis
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

// Quit the Redis client when done
client.quit();
