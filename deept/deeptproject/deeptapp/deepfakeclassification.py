import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

import logging
import cv2
import numpy as np
#import face_recognition
import re
import os
import torchvision
from torchvision import models
from PIL import Image

def extract_frame(video_path):
    pretrained_model = models.alexnet(pretrained=True)
    pretrained_model.eval()
    print(video_path)
    video = cv2.VideoCapture(video_path)
    count = 0
    num = -1
    
    videoframe = video.get(cv2.CAP_PROP_POS_FRAMES)
    videocount = video.get(cv2.CAP_PROP_FRAME_COUNT)

    while video.isOpened():
        #ret 은 프레임이 존재하지 않을때 T/F 반환
        #frame 은 프레임 반환
        num += 1
        ret, frame = video.read()
        if ret == False:
            print("Frame doesn't Exist")
            break
        if num % 15 == 0:
            if(videoframe == videocount):
                video.open(filename)
            

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    

            try:
                print("1")
                face_image = Image.fromarray(frame)
                trans = torchvision.transforms.ToTensor()
                face_image = trans(face_image)
                c, h, w = face_image.shape
                out = pretrained_model(face_image.reshape(1, c, h, w))
                count += 1

            except Exception as e:
                print("Exception Occurs.", e)
                pass

    video.release()
    cv2.destroyAllWindows()
    return out, count

def do(video_path):
    result, cnt = extract_frame(video_path)
    print("result : {}".format(result))
    logging.warn("result : {}".format(result))
    return("cnt : {}".format(cnt))
    

#if __name__ == "__main__":
#    main()