#!/usr/bin/node

const redis = require('redis');
const redisPort = 6379;
const redidHost = 'localhost'
const client = redis.createClient(redisPort, redidHost);

client.set('Name', 'Al-Areef', (err, reply) => {
  if (err) {
    console.error(err)
  } else {
    console.log(`Key Set: ${reply}`);
  }
});

client.get('Name', (err, reply) => {
  if (err) {
    console.error(err)
  } else {
    console.log(`Value: ${reply}`);
  }
})
// Example: Working with lists
client.lpush('myList', 'item1', 'item2', (err, reply) => {
  if (err) {
    console.error(err);
  } else {
    console.log('List length:', reply);
  }
});

client.lrange('myList', 0, -1, (err, reply) => {
  if (err) {
    console.error(err);
  } else {
    console.log('List contents:', reply);
  }
});

client.quit()