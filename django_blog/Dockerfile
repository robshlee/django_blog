FROM ubuntu:18.04

RUN apt-get update && apt-get install -y apt-transport-https  \
    sudo \
      curl \
    gnupg2 \ 
    libcurl4 \
    libssl1.0.0 libssl-dev

# get python
RUN apt-get update && apt-get install -y  \
    python3.6 \
    python3-pip \
    python3-setuptools

# not sure what this does yet
RUN apt-get install -y locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

# install git
RUN apt-get update && apt-get install -y git

# update pip
RUN pip3 install 

# set working directory
WORKDIR /usr/src/django_blog

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/base.txt /usr/src/django_blog
COPY requirements/prod.txt /usr/src/django_blog

RUN pip3 install -r prod.txt
RUN pip3 install -e git+http://github.com/larserikgk/django-storages.git#egg=django-storages

COPY . /usr/src/drax/

COPY entrypoint.sh /usr/src/django_blog
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:1337"]

ENTRYPOINT ["chmod", "+x", "./entrypoint.sh"]

# "chmod", "+x", 