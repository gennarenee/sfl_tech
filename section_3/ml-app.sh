#!/bin/sh

mod_path=$(pwd)

docker run -p 8501:8501 --name fashion_model   \
     --mount type=bind,source=$mod_path/fashion_model/,target=/models/fashion_model \
      -e MODEL_NAME=fashion_model -t tensorflow/serving