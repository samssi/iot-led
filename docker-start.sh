# Another option to run the container: docker run --privileged -d iot/led
docker run --device /dev/gpiomem -d iot/led
