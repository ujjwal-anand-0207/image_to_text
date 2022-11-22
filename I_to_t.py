from PIL import Image
import os
import pandas as pd
import numpy as np
import re,string,unicodedata
import pytesseract
import warnings
warnings.filterwarnings("ignore")
import gc
import cv2
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract
img=cv2.imread("D:\work\image_to_text\image_to_text_project\pan.jpg")
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
fig=plt.figure(figsize=[10,10])
height,width,channel=img.shape
plt.imshow(img)
# print(type(img))
# print(height,width,channel)
custom_config = r'-l eng+hin'
text=pytesseract.image_to_string(img,config=custom_config)
print(text)
