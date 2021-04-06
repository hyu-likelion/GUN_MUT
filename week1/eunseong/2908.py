# 상수

a,b = map(int, input().split())

a = int(a[::-1])
b = int(b[::-1])

if( a > b ):
    print(a)
else :
    print(b)