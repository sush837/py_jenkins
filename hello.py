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
def cal1(a):
    cal = ''
    for b in a:
        cal = cal+b
    return cal
print(cal1('USNAM'))

