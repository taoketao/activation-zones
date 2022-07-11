echo ''
echo '**** Navigate to localhost:8000; ignore jupyter ****'
echo ''
docker run --rm \
    -v $(pwd)/tf/:/tf/ \
    --privileged \
    -p 8000:8888 \
    -u $(id -u):$(id -g) \
    --workdir /tf/ \
    -it \
    tensorflow/tensorflow:latest-jupyter 
