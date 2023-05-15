# DOCKER

## Instalação
> Link: [Docker](https://docs.docker.com/desktop/)

 ```sh 

#Criar e rodar container com nginx
docker run -ti -p 8081:8081 nginx

#listar containers
docker ps

#lista todos os containers
docker ps -a

#constrói a imagem através do Dockerfile (-t (gerar com tag de versionamento))
docker build -t my-app .




```