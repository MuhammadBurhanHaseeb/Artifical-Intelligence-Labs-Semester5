def dynamic_recursive_Fibonacci(n ,fibonacci={}):
    if n<=1:
        return n
    elif n not in fibonacci:
        fibonacci[n]  = (dynamic_recursive_Fibonacci(n-1 , fibonacci) + dynamic_recursive_Fibonacci(n-2 , fibonacci) )
    return fibonacci[n]
    
print("enter how many term you want to get :")
n = input()
if int(n) <= 0:
    print("plz enter the positive integer")
else:
    print("fibonacci sequence")
    for i in range(int(n)):
        print(dynamic_recursive_Fibonacci(i))