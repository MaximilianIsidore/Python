def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    if n<1:
        return "Argument must be an integer greater than 0."
    
    nums = ''
    for i in range(1, n+1):
        nums += str(i)

        if(i != n):
            nums += ' '

    return nums

print(number_pattern("g"))
