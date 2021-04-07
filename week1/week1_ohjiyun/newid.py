import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower() #소문자 치환

    new_id = re.sub(r"[^a-z0-9\-\_\.]","",new_id) #소문자,숫자,-,_,. 제외 제고

    answer = re.sub(r"[\.]+", ".", new_id) # . 두개 이상 제거

    if answer:
        if answer[0] == '.':
            answer = answer[1]

    if answer:
        if answer[-1] == '.':
            answer = answer[:-1]

return answer
