# 완주하지 못한 선수

def solution(participant, completion):
    check = dict()
    for i in participant :
        if i not in check :
            check[i] = 1
        else :
            check[i] += 1
    
    for j in completion : 
        if j in check.keys() :
            check[j] -= 1
    
    for k, val in check.items():
        if val > 0 :
            answer = k
            break
    
    print(answer)
    
    return answer