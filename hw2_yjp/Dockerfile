## Yejoon Park
## University of Cincinnati
## Homework 2 Docker

FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3
RUN mkdir /home/sources
RUN mkdir /home/data
RUN mkdir /home/output

ENTRYPOINT ["python3"]

COPY app.py /home/sources/app.py
COPY 1.txt /home/data/1.txt
COPY 2.txt /home/data/2.txt
COPY 3.txt /home/data/3.txt

WORKDIR /home/sources

EXPOSE 80

CMD ["app.py"]
