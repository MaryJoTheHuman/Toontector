# Toontector

having trouble recognizing a cartoon?? fear not! the toontector is here to help you know which cartoon is which!!

![add image descrition here](direct image link here)

## The Algorithm

### Dataset
This is the original Kaggle cartoon [dataset] (https://www.kaggle.com/datasets/kanakmittal/anime-and-cartoon-image-classification). I narrowed it down to 5 cartoons: invader zim, spongebob, phineas and ferb, animaniacs, powerpuff girls. I also ran a python script to split the images into test, train, and val folders.


## Training Process
- `cd ~/jetson-inference/`
- `./docker/run.sh`
Inside of the docker container:
- `cd python/training/classification`
- python3 train.py --epochs=70 --model-dir=models/toon_model data/new_cartoon_dataset`
- `python3 onnx_export.py --model-dir=models/toon_model 

## Running this project

1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

[View a video explanation here](video link)
