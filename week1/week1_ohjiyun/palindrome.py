word = input('Enter the word : ')

palindrome = True #초깃값 TRUE
for i in range(len(word) // 2): #문자열 길이 절반만큼 반복
    if word[i] != word[-1 -i]: #왼쪽과 오른쪽 문자 비교
        palindrome = False
        break

print(palindrome)