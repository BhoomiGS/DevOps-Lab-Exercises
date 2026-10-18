# Exercise 1: Kubernetes Hello Pod

## Business Scenario
Simulate a Zepto storefront web server using Nginx running in Kubernetes.

## Objective
Deploy an Nginx container as a Kubernetes Pod and access it through a NodePort Service.

## Prerequisites
- Docker Desktop
- Minikube
- kubectl

## Steps Performed
1. Started the local Kubernetes cluster using Minikube.
2. Created the hello-k8s Pod using the Nginx image.
3. Verified the Pod status.
4. Exposed the Pod using a NodePort Service.
5. Opened the Nginx welcome page in a browser.

## Commands
```powershell
minikube start --driver=docker
kubectl run hello-k8s --image=nginx --port=80
kubectl get pods
kubectl expose pod hello-k8s --type=NodePort --port=80
minikube service hello-k8s
```

## Expected Result
The hello-k8s Pod runs successfully, and the Nginx welcome page is accessible through the Service.

## Kubernetes Resources
- pod.yaml: Pod definition
- service.yaml: NodePort Service definition
