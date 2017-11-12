
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

#RUN useradd -ms /bin/bash sensor
#RUN usermod -G i2c sensor
#RUN usermod -G gpio sensor
#RUN chown -R sensor:sensor /iot-led

#USER sensor
ENV HOME /iot-led

COPY . /iot-led

CMD ["python", "/iot-led/main.py"]
