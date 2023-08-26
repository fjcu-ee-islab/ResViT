import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import os
import argparse

def main(args):
    # 載入 ResNet50 模型
    model = models.resnet50(pretrained=True)

    # 將模型設置為評估模式
    model.eval()

    # 載入影像並對其進行預處理
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

        # 將影像輸入模型，獲取第一層卷積的輸出
        with torch.no_grad():
            conv_output = model.conv1(input_batch)

        # 將數組從 4 維展平為 2 維，從中提取第一個通道的數據（第一層卷積的輸出）
        for j in range(64):
            conv1_output = conv_output.detach().numpy()[0, j]

            # 將數組的數值範圍縮放到 [0, 1] 的範圍內
            conv1_output = (conv1_output - conv1_output.min()) / (conv1_output.max() - conv1_output.min())

            # 將數組的數據類型轉換為浮點數 32 位，並將其轉換為 PIL 可接受的數據類型 'F'
            #conv1_output = conv1_output.astype('float32')
            #conv1_output = Image.fromarray(conv1_output, mode='F')

            # 將數組的數據類型轉換為 PIL 可接受的數據類型 'L'
            conv1_output = (conv1_output * 255).astype(np.uint8)
            conv1_output = Image.fromarray(conv1_output, mode='L')

            # 將輸出影像儲存到文件中
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
            #conv1_output.save(str(i)+'resnet_conv1_output.png')

            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--classname', type=str, default="normal")
    parser.add_argument('--rpath', type=str, default=None)
    parser.add_argument('--spath', type=str, default=None)
    opt = parser.parse_args()
    main(opt)