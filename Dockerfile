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

# Create app directory
RUN mkdir -p /iot-led/app
WORKDIR /iot-led

COPY . /iot-led

ENV HOME /iot-led

CMD ["python", "main.py"]