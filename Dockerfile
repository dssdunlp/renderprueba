#Create a ubuntu base image with python 3 installed.
FROM python:3.8

#Set the working directory
WORKDIR /src/app

COPY requirements.txt ./

#se copia el contenido del archivo app.py como ejemplo, a la carpeta /src/example

RUN mkdir -p /src/example

COPY app.py /src/example

#Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 5000
WORKDIR /src/example

#Expose the required port
#EXPOSE 5000

#Run the command
#CMD gunicorn main:app
