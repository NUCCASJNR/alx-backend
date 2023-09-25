import redis from 'redis';
const redisPort = 6379;
const redisHost = 'localhost';
const client = redis.createClient(redisPort, redisHost);

// Establish a connection on the redis server

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle any connection error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, response) => {
    if (err) {
      console.error(`Redis Error: ${err}`);
    } else {
      console.log(`Reply: ${response}`);
    }
  });
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

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
client.quit();
