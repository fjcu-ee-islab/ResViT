import cv2
import os
import numpy as np
import argparse

def main(args):
    path = str(args.rpath)
    #os.mkdir('retrain/test/moderate')
    dirlist = os.listdir(path)
    dirlist.sort(key= lambda x:int(x[-8:-4]))
    a=0
    for i in dirlist:
        # 讀取圖檔
        img = cv2.imread(path+i)
        print(path+i)
        # 裁切區域的 x 與 y 座標（左上角）
        x = 632
        y = 0

        # 裁切區域的長度與寬度
        w = 495
        h = 495

        # 裁切圖片
        crop_img = img[y:y+h, x:x+w]
        img90=np.rot90(crop_img)
        img90=np.rot90(img90)
        img90=np.rot90(img90)
        img90=np.rot90(img90)
        # 寫入圖檔
        a=a+1
        if(a<10):
            cv2.imwrite(str(args.spath)+'0000'+str(a)+'.png', img90)
        elif(a<100):
            cv2.imwrite(str(args.spath)+'000'+str(a)+'.png', img90)
        elif(a<1000):
            cv2.imwrite(str(args.spath)+'00'+str(a)+'.png', img90)
        elif(a<10000):
            cv2.imwrite(str(args.spath)+'0'+str(a)+'.png', img90)
        else:
            cv2.imwrite(str(args.spath)+''+str(a)+'.png', img90)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--classname', type=str, default="normal")
    parser.add_argument('--rpath', type=str, default=None)
    parser.add_argument('--spath', type=str, default=None)
    opt = parser.parse_args()
    main(opt)