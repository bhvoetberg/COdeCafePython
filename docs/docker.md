Docker

https://www.youtube.com/watch?v=3c-iBn73dDE
1:19:00


# Remove docker (uninstall older versions) 


# Install docker
sudo apt-get update
sudo apt install docker.io
sudo snap install docker
docker –version

# Show locally available images & run image
sudo docker images

# Download image
docker pull image_name
of (run en download als het niet is geinstalleerd)
docker run image_name

docker run -it

# create new container from image
docker run hello-world

# run container in detached mode container
docker run -d mysql:latest

docker run -d -p0.0.0.0:89:90 mysql:latest




# Show all available containers
sudo docker ps -a
## Show all running states
sudo docker ps

# Start/stop container ID
docker stop d21464dc79dc
docker start d21464dc79dc

# Log info
docker logs 'id'

# Remove image
docker rmi ImageID
sudo docker image rm -f image mysql


# Bind ports
bind container port
(local port = 6000, container port = 6379 container name = redis)
docker run -p6000:6379 redis

# enter the terminal of a running container
docker exec -it 'id'  /bin/bash
or
docker exec -it 'name'  /bin/bash
and exit to exit the terminal


# Docker network
docker network ls

docket network create 'network-name'



# Run container in specific network


