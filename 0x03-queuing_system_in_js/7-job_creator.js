/*
* Track progress and errors with Kue: Create the Job creator
 */

import kue from 'kue';
const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

queue.on('error', (err) => {
  console.error('Kue Error:', err);
});

jobs.forEach((job) => {
  const notification = queue.create('push_notification_code_2', job);

  notification.on('enqueue', () => {
    console.log(`Notification job created: ${notification.id}`);
  });

  notification.on('complete', () => {
    console.log(`Notification job ${notification.id} completed`);
  });

  notification.on('failed', (err) => {
    console.log(`Notification job ${notification.id} failed: ${err}`);
  });

  notification.on('progress', (progress) => {
    console.log(`Notification job ${notification.id} ${progress}% complete`);
  });
  notification.save();
});
