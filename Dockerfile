FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD python routes.py
