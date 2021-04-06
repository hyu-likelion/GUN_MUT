# 단어 공부

word = input().upper()
alphabet = list(set(word))
cnt = list()

for i in alphabet:
    tmp = word.count(i)
    cnt.append(tmp)

if cnt.count(max(cnt)) > 1 :
    print("?")
else :
    print(alphabet[cnt.index(max(cnt))])
