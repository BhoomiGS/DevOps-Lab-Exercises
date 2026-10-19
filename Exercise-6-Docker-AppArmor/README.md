# Exercise 6: Docker Security with AppArmor and Python

## Objective
Understand Docker container security using AppArmor profiles, the Docker SDK for Python, and restricted-action testing.

## 1. Flask Application
Created a Flask application in `app.py` that responds on port 5000 with:

`Hello, this is a secure Flask application running inside a Docker container!`

## 2. Docker Image
Built the Docker image using:

```bash
docker build -t flask-apparmor .
```

## 3. AppArmor Platform Finding
The environment uses Docker Desktop with the WSL2 kernel. The following checks were performed:

- `docker info --format '{{.SecurityOptions}}'` showed `seccomp` and `cgroupns`, with no AppArmor entry.
- `cat /sys/module/apparmor/parameters/enabled` returned `N`.
- `/sys/kernel/security/apparmor` was not present.

Therefore, AppArmor enforcement was unavailable in this environment. The requested profile option was tested, but actual AppArmor enforcement could not be demonstrated.

## 4. Flask Container Test
Started the container with the requested security option:

```bash
docker run --security-opt="apparmor=my-apparmor-profile" -p 5001:5000 -d --name flask-apparmor-test flask-apparmor
```

The container started, and `curl http://localhost:5001/` returned the expected Flask response.

## 5. Docker SDK Verification
The `sdk_profile.py` script used the Docker SDK to build the image, start a container, inspect its requested security options, and stop it.

Output confirmed:

`AppArmor profile applied: ['apparmor=my-apparmor-profile']`

This confirms the option was recorded in the container configuration, not that AppArmor enforcement was active.

## 6. Security Tests
The `sdk_security_test.py` script tested reading `/etc/passwd` and executing `/bin/bash`.

- Reading `/etc/passwd`: exit code `0` — succeeded.
- Executing `/bin/bash`: exit code `0` — succeeded.

These actions were not blocked. This is consistent with AppArmor not being enforced in the current environment.

## 7. Questions and Answers

**Q1. What is the purpose of using AppArmor with Docker containers?**

AppArmor enforces mandatory access control policies that confine what a containerized application can access, adding a security layer beyond Docker's default isolation.

**Q2. How do AppArmor profiles help secure a Docker container?**

Profiles define rules that allow or deny access to specific paths, capabilities, and network actions. This can limit the impact of an application compromise.

**Q3. Why restrict access to `/etc/` and `/var/`?**

These directories can contain system configuration, credentials, logs, and other sensitive files. Restricting access helps reduce unauthorized reading or modification.

**Q4. What other capabilities can be restricted using AppArmor?**

Policies can restrict file access, binary execution, network activity, and Linux capabilities such as `cap_sys_admin`.

**Q5. How can you verify whether an AppArmor profile is successfully applied?**

Inspect the container configuration and check its security options. However, the presence of a requested profile name alone does not prove enforcement. Host kernel support and active AppArmor policy must also be verified.

## Conclusion
The Flask application and Docker SDK workflow worked successfully. AppArmor was unavailable in the current WSL2 environment, so the profile's restrictions could not be demonstrated. The limitation and actual test results are documented honestly.
