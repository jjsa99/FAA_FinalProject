from PIL import Image

import cv2 as cv
import numpy as np
import pandas as pd
import os


DATA_PATH = "C:/Users/UX550/Documents/GitHub/FAA_FinalProject/metadata.csv"
image_path = "C:/Users/UX550/Documents/GitHub/FAA_FinalProject/COVID19_Pneumonia_Normal_Chest_Xray_PA_Dataset/covid"




names = []
for subdir, dirs, files in os.walk(image_path):
    for file in files:
        names.append(os.path.join(subdir, file))

print(names[400][-5:])

for i in range(1526):
    #if(names[i][-5:] == '.jpeg'):
    im1 = Image.open(str(names[i]))
    im1.save("C:/Users/UX550/Documents/GitHub/FAA_FinalProject/COVID19_Pneumonia_Normal_Chest_Xray_PA_Dataset/covid/covid_" +str(i)+ ".png")