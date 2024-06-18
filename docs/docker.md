Docker

https://www.youtube.com/watch?v=3c-iBn73dDE
57:39


Remove docker (uninstall older versions) 
sudo apt-get remove docker docker-engine docker.io

Install docker
sudo apt-get update
sudo apt install docker.io
sudo snap install docker
docker –version

Show locally available images & run image
sudo docker images
sudo docker run -it hello-world


Show all available containers
sudo docker ps -a
Show all running states
sudo docker ps

Start/stop container ID
docker stop d21464dc79dc
docker run d21464dc79dc

Remove image
docker rmi ImageID
sudo docker image rm -f image mysql

Download image
docker pull image_name
of (run en dowlload als het niet is geinstalleerd)
docker run image_name

docker run -it


sudo docker run -d -p0.0.0.0:89:90 mysql:latest


bind container port
(local port = 6000, container port = 6379 container name = redis)
docker run -p6000:6379 redis


