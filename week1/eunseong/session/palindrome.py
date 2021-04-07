def student_func(x):
    length = len(x)
    for i in range(length/2):
        if x[i] != x[length-1-i]:
           return False 

    return True