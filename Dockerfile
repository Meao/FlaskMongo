FROM python:3.6
ADD . /shop
WORKDIR /shop
RUN pip install -r requirements.txt 