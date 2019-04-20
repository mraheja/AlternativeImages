import cv2
import numpy as np
import check

def save(path,store):
    
    rep = 0
    use = 0
    
    name = path[0:path.find('.')]
    img = cv2.imread('Images\\' + path)
    
    master = cv2.imread("Saves\\master.png")
    
    if(master is None):
        master = []
    
    master = list(master)
    
    max_ind = int(open("Saves\\max_ind.txt",'r').read())
    replace = ""
    
    
    for i in range(0,len(img)-32,32):
        for j in range(0,len(img[0])-32,32):
            
            sections = img[i:i+32]
            save = []
            for section in sections:
                save.append(section[j:j+32])
                
            c = check.check(save,master,store)
            
            #c = -1
            
            
            if(c == -1):
                h = hash(str(save))
                if(not h in store):
                    store[h] = []
                store[h].append(max_ind)
                master.extend(save)
                replace +=  str(max_ind) + " "
                max_ind += 1  
                use += 32*32
            else:
                rep += 32*32
                replace +=  str(c) + " "
                
        replace += "\n"
        
    cv2.imwrite("Saves\\master.png",np.array(master),[cv2.IMWRITE_PNG_COMPRESSION, 3])
    
    file = open("New Images\\" + name + ".rna",'w')
    file.write(replace)
    file.close()
    
    file = open("Saves\\max_ind.txt",'w')
    file.write(str(max_ind))
    file.close() 
    
    print(name,"SAVED",rep,"USED",use)