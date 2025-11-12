
x = 15
if x < 0:
    raise Exception("Number should be greater than 0")

try:
    assert(x<10),"The number must be less than 10"
except:
    print("Even errors from assertion is catched")

try:
    a = 5/1
except Exception as e:
    print(e)
else:
    print("something from else")
finally:
    print("finally")