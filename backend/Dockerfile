FROM python:3.8.1-slim-buster
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get install -y python3-gdal


RUN mkdir /code
WORKDIR /code

ADD ./requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8000
