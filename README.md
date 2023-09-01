# MongodbDocker

Deploy a mongodb server through a docker container using one command

## Installing Docker and Docker-compose
If you run linux you can install docker using this commandline
```commandline
sudo apt install-get docker.io
```
You may also get issues connecting the docker service.
The problem is that you need to add the current user into the docker group so that they can run the `docker` command without appending `sudo` 
```commandline
# Create docker group
sudo groupadd docker

# Add user to docker group
sudo usermod -aG docker ${USER}

#RE-authenticate user
su -s ${USER}
```

## Install docker-compose
```commandline
sudo apt install -y docker-compose
```

## Deploy docker container
```commandline
git clone https://github.com/bengabp/MongodbDocker.git
cd MongodbDocker/
docker-compose up -d --build
```
