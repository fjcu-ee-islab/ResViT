import cv2
import os
import numpy as np
import argparse

def main(args):
    path = str(args.rpath)
    dirlist = os.listdir(path)
    dirlist.sort(key= lambda x:int(x[:-4]))
    a=args.num #####需要改成上一步最後一筆
    for i in dirlist:
        # 讀取圖檔
        img = cv2.imread(path+i)
        flipimg=cv2.flip(img,1)
        a=a+1
        if(a<10):
            cv2.imwrite(str(args.rpath)+'0000'+str(a)+'.png',flipimg)
        elif(a>=10 and a<100):
            cv2.imwrite(str(args.rpath)+'000'+str(a)+'.png',flipimg)
        elif(a>=100 and a<1000):
            cv2.imwrite(str(args.rpath)+'00'+str(a)+'.png',flipimg)
        elif(a>=1000 and a<10000):
            cv2.imwrite(str(args.rpath)+'0'+str(a)+'.png',flipimg)
        else:
            cv2.imwrite(str(args.rpath)+''+str(a)+'.png',flipimg)
            
    path1 = str(args.rpath)
    dirlist = os.listdir(path1)
    dirlist.sort(key= lambda x:int(x[:-4]))
    #a=args.num #####需要改成上一部最後一筆
    for i in dirlist:
        # 讀取圖檔
        img = cv2.imread(path1+i)
        res1 = np.uint8(np.clip((cv2.add(1.5*img,0)), 0, 255))
        res2 = np.uint8(np.clip((cv2.add(0.5*img,0)), 0, 255))
        a=a+1
        if a<10:
            cv2.imwrite(str(args.rpath)+'0000'+str(a)+'.png',res1)
            a=a+1
            if a<10:
                cv2.imwrite(str(args.rpath)+'0000'+str(a)+'.png',res2)
            elif a>=10 and a<100:
                cv2.imwrite(str(args.rpath)+'000'+str(a)+'.png',res2)
        elif a>=10 and a<100:
            cv2.imwrite(str(args.rpath)+'000'+str(a)+'.png',res1)
            a=a+1
            if a>=10 and a<100:
                cv2.imwrite(str(args.rpath)+'000'+str(a)+'.png',res2)
            elif a>=100 and a<1000:
                cv2.imwrite(str(args.rpath)+'00'+str(a)+'.png',res2)
        elif a>=100 and a<1000:
            cv2.imwrite(str(args.rpath)+'00'+str(a)+'.png',res1)
            a=a+1
            if a>=100 and a<1000:
                cv2.imwrite(str(args.rpath)+'00'+str(a)+'.png',res2)
            elif a>=1000 and a<10000:
                cv2.imwrite(str(args.rpath)+'0'+str(a)+'.png',res2)
        elif a>=1000 and a<10000:
            cv2.imwrite(str(args.rpath)+'0'+str(a)+'.png',res1)
            a=a+1
            if a>=1000 and a<10000:
                cv2.imwrite(str(args.rpath)+'0'+str(a)+'.png',res2)
            else:
                cv2.imwrite(str(args.rpath)+''+str(a)+'.png',res2)
                
    path2 = str(args.rpath)
    dirlist = os.listdir(path2)
    dirlist.sort(key= lambda x:int(x[:-4]))
    #a=390 #####需要改成上一部最後一筆
    for i in dirlist:
        # 讀取圖檔
        img = cv2.imread(path2+i)
        (h, w, d) = img.shape
        center = (w//2, h//2)
        # 第一個參數旋轉中心，第二個參數旋轉角度(-順時針/+逆時針)，第三個參數縮放比例
        M1 = cv2.getRotationMatrix2D(center, 15, 1.0)
        M2 = cv2.getRotationMatrix2D(center, -15, 1.0)
        rotimg1 = cv2.warpAffine(img, M1, (w, h))
        rotimg2 = cv2.warpAffine(img, M2, (w, h))
        a=a+1
        if a<100:
            cv2.imwrite(str(args.rpath)+'000'+str(a)+'.png',rotimg1)
            a=a+1
            if a<100:
                cv2.imwrite(str(args.rpath)+'000'+str(a)+'.png',rotimg2)
            else:
                cv2.imwrite(str(args.rpath)+'00'+str(a)+'.png',rotimg2)
        elif a<1000:
            cv2.imwrite(str(args.rpath)+'00'+str(a)+'.png',rotimg1)
            a=a+1
            if a<1000:
                cv2.imwrite(str(args.rpath)+'00'+str(a)+'.png',rotimg2)
            else:
                cv2.imwrite(str(args.rpath)+'0'+str(a)+'.png',rotimg2)
        else:
            if a<10000:
                cv2.imwrite(str(args.rpath)+'0'+str(a)+'.png',rotimg1)
                a=a+1
                if a<10000:
                    cv2.imwrite(str(args.rpath)+'0'+str(a)+'.png',rotimg2)
                else:
                    cv2.imwrite(str(args.rpath)+''+str(a)+'.png',rotimg2)
            else:
                cv2.imwrite(str(args.rpath)+''+str(a)+'.png',rotimg1)
                a=a+1
                cv2.imwrite(str(args.rpath)+''+str(a)+'.png',rotimg2)
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', type=int, default=None)
    parser.add_argument('--rpath', type=str, default=None)
    parser.add_argument('--spath', type=str, default=None)
    opt = parser.parse_args()
    main(opt)