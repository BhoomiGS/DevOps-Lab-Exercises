\# Exercise 5: Docker Networking with Multiple Containers



\## Objective

Understand Docker bridge networking and configure communication between a Flask application, MySQL database, and Redis cache.



\## Technologies Used

\- Docker

\- Python

\- Flask

\- MySQL

\- Redis

\- Docker Bridge Network



\## Implementation

1\. Built the Flask application image named `flask-api`.

2\. Created a bridge network named `my-bridge-net`.

3\. Launched MySQL, Redis, and Flask containers on the same network.

4\. Published Flask port 5001 to host port 5001.

5\. Tested the Flask `/about` endpoint.

6\. Verified connectivity from Flask to MySQL on port 3306.

7\. Tested connectivity from Flask to Redis on port 6379.



\## Verification Results

\- Docker image built successfully.

\- Bridge network created and inspected successfully.

\- All three containers started successfully.

\- Flask `/about` returned the expected JSON response.

\- Flask-to-MySQL TCP connection succeeded.

\- Flask-to-Redis TCP connection: record the result after successful verification.



\## Lab Questions and Answers



\### 1. What is the purpose of the `--net` flag in `docker run`?

It specifies which Docker network the container should join.



\### 2. How do containers communicate on the same network?

They can use container names or IP addresses. Docker's embedded DNS resolves container names on a user-defined bridge network.



\### 3. What is the difference between bridge and host networking?

A bridge network provides an isolated network for containers. Host networking shares the host's network stack instead of providing the same kind of separate container network.



\### 4. How can you expose a container's port to the host?

Use the `-p` flag. For example, `-p 5001:5001` maps host port 5001 to container port 5001.



\## Conclusion

The exercise demonstrates how Docker containers can communicate through a shared user-defined bridge network and how to publish a container port to the host.



