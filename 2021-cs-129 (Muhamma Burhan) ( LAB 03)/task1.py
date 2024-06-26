
cache = {}
cache['count'] = 0
def compute(a, b):
    return recurse(a, b, len(a), len(b))
def recurse(a, b, m, n):
    if (m, n) in cache:
        return cache[(m, n)]
    if m == 0:
        result = n 
    elif n == 0:
        result = m 
    elif a[m - 1] == b[n - 1]:
        result = recurse(a, b, m - 1, n - 1)
    else:
        c1 = 1 + recurse(a, b, m - 1, n - 1)  
        c2 = 1 + recurse(a, b, m - 1, n)    
        c3 = 1 + recurse(a, b, m, n - 1)   
        result = min(c1, c2, c3)     
    cache[(m, n)] = result
    return result
print("enter the string 1:")
a =input()      
print("enter the string 2:")
b = input()
min_edit_distance = compute(a, b)
print(f"Minimum edit distance between '{a}' and '{b}' is {min_edit_distance}")