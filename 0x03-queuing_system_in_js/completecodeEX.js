const express = require('express');
const redis = require('redis');
const kue = require('kue');

// Create an Express app
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Connected to Redis');
});

client.on('error', (err) => {
  console.error('Redis error:', err);
});

// Create a Kue queue
const queue = kue.createQueue();

// Set a key-value pair and queue a job
app.post('/set', (req, res) => {
  const { key, value } = req.body;
  client.set(key, value, (err) => {
    if (err) {
      return res.status(500).send('Error setting key');
    }
    // Queue a job
    const job = queue.create('key_set', { key, value }).save((err) => {
      if (err) {
        return res.status(500).send('Error creating job');
      }
      res.status(200).send(`Key ${key} set with value ${value} and job ${job.id} queued`);
    });
  });
});

// Get a value by key
app.get('/get/:key', (req, res) => {
  const key = req.params.key;
  client.get(key, (err, value) => {
    if (err) {
      return res.status(500).send('Error getting key');
    }
    if (value) {
      res.status(200).send(`Value for key ${key}: ${value}`);
    } else {
      res.status(404).send('Key not found');
    }
  });
});

// Delete a key and queue a job
app.delete('/delete/:key', (req, res) => {
  const key = req.params.key;
  client.del(key, (err, result) => {
    if (err) {
      return res.status(500).send('Error deleting key');
    }
    if (result) {
      // Queue a job
      const job = queue.create('key_deleted', { key }).save((err) => {
        if (err) {
          return res.status(500).send('Error creating job');
        }
        res.status(200).send(`Key ${key} deleted and job ${job.id} queued`);
      });
    } else {
      res.status(404).send('Key not found');
    }
  });
});

// Process jobs
queue.process('key_set', (job, done) => {
  console.log(`Processing job ${job.id} to set key ${job.data.key} with value ${job.data.value}`);
  done(); // Signal that the job is complete
});

queue.process('key_deleted', (job, done) => {
  console.log(`Processing job ${job.id} to delete key ${job.data.key}`);
  done(); // Signal that the job is complete
});

// Define a port
const PORT = process.env.PORT || 3000;

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});



