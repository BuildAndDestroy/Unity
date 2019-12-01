FROM ubuntu:bionic
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install python-pip -y
RUN pip --version; pip install --upgrade pip
RUN mkdir /opt/Unity/
COPY ./ /opt/Unity/
RUN pip install /opt/Unity/.

