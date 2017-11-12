# Another option to run the container: 
#docker run --privileged -d -p 5000:5000 iot/led
docker run -d -p 5000:5000 --device /dev/gpiomem iot/led
