import os
import json
import argparse

import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt

from vit_model import vit_base_patch16_224_in21k as create_model


def main(args):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
   
    data_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
         transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])])

    List=[]
#normal
#severe
#mildmoderate
    tlist=["normal","mms"]
    a=0
    for i in range(1,3):
        #print(tlist[a])
        ptn = "data/retrain/test/"+tlist[a]+"/"
        dir = os.listdir(ptn)
        dir.sort()
        pro=0
        n=0
        for j in dir:
            img_path = (ptn+j)
            #print(j)
            assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
            img = Image.open(img_path)
            plt.imshow(img)
            # [N, C, H, W]
            img = data_transform(img)
            # expand batch dimension
            img = torch.unsqueeze(img, dim=0)

            # read class_indict
            json_path = 'class_indices21.json'
            assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)

            with open(json_path, "r") as f:
                class_indict = json.load(f)
            # create model
            model = create_model(num_classes=2, has_logits=False).to(device)
            # load model weights
            model_weight_path = str(args.wpath)
            model.load_state_dict(torch.load(model_weight_path, map_location=device))
            model.eval()
            with torch.no_grad():
                # predict class
                output = torch.squeeze(model(img.to(device))).cpu()
                predict = torch.softmax(output, dim=0)
                predict_cla = torch.argmax(predict).numpy()

            print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
                                                     predict[predict_cla].numpy())
            plt.title(print_res)

            for k in range(len(predict)):
                #print("class: {:10}   prob: {:.3}".format(class_indict[str(k)],
                #                                      predict[k].numpy()))
                if class_indict[str(k)] == tlist[a]:
                    pro=float(pro)+float(predict[k].numpy())
                    n=n+1
        if a==0:
            acc0 = float(pro/n)
        elif:
            acc1 = float(pro/n)
            acc = (round(acc0)+round(acc1))/2
            #print(tlist[a]+" average accuracy : " + str(acc))        
            #if n==len(dir):
            f = open("predict.txt", "a")
            #f.write(str(args.wpath)+" "+tlist[a]+" average accuracy : "+ str(acc)+"\n")
            f.write(str(args.wpath)+"  average accuracy : "+ str(acc)+"\n")
            f.close()
        a=a+1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--classname', type=str, default="normal")
    parser.add_argument('--wpath', type=str, default=None)
    opt = parser.parse_args()
    main(opt)