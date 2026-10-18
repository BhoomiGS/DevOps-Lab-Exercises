\# Exercise 4: Scaling Flask App on a Single Node Using ReplicaSets



\## Objective

Deploy a Flask-based flash-sale application on Kubernetes, scale it using a ReplicaSet, and demonstrate automatic recovery when a Pod is deleted.



\## Technologies Used

\- Python and Flask

\- Gunicorn

\- Docker

\- Kubernetes

\- Minikube



\## Application Endpoints

\- `/` — Returns the flash-sale welcome message and serving Pod name.

\- `/buy?user=123` — Simulates a purchase and returns the selected item, user, and serving Pod.

\- `/health` — Reports the application's health and Pod name.



\## Implementation

1\. Created a Flask application with homepage, purchase, and health endpoints.

2\. Created a Docker image named `flashsale:1.0`.

3\. Deployed a Kubernetes ReplicaSet named `flashsale-rs`.

4\. Configured the ReplicaSet initially with three replicas.

5\. Exposed the application using the `flashsale-svc` NodePort Service.

6\. Configured readiness and liveness probes using `/health`.

7\. Scaled the ReplicaSet from three to five replicas.

8\. Deleted a Pod and verified that Kubernetes created a replacement automatically.



\## Verification Results

\- Docker image built successfully.

\- Initial three Pods reached the Running and Ready states.

\- ReplicaSet scaled to five desired, current, and ready replicas.

\- All five Pods ran on the single Minikube node.

\- After deleting a Pod, Kubernetes created a replacement and restored the five-Pod count.

\- Homepage endpoint tested successfully and returned `Welcome to Big Sale!`.

\- Health and purchase endpoints: verify their responses before marking these tests as successful.



\## Conclusion

The exercise demonstrates ReplicaSet-based scaling and self-healing in Kubernetes. The ReplicaSet maintains the desired number of application Pods when a Pod is deleted.



