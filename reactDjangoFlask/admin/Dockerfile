FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
# RUN apt-get update
# RUN apt-get -y install python3-pip
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app


