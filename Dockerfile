FROM python:3.9.6

LABEL MAINTAINER="Candido Souza <candidosouzza@gmail.com>"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/product/app

ENV PATH $PATH:/home/product/.local/bin

COPY requirements.txt /home/product/app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/product/app

ENTRYPOINT ["./.docker/entrypoint.sh"]