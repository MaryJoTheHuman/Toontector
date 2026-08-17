# Toontector

having trouble recognizing a cartoon?? fear not! the toontector is here to help you know which cartoon is which!!

![add image descrition here](direct image link here)

## The Algorithm
This project uses the ImageNet classification program from the Jetson Inference library on the NVIDIA Jetson Orin Nano. To install Jetson Inference, follow the [Jetson Inference build instructions](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md).I retrained the ResNet-18 model on a cartoon dataset and used ImageNet to process images.

### Dataset
This is the original Kaggle cartoon [dataset] (https://www.kaggle.com/datasets/kanakmittal/anime-and-cartoon-image-classification). I narrowed it down to 5 cartoons: invader zim, spongebob, phineas and ferb, animaniacs, powerpuff girls. I also ran a python script to split the images into test, train, and val folders.


## Training
this code is how I trained the model. I opened the Docker container, I ran the training script for 70 epochs, then I exported the model.
- `cd ~/jetson-inference/`
- `./docker/run.sh`
Inside of the docker container:
- `cd python/training/classification`
- `python3 train.py --epochs=70 --model-dir=models/toon_model data/new_cartoon_dataset`
- `python3 onnx_export.py --model-dir=models/toon_model 
Exit the Docker container (CTRL + D)

## Running this project
1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

[View a video explanation here](video link)
