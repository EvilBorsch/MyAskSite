# pull official base image
FROM python:3.7-buster

  # set work directory

WORKDIR /usr/src/ask_gulyachenkov

  # set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

  # install dependencies
RUN pip install --upgrade pip
COPY ./requirments.txt /usr/src/ask_gulyachenkov/requirments.txt
RUN pip install -r requirments.txt

  # copy project
COPY . /usr/src/ask_gulyachenkov/