FROM python:3.6

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /data

