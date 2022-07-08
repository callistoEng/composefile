FROM python:3.8-slim-buster
# FROM python:3.9.1-alpine
#slimbuster wont work for mysql hence FROM PYTHON:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /Djangogeoloc

LABEL maintainer="admin@homecraft.co.ke"
LABEL description="location based app for homecraft"

# RUN apk add --update gcc netcat postgresql binutils libproj-dev \
#             gdal-bin python-gdal python3-gdal
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal  
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /Djangogeoloc 

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]