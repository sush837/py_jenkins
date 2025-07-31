print("Hello, Jenkins Automation!")
print("Successfully Done!")
a = 10
b = 20
def cal(): 
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    #print("Addition:", addition)
    #print("Subtraction:", subtraction)
    #print("Multiplication:", multiplication)
    #print("Division:", division)
    print(f"Addition: {addition} \nSubtraction: {subtraction} \nMultiplication: {multiplication} \nDivision: {division}")
cal()
def str(s):
    str1 = ''
    for x in s:
        str1 = x+str1
    return str1
print(str('Hello'))
def rep(s):
    rep1 = {}
    for x in s:
        rep1[x] = rep1.get(x,0) +1
    result = {k:v for k,v in rep1.items() if v>1 }
    return result
rep2 = 'xyzxyzxyzxyzxyzxyzxyzxyz'
print(rep(rep2))
def count_1(m):
    count = 0
    for n in m:
        if n == 'a':
            count = count+1
    return count
    print(f"number of 'a'",count)
count = 'ababababababab'
print(count_1(count))



