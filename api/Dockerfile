FROM python:3.8.0

RUN mkdir /var/www

WORKDIR /var/www

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y vim && \
  apt-get install -y liblapack-dev && \
  apt-get install -y gfortran && \
  pip install --upgrade pip

COPY requirements.txt /var/www
  
RUN pip install -r requirements.txt

COPY . /var/www/

WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
