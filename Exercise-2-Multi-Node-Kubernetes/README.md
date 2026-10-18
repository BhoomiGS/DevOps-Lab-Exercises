\# Exercise 2: Multi-Node Kubernetes Cluster with Multiple Applications and ReplicaSets



\## Objective

Deploy two Flask applications on a three-node Minikube Kubernetes cluster using Deployments, ReplicaSets, Services, and pod anti-affinity.



\## Applications

\- \*\*Product Catalog:\*\* Flask API exposing `/products`, deployed with 2 replicas.

\- \*\*Shopping Cart:\*\* Flask API exposing `/cart` with GET and POST methods, deployed with 3 replicas.



\## Technologies Used

\- Kubernetes

\- Minikube

\- Docker

\- Python

\- Flask

\- YAML



\## Implementation

1\. Created a three-node Minikube profile named `devops-multinode`.

2\. Built Docker images for both Flask applications.

3\. Deployed Product Catalog with 2 replicas.

4\. Deployed Shopping Cart with 3 replicas.

5\. Configured required pod anti-affinity using `kubernetes.io/hostname` to distribute replicas of each application across different nodes.

6\. Exposed both applications using NodePort Services.



\## Verification

\- Product Catalog Deployment: 2/2 replicas available.

\- Shopping Cart Deployment: 3/3 replicas available.

\- Both applications' pods reached the Running state.

\- All five application pods were distributed across three Kubernetes nodes.

\- Both NodePort Services were created successfully.

\- The Product Catalog endpoint returned product data.

\- The Shopping Cart `/cart` endpoint returned an empty collection initially.



\## Kubernetes Commands

```powershell

kubectl --context=devops-multinode get nodes

kubectl --context=devops-multinode get deployments

kubectl --context=devops-multinode get replicasets

kubectl --context=devops-multinode get services

kubectl --context=devops-multinode get pods -o wide

```



\## Conclusion

Successfully deployed and verified two Flask applications on a three-node Kubernetes cluster with five replicas distributed across the nodes using pod anti-affinity.

