import os

def init():   
    for file in os.listdir(".\\New Images"):
        os.remove("New Images\\" + file)
        
    for file in os.listdir(".\\Saves"):
        os.remove("Saves\\" + file)
        
    file = open("Saves\\max_ind.txt",'w')
    file.write('1')
    file.close()