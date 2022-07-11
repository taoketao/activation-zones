

docker run --rm \
    -v $(pwd)/tf/:/tf/ \
    --privileged \
    -p 8000:8888 \
    -u $(id -u):$(id -g) \
    --workdir /tf/ \
    -it \
    tensorflow/tensorflow:latest-jupyter 
#    bash ./.run_jupyter.sh

    
  # jupyter/tensorflow-notebook:latest
#    bash
#    jupyter notebook  --autoreload --allow-root
#    jupyter notebook --port=8061 --autoreload --allow-root
