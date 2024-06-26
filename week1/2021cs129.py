
#1
kg = input("enter weight in kg ")
InPound = float(kg) ** 2.2046
print("the weight in Pounds :",InPound)



#2

prices =[20,50,80,10,56,89]
sum = 0 
for x in prices:
    sum = sum + x
print(sum)
    
#3
def biggest(a,b):
    if a< b:
        return b
    elif b<a:
        return a
    
print(biggest(5,6))


#4
def deepmind(a):
    if a/3 ==0 :
        return 'deep'
    elif a/5 == 0:
        return 'mind'
    elif a/3 == 0 and a/5 == 0:
        return 'deepmind'
    else :
        return a
    

print(deepmind(2))


#5 
listA =  [1,2,3,4,5,6,7,8,9,10] 

for x in range(0,len(listA)):
    if listA[x] < 5:
        listA[x] = 0
    elif listA[x] > 5:
        listA[x] = 1    

print(listA)

#6
listA = [1,2,3,4,5,6,7,8,9,10]

a = [x*x for x in listA]



#7 

b1 = ['Hello', 'in','first']
b2 = ['Students','the','recitation']

b2 = b1+ b2
print(b2)

#8 

student_dic = {
    "oop" : 12 ,
    "dm" : 14
}
print(student_dic["oop"])



#9

class calculator :

    def __init__(self) :
        pass
        
    def division(self,a,b):
        c = a/b
        return c
    
    def subtraction(self,a,b):
        c = a - b
        return c
    
    def multiplication(self,a,b):
        c = a * b
        return c
    
    def square(self,a):
        c = a ** 2
        return c
    

a = calculator()
print(a.division(2,1))
print(a.multiplication(2,3))
print(a.square(5))
print(a.subtraction(5,2))

    
