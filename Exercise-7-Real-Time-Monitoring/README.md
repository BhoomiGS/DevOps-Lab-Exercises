\# Real-Time Operations Monitoring and Alerting



A DevOps project for \*\*ZAPPTTO\*\* that simulates delivery-service metrics, monitors operational performance, visualizes metrics using Grafana, and detects abnormal conditions through Prometheus alert rules.



\## Features



\- \*\*Python:\*\* Simulates total deliveries, pending deliveries, deliveries on the way, and average delivery time.

\- \*\*Prometheus:\*\* Scrapes application metrics and evaluates alert rules.

\- \*\*Grafana:\*\* Visualizes delivery performance through a dashboard with four panels.

\- \*\*Docker:\*\* Containerizes the delivery metrics application.

\- \*\*Jenkins:\*\* Automates Docker image building and verifies the availability of the metrics endpoint, Prometheus, and Grafana.



\## Technology Stack



Python, Prometheus, Grafana, Jenkins, Docker, PowerShell, YAML



\## Project Structure



```text

Exercise-7-Real-Time-Monitoring/

├── delivery\_metrics.py

├── prometheus.yml

├── alert\_rules.yml

├── Dockerfile

├── Dockerfile.jenkins

├── Jenkinsfile

├── screenshots/

└── README.md

```



\## Metrics Monitored



| Metric | Description |

|---|---|

| `total\_deliveries` | Total number of simulated deliveries |

| `pending\_deliveries` | Number of pending deliveries |

| `on\_the\_way\_deliveries` | Deliveries currently on the way |

| `average\_delivery\_time` | Average delivery time in seconds |



\## Alerting



Two Prometheus alert rules are configured:



\- \*\*HighPendingDeliveries:\*\* Fires when pending deliveries exceed 10 for 15 seconds.

\- \*\*HighAverageDeliveryTime:\*\* Fires when average delivery time exceeds 30 seconds.



The high-pending-deliveries scenario was tested by increasing simulated pending deliveries to a range of 50–100.



\## Grafana Dashboard



The dashboard contains four panels for total deliveries, pending deliveries, deliveries on the way, and average delivery time.



See the `screenshots/` directory for evidence of the dashboard, alerting, and Jenkins pipeline.



\## Jenkins Pipeline



The Jenkins pipeline:



1\. Checks Docker CLI and engine availability.

2\. Builds the `zapptto-delivery-monitor` Docker image.

3\. Verifies the application metrics endpoint.

4\. Checks Prometheus health.

5\. Checks Grafana health.



\*\*Verification:\*\* The pipeline completed successfully, including the Docker image build and service checks.



\## Run Locally



Install the Python dependency:



```powershell

python -m pip install prometheus-client

```



Start the metrics application:



```powershell

python delivery\_metrics.py

```



Access the metrics endpoint at:



`http://localhost:8000/metrics`



Prometheus and Grafana require their respective services and configurations to be running.



\## Learning Outcomes



\- Application metrics instrumentation

\- Prometheus scraping and alert rules

\- Grafana dashboards

\- Docker image creation and containerization

\- Jenkins pipeline automation and service verification

