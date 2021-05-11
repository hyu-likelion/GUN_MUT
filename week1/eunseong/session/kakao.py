
import re

def solution(new_id):
    answer=""
    
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9\-\_\.]","", new_id)
    new_id = re.sub("\.{2,}", ".", new_id)
    
    if len(new_id)>0 and new_id[0]==".":
        new_id = new_id[1:]
    if len(new_id)>0 and new_id[-1]==".":
        new_id = new_id[:-1]
        
    if new_id=="":
        new_id="a"
        
    if len(new_id) > 15 :
        new_id = new_id[:15]
        if new_id[-1]==".":
            new_id = new_id[:-1]
        
    if len(new_id) <=2 : 
        while True:
            if len(new_id)== 3 :
                break;
            new_id += new_id[-1]
            
    answer = new_id
    return answer