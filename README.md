
# LoadBalancer Tester

This simple aim of the project is to test if a container's load is getting balanced across cluster.
For Demonstration we will use DOCKER SWARM to simulate cluster environment which will load balance our requests.




## Pre-Requisites

- Docker Engine
- Docker Desktop (optional)
- Portainer Conatiner (optional/UI for Clusters)



## Run Locally

Clone the project

```bash
git clone https://github.com/dknaix/Load-balancer-tester.git
```

Go to the project directory

```bash
cd Load-balancer-tester
```

Build Image from Dockerfile

```bash
docker build -t flask-lb-tester:v1.0 .
```

Initialise Docker Swarm

```bash
docker swarm init
```

Create Service

```bash
docker service create --replicas 3 --name flask-lb-tester -p 5000:5000 flask-lb-tester:v1.0
```


## Usage/Examples

```javascript
curl http://localhost:5000

```
If the Container-ID changes after every request means the load is getting balanced, if not meaning there is some misconfiguration.


## Lessons Learned

flask-lb-tester is a light-weight images to quickly test if the a container/pod is getting balanced in a cluster environment. You can build your own version or use build the image from provided Dockerfile.
