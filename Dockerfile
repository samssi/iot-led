FROM resin/rpi-raspbian:jessie

RUN apt-get update

RUN apt-get install -y \
    build-essential \
    libi2c-dev \
    i2c-tools \
    python-dev \
    libffi-dev \
    python-rpi.gpio \
    python-smbus \
    python-pip

RUN pip install -U pip
RUN pip install virtualenv
RUN pip install flask

# Application setup
RUN mkdir -p /iot-led
WORKDIR /iot-led
ENV HOME /iot-led
COPY . /iot-led

ENV FLASK_APP=/iot-led/app/main.py

CMD ["flask", "run", "--host=0.0.0.0"]