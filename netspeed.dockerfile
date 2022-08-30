# Using the latest long-term-support Ubuntu OS
FROM ubuntu:18.04

RUN apt -y update
RUN apt -y upgrade
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt -y update
#RUN apt install -y python
RUN apt install -y python3.7
RUN ln -s /usr/bin/python3.7 /usr/bin/python
#RUN apt -y install python-pip
#RUN apt install -y vim man
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN apt install -y tree vim

WORKDIR /home/oe/spdtst
ENV HOME=/home/oe
COPY ./ /home/oe

RUN apt install -y python3-distutils
RUN python /home/oe/get-pip.py

RUN mv $HOME/vimrc $HOME/.vimrc

# RUN apt install -y python3-venv
RUN pip install flask
RUN pip install speedtest-cli
RUN speedtest-cli
#RUN pip install flask-wtf
#RUN pip install flask-sqlalchemy
#RUN pip install flask-migrate
#RUN pip install -U flask-cors


EXPOSE 5005
