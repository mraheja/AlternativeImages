import cv2
import numpy as np

def load(path):
    frame = open("New Images\\" + path,'r').read().split('\n')
    loaded = []
    
    master = cv2.imread("Saves\\master.png")
    
    for e in frame:
        if(len(e) == 0):
            continue
        refs = e.split(" ")
        
        cur = []
        for i in range(32):
            cur.append([])
            
        for ref in refs:
            if(len(ref) == 0):
                continue
            ref = int(ref)
            
            img = master[(ref-1) * 32:ref*32]
            
            for i in range(len(img)):
                cur[i].extend(img[i])
                
        
        
        loaded.extend(cur)
        
    return np.array(loaded)
                
            