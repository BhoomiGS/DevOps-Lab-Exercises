\# Exercise 3: Deploy a Flask App on Minikube Using Kubernetes



\## 1. Objective



To deploy a Python Flask application on Kubernetes using Minikube, Docker, kubectl, and YAML configuration files. The application is exposed using a Kubernetes NodePort Service.



\## 2. Technologies Used



\- Python

\- Flask

\- Docker

\- Kubernetes

\- Minikube

\- kubectl

\- YAML



\## 3. Project Structure



```text

Exercise-3-Flask-Kubernetes/

├── app.py

├── Dockerfile

├── flask-deployment.yaml

└── README.md

```



\## 4. Flask Application



The `app.py` file implements a simple Flask web application.



```python

from flask import Flask



app = Flask(\_\_name\_\_)



@app.route("/")

def home():

&#x20;   return "Hello from Flask on Kubernetes!"



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   app.run(host="0.0.0.0", port=15000)

```



The application listens on port `15000` and returns a greeting when the root endpoint `/` is accessed.



\## 5. Dockerfile



The Dockerfile defines the container image for the Flask application.



```dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY app.py /app/

RUN pip install --no-cache-dir flask

EXPOSE 15000

CMD \["python", "app.py"]

```



\## 6. Build the Docker Image



The image was built using Minikube's image-building command:



```powershell

minikube image build -t flask-app:latest .

```



The build completed successfully, producing the image `flask-app:latest`.



\## 7. Kubernetes Deployment and Service



The `flask-deployment.yaml` file defines a Deployment with one replica and a NodePort Service.



```yaml

apiVersion: apps/v1

kind: Deployment

metadata:

&#x20; name: flask-app

spec:

&#x20; replicas: 1

&#x20; selector:

&#x20;   matchLabels:

&#x20;     app: flask-app

&#x20; template:

&#x20;   metadata:

&#x20;     labels:

&#x20;       app: flask-app

&#x20;   spec:

&#x20;     containers:

&#x20;       - name: flask-app

&#x20;         image: flask-app:latest

&#x20;         imagePullPolicy: Never

&#x20;         ports:

&#x20;           - containerPort: 15000

\---

apiVersion: v1

kind: Service

metadata:

&#x20; name: flask-app-service

spec:

&#x20; selector:

&#x20;   app: flask-app

&#x20; ports:

&#x20;   - port: 15000

&#x20;     targetPort: 15000

&#x20; type: NodePort

```



\### Configuration Explanation



\- \*\*Deployment:\*\* Maintains one replica of the Flask application.

\- \*\*Container image:\*\* Uses the locally available `flask-app:latest` image.

\- \*\*imagePullPolicy:\*\* `Never` tells Kubernetes not to pull the image from a remote registry.

\- \*\*containerPort:\*\* The Flask application listens on port `15000`.

\- \*\*NodePort Service:\*\* Exposes the application and forwards requests to the container on port `15000`.



\## 8. Deploy the Application



Apply the Kubernetes configuration:



```powershell

kubectl apply -f flask-deployment.yaml

```



Expected resources:



```text

deployment.apps/flask-app created

service/flask-app-service created

```



\## 9. Verify the Deployment



Check the Deployment:



```powershell

kubectl get deployments flask-app

```



Verified result:



```text

NAME        READY   UP-TO-DATE   AVAILABLE

flask-app   1/1     1            1

```



The Deployment has one desired replica and one available replica.



\## 10. Verify the Pod



Run:



```powershell

kubectl get pods -l app=flask-app -o wide

```



Verified result:



\- Pod: `flask-app-59f7cdccb4-58fzq`

\- Ready: `1/1`

\- Status: `Running`

\- Restarts: `0`

\- Node: `minikube`

\- Pod IP: `10.244.0.4`



\## 11. Verify the Service



Run:



```powershell

kubectl get service flask-app-service

```



Verified result:



\- Service name: `flask-app-service`

\- Type: `NodePort`

\- Cluster IP: `10.104.140.13`

\- Service port: `15000`

\- NodePort: `30487`



The Service forwards traffic from port `15000` to the Flask container's target port `15000`.



\## 12. Access the Application



Run:



```powershell

minikube service flask-app-service --url

```



Minikube generated the following URL during testing:



```text

http://127.0.0.1:52673

```



The generated URL may change when the service tunnel is restarted. With the Docker driver on Windows, keep the terminal running the URL command open.



Test the application from another PowerShell window:



```powershell

Invoke-RestMethod "http://127.0.0.1:52673"

```



Verified response:



```text

Hello from Flask on Kubernetes!

```



The application successfully returned the expected response.



\## 13. Check Application Logs



Run:



```powershell

kubectl logs deployment/flask-app

```



The logs confirmed that Flask was running on `0.0.0.0:15000`. They also recorded successful requests:



```text

"GET / HTTP/1.1" 200 -

```



HTTP status `200` indicates that the request completed successfully.



\## 14. Inspect Deployment and Service Details



Deployment details:



```powershell

kubectl describe deployment flask-app

```



Service details:



```powershell

kubectl describe service flask-app-service

```



Verified Service endpoint:



```text

10.244.0.4:15000

```



The Service selector `app=flask-app` correctly identifies the application Pod.



\## 15. Results



The following checks were completed successfully:



\- Docker image built successfully.

\- Kubernetes Deployment created with one replica.

\- Pod reached the `Running` state with its container ready.

\- NodePort Service created successfully.

\- Service endpoint correctly mapped to the Flask Pod.

\- Application logs confirmed Flask startup and successful HTTP requests.

\- The application returned `Hello from Flask on Kubernetes!`.



\## 16. Conclusion



Successfully deployed a Python Flask application on Minikube using Docker and Kubernetes YAML configuration. The application was exposed through a NodePort Service and verified using Kubernetes commands, application logs, and an HTTP request.



This exercise demonstrates the basic workflow of containerizing an application, deploying it on Kubernetes, exposing it through a Service, and verifying its operation.

