import calc.arithmetic as arithmetic

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
op =  input("Enter the operator : ")

ans = None

if(op == '+'):
    ans = arithmetic.add(a,b)
elif(op == '-'):
    ans = arithmetic.sub(a,b)
elif(op == '*'):
    ans = arithmetic.mul(a,b)
elif(op == '/'):
    ans = arithmetic.div(a,b)
elif(op == '%'):
    ans = arithmetic.mod(a,b)
else:
    print("invalid choice")

print("Answer = ", ans)


