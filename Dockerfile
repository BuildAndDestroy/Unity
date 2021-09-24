FROM debian:latest
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-get install python3 python3-pip -y
RUN pip3 --version; pip3 install --upgrade pip
RUN mkdir /opt/Unity/
COPY ./ /opt/Unity/
RUN pip3 install /opt/Unity/.
