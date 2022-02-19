import cv2 as cv
import numpy as np
import pandas as pd
import os
from PIL import Image
# sklearn library 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.metrics import classification_report


IMAGE_PATH = "C:/Users/UX550/Documents/GitHub/FAA_FinalProject/COVID19_Pneumonia_Normal_Chest_Xray_PA_Dataset/"
DATA_PATH = "C:/Users/UX550/Documents/GitHub/FAA_FinalProject/metadata.csv"

img_size = 150
data = []
folders = ["covid","normal","pneumonia"]
for i in range(len(folders)):
    image_path = IMAGE_PATH + str(folders[i])
    print(folders[i])
    print(image_path)
    for subdir, dirs, files in os.walk(image_path):
        for file in files:
            aux_name = str(subdir) + "/" + str(file)
            # read image
            img_arr = cv.imread(aux_name,cv.IMREAD_GRAYSCALE)
            # resize image
            resized_arr = cv.resize(img_arr,(img_size,img_size))
            data.append([resized_arr, i+1])
            #print(names)

# convert the list into a dataframe
data_df = pd.DataFrame(data,columns=['feature','class'])

# randomize the data
data_rand = data_df.sample(frac = 1)

train_X, test_X, train_Y, test_Y = train_test_split(data_rand['feature'],data_rand['class'],random_state = 50, test_size= 0.4)
test_X, val_X, test_Y, val_Y = train_test_split(test_X,test_Y,random_state = 50, test_size= 0.5)

# Normalize the data
x_train = np.array(train_X) / 255
x_val = np.array(val_X) / 255
x_test = np.array(test_X) / 255




