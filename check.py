def same(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a[i][j])):
                if(a[i][j][k] != b[i][j][k]):
                    return False
    return True

def check(a,master,store):
    h = hash(str(a))
    if(not h in store):
        #print("NOT FOUND")      
        return -1
    
    for j in store[h]:
        i = (j-1) * 32
        temp = master[i:i+32]
        if(same(temp,a)):
            #print("FOUND SAME")
            return j
        
    #print("NOT FOUND")
    return -1
    
                
