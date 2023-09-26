const queue = require('kue').createQueue();
const job = queue.create('email', {
  title: 'welcome email for tj'
  , to: 'tj@learnboost.com'
  , template: 'welcome-email'
}).save(function (err) {
  if (!err) console.log(job.id);
});
// queue.close()