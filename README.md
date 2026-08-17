# Toontector

having trouble recognizing a cartoon?? fear not! the toontector is here to help you know which cartoon is which!!

<img width="318" height="159" alt="zimtest2" src="https://github.com/user-attachments/assets/4c222335-bbdd-447c-8cae-e33fb75dbe28" />

## The Algorithm
This project uses the ImageNet classification program from the Jetson Inference library on the NVIDIA Jetson Orin Nano. To install Jetson Inference, follow the [Jetson Inference build instructions](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md). I retrained the ResNet-18 model on a cartoon dataset and used ImageNet to process images.

### Dataset
This is the original Kaggle cartoon [dataset](https://www.kaggle.com/datasets/kanakmittal/anime-and-cartoon-image-classification). I narrowed it down to 5 cartoons: invader zim, spongebob, phineas and ferb, animaniacs, powerpuff girls. I also ran a python script to split the images into test, train, and val folders.


## Training
this code is how I trained the model. I opened the Docker container, I ran the training script for 70 epochs, then I exported the model.
- `cd ~/jetson-inference/`
- `./docker/run.sh`

Inside of the docker container:
- `cd python/training/classification`
- `python3 train.py --epochs=70 --model-dir=models/toon_model data/new_cartoon_dataset`
- `python3 onnx_export.py --model-dir=models/toon_model`

Exit the Docker container (CTRL + D)

## Running this project
1. Clone the project repository.
`git clone https://github.com/MaryJoTheHuman/Toontector.git`
2. Change into the project folder.
`cd Toontector`
3. Set the NET and DATASET variables
- `NET=model/toon_model`
- `DATASET=data/new_cartoon_dataset`
4. Test on any image in the test folder
`imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/CLASS_FOLDER/CLASS_IMG.EXT output/OUTPUT.jpg`
- Replace CLASS_FOLDER with the name of the class (ex. Spongebob)
- Replace CLASS_IMG.EXT with the image file name (ex. 101.png)
- Replace OUTPUT.jpg with your desired output image name

[video demo](https://drive.google.com/file/d/1n362H6FGQUJm4pMa-pHAuGTjZWjTDvSE/view?usp=sharing)
