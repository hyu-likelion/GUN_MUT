# 전화번호 목록


# 효율성 통과 못함
# def solution(phone_book):
#     answer = True
#     phone_list = sorted(phone_book, key= lambda x : (x, len(x)))
    
#     for idx, val in enumerate(phone_list):
#         for j in range(idx+1, len(phone_list)):
#            if val == phone_list[j][:len(val)] :
#                return False
   
#     return answer

# 통과 코드
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
        
    
    return True