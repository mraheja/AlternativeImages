import sys
import load
import cv2
import numpy as np

if(len(sys.argv) != 2):
    print("Invalid Argument")
    exit()
    
img = load.load(str(sys.argv[1]) + ".rna")

cv2.imshow('image',np.array(img))
cv2.waitKey(0)         
cv2.destroyAllWindows()  
