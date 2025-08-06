#!/user/bin/env bash

set -e


pip install poetry
if  ! [ -f "api/model-bird_classifier.pkl" ]; then
    cd data 
    poetry install
    poetry run python pipeline.py
    cd ..

    cd model
    poetry install
    poetry run python pipeline.py
    cd ..
fi
cd api 
poetry install

