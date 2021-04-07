def student_func(x):
    answer=''
    if x%5==0 and x%3==0:
        answer="threefive"
    elif x%5==0:
        answer="five"
    elif x%3==0:
        answer="three"
    else :
        answer=x

    return answer