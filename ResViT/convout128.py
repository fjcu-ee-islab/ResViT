import torch
import torch.nn as nn
import torchvision.models.resnet as resnet
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import os
import argparse

def main(args):
    # Create a new ResNet50 class with 128 output channels in the first conv layer
    class ResNet50Custom(resnet.ResNet):
        def __init__(self):
            super(ResNet50Custom, self).__init__(resnet.Bottleneck, [3, 4, 6, 3])
            self.conv1 = nn.Conv2d(3, 128, kernel_size=7, stride=2, padding=3, bias=False)
            self.bn1 = nn.BatchNorm2d(128)

    # Load the custom ResNet50 model
    model = ResNet50Custom()

    # Set the model to evaluation mode
    model.eval()

    # Load the image and preprocess it
    path = str(args.rpath)
    dirlist = os.listdir(path)
    dirlist.sort(key= lambda x:int(x[:-5]))
    a=0
    for i in dirlist:
        image = Image.open(path+i)
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        # Get the output of the first conv layer
        with torch.no_grad():
            conv_output = model.conv1(input_batch)

        # Flatten the array from 4D to 2D and extract the data of the first channel
        for j in range(128):
            conv1_output = conv_output.detach().numpy()[0, j]

            # Scale the array values to the range [0, 1]
            conv1_output = (conv1_output - conv1_output.min()) / (conv1_output.max() - conv1_output.min())

            # Convert the array data type to float 32 and to a PIL acceptable data type 'L'
            conv1_output = (conv1_output * 255).astype(np.uint8)
            conv1_output = Image.fromarray(conv1_output, mode='L')

            # Save the output image to a file
            if(a<10):
                conv1_output.convert('RGB').save(str(args.spath)+'00000'+str(a)+'.png')
            elif(a>=10 and a<100):
                conv1_output.convert('RGB').save(str(args.spath)+'0000'+str(a)+'.png')
            elif(a>=100 and a<1000):
                conv1_output.convert('RGB').save(str(args.spath)+'000'+str(a)+'.png')
            elif(a>=1000 and a<10000):
                conv1_output.convert('RGB').save(str(args.spath)+'00'+str(a)+'.png')
            elif(a>=10000 and a<100000):
                conv1_output.convert('RGB').save(str(args.spath)+'0'+str(a)+'.png')
            else:
                conv1_output.convert('RGB').save(str(args.spath)+''+str(a)+'.png')
            a=a+1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--classname', type=str, default=None)
    parser.add_argument('--rpath', type=str, default=None)
    parser.add_argument('--spath', type=str, default=None)
    opt = parser.parse_args()
    main(opt)