FROM python:3.8.1-slim-buster
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get install -y python3-gdal


RUN mkdir /code
WORKDIR /code

ADD ./requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y openssl
RUN openssl genrsa -des3 -passout pass:MySuperPass -out server.pass.key 2048
RUN openssl rsa -passin pass:MySuperPass -in server.pass.key -out server.key
RUN rm server.pass.key
RUN openssl req -new -key server.key -out server.csr -subj "/C=UK/ST=Warwickshire/L=Leamington/O=OrgName/OU=IT Department/CN=example.com"
RUN openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

ADD . /code/

EXPOSE 8000
