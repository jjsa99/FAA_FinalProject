import cv2 as cv
import numpy as np
import pandas as pd


IMAGE_PATH = "C:/Users/UX550/Documents/GitHub/FAA_FinalProject/COVID19_Pneumonia_Normal_Chest_Xray_PA_Dataset/"
DATA_PATH = "C:/Users/UX550/Documents/GitHub/FAA_FinalProject/metadata.csv"


# distribution 
df = pd.read_csv(DATA_PATH)

df["class"].value_counts(normalize = True).plot(kind = 'pie', autopct = "%.1f")

df_covid = df.loc[df["class"] == 1]
df_normal = df.loc[df["class"] == 0]
df_pneumonia = df.loc[df["class"] == 2]

# reset the index counter 
df_covid.reset_index(inplace = True)
df_covid.drop(["index"], axis = 1, inplace = True)
df_normal.reset_index(inplace = True)
df_normal.drop(["index"], axis = 1, inplace = True)
df_pneumonia.reset_index(inplace = True)
df_pneumonia.drop(["index"], axis = 1, inplace = True)

df_data = pd.concat([df_normal,df_covid,df_pneumonia],ignore_index = True)

img_size = 150
data_arr = np.zeros((len(df_data),img_size,img_size))

  
for i in range(len(df_data)):
 image_name = df_data["directory"]
 name = IMAGE_PATH + image_name[i]
 print(name)
 im = cv.imread(name, cv.IMREAD_GRAYSCALE)
 resized_arr = cv.resize(im, (img_size, img_size)) # Reshaping images to preferred size
 data_arr[i] =(resized_arr)
 
print(data_arr[2000])

