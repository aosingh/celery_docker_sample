FROM python:3

RUN apt-get update && \
    apt-get install -y --no-install-recommends
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt