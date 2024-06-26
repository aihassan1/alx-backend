0x03-queuing_system_in_js

Project Goal:

Build a basic queuing system using Node.js, Redis, Express.js, and Kue.
Understand how to interact with Redis for storing and retrieving data.
Implement a job creator and processor using Kue.
Requirements:

Ubuntu 18.04
Node.js 12.x
Redis 5.0.7 (provided dump.rdb file can be used)
Basic understanding of JavaScript (ES6+)
Tasks:

Install and Configure Redis:

Download and install the latest stable Redis version (higher than 5.0.7).
Start the Redis server in the background.
Verify the server is running by connecting to it (redis-cli ping).
Use the dump.rdb file provided to populate the Redis server with initial data.
Node.js Redis Client:

Install the node_redis package.
Write a script (0-redis_client.js) to connect to the Redis server.
The script should log messages indicating successful connection or connection error.
Node.js Redis Client and Basic Operations:

Copy the code from the previous task (1-redis_op.js).
Implement two functions:
setNewSchool: Stores a key-value pair in Redis.
displaySchoolValue: Retrieves and logs the value for a given key.
Use callbacks for asynchronous operations.
Node.js Redis Client and Async Operations:

Copy the code again (2-redis_op_async.js).
Modify displaySchoolValue to use async/await for a cleaner approach.
Node.js Redis Client and Advanced Operations:

Write a script (4-redis_advanced_op.js) to store a hash value in Redis.
Use hset to store key-value pairs representing school names and student counts.
Implement hgetall to retrieve and display the entire hash object.
Use callbacks for asynchronous operations.
Node.js Redis Publisher and Subscriber:

Create two scripts:
5-subscriber.js: Subscribes to a channel and logs received messages.
5-publisher.js: Publishes messages to the channel at specified intervals.
The subscriber terminates when it receives the message "KILL_SERVER".
This demonstrates basic pub/sub functionality for message queuing.
Create the Job Creator:

Write a script (6-job_creator.js) to use Kue for creating jobs.
Define a job object containing data (e.g., phone number and message).
Create a queue named "push_notification_code" and add the job to it.
Log messages indicating successful job creation, completion, or failure.
Create the Job Processor:

Write a script (6-job_processor.js) to process jobs using Kue.
Define a function sendNotification to simulate sending a notification.
Create a queue process that listens for new jobs on "push_notification_code".
When a new job arrives, call sendNotification with the job data.
This demonstrates processing jobs from the queue.
Track Progress and Errors with Kue: Create the Job Creator:

Modify the job creator script (7-job_creator.js) to create multiple jobs.
Use an array containing job objects with phone numbers and messages.
Loop through the array and add each job to the queue "push_notification_code_2".
Log messages for job creation, completion, or failure.
Track Progress and Errors with Kue: Create the Job Processor:

Modify the job processor script (7-job_processor.js) to handle job progress and errors.
Define a blacklist containing phone numbers to be blocked.
In sendNotification, check if the phone number is blacklisted.
If blacklisted, fail the job with an error message.
Otherwise, simulate sending the notification and track progress (for demonstration).
Configure the queue to process two jobs concurrently.
This demonstrates tracking job status and handling errors during processing.
