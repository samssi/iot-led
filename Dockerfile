
FROM resin/rpi-raspbian:jessie

RUN apt-get update

RUN apt-get install -y \
    build-essential \
    libi2c-dev \
    i2c-tools \
    python-dev \
    libffi-dev \
    python-rpi.gpio \
    python-smbus

# Application setup
RUN mkdir -p /iot-led
WORKDIR /iot-led

ENV HOME /iot-led

COPY . /iot-led

CMD ["python", "/iot-led/app/main.py"]
