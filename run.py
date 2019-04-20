import save
import load
import cv2
import numpy as np
import os
import init

init.init()

#print(os.getcwd())
store = dict()

for file in os.listdir(".\\Images"):
    print(file)
    save.save(file,store)
    




img = load.load("Screenshot_20190410-232140.rna")

cv2.imshow('image',np.array(img))

# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)         
  
# Destroying present windows on screen 
cv2.destroyAllWindows()  
