\# Exercise 8: Introduction to Continuous Integration (CI) and Jenkins Installation



\## Objective

Understand Continuous Integration (CI), Jenkins, and Jenkins installation using Docker.



\## What is Continuous Integration?

Continuous Integration is a development practice where developers frequently integrate code changes into a shared repository. Automated builds and tests help detect errors early and provide immediate feedback.



\## Jenkins

Jenkins is an open-source automation server used to build, test, and deploy software. It supports CI/CD through jobs, pipelines, plugins, and distributed build nodes.



\## Installation and Verification

Jenkins was already installed and running in Docker Desktop, so the existing container was reused instead of creating a duplicate.



\- Container: `jenkins`

\- Image: `jenkins-docker-enabled`

\- Jenkins version: `2.580.1`

\- Web interface: http://localhost:8080/

\- Ports: `8080` (web interface) and `50000` (agent communication)

\- Status: Jenkins fully up and running



\## Verification Commands



```powershell

docker ps --filter name=jenkins

docker logs --tail 20 jenkins

```



The container listing confirmed that Jenkins was running. The logs confirmed that Jenkins completed initialization and was fully up and running.



\## Screenshots

\- `Exercise-8-Jenkins-Dashboard.png` — Jenkins dashboard

\- `Exercise-8-Jenkins-Running.png` — Docker container and startup logs



\## Conclusion

Jenkins was verified running successfully in Docker, and its web interface was accessible on port 8080. The existing Jenkins instance was reused to avoid unnecessary duplicate containers.

