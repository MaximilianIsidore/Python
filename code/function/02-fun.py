def fact(n):
    res =  1
    while(n):
        res *= n
        n-=1
    
    return res

print(fact(5))