FROM ubuntu:latest

EXPOSE 5001

RUN mkdir -p /srv/gui
COPY ./src/* ./srv/gui

RUN mkdir -p /tests

RUN apt update

RUN apt install -y python3 python3-pip vim
RUN pip install quart flask requests pymongo

RUN chmod +x /usr/local/lib/python3.10/dist-packages/quart/utils.py

WORKDIR /srv/gui

ENTRYPOINT [ "python3", "main.py" ]