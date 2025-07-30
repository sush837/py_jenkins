print("Hello, Jenkins Automation!")
print("Successfully Done!")
a = 10
b = 20
def cal(): 
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)
cal()
def str(s):
    str1 = ''
    for x in s:
        str1 = x+str1
    return str1
print(str('Hello'))
def rep(y):
    rep2 = {}
    for x in y:
        rep2[x] = rep2.get(x,0) +1
    result = {k:v for k,v in rep2.items() if v>1}
    rep3 = 'ijkijkijkijkijkijk'
print(rep(rep3))


