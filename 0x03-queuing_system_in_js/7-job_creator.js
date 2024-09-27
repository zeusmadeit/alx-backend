#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const jobs = [
  {
    phoneNumber: '2456790543',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '5317654621',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '3111563545',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '3111563541',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '3111563542',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '3111563543',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '3111563544',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '31115635456',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '3111563547',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '3111563548',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '3111563549',
    message: 'This is the code 4321 to verify your account',
  },
];

const queue = createQueue({ name: 'push_notification_code_2' });

for (const jobInfo of jobs) {
  const job = queue.create('push_notification_code_2', jobInfo);

  job
    .on('enqueue', () => {
      console.log('Notification job created:', job.id);
    })
    .on('complete', () => {
      console.log('Notification job', job.id, 'completed');
    })
    .on('failed', (err) => {
      console.log('Notification job', job.id, 'failed:', err.message || err.toString());
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
  job.save();
}
