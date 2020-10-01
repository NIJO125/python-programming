def squareof100():
    s1=sum(i for i in range(1,101))
    s2=sum(i**2 for i in range(1,101))
    return str(s1**2 - s2)
print(squareof100())