# Use a base image with Python and other dependencies
FROM ubuntu:18.04

# Install dependencies
# Atualize os pacotes e instale o Python 2.7
RUN apt update
RUN apt install -y python3.10
RUN apt install -y python3-pip
RUN apt install -y git
#RUN apt install -y npm

# Defina a versão padrão do Python
#RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10

# Exemplo: Defina o diretório de trabalho
WORKDIR /home