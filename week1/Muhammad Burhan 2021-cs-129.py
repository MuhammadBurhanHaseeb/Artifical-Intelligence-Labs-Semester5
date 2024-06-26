#!/usr/bin/env python
# coding: utf-8

# # <center>Artificial Intelligence Lab</center>  <center>Fall 2023</center>
# ## Lab 01
# #### Name: Muhammad Burhan
# #### Roll number: 2021-cs-129
# Email to: tazeem.haider@uet.edu.pk
# 

# Take weight in kgs and convert it into pounds. 1 pound = 1 kg 2.2046 **(2 marks)**

# In[1]:


## add code here
kg = input("enter weight in kg ")
InPound = float(kg) ** 2.2046
print("the weight in Pounds :",InPound)


# Calculate the cost of all the items in a shopping cart. **(2 marks)**

# In[2]:


prices =[20,50,80,10,56,89]

## add code here
sum = 0 
for x in prices:
    sum = sum + x
print(sum)


# Write a function that returns the maximum of two numbers. **(2 marks)**

# In[3]:


## add code here

def biggest(a,b):
    if a< b:
        return b
    elif b<a:
        return a
    
print(biggest(5,6))


# Write a function called **deepmind** that takes a number  **(4 marks)**
# * If the number is divisible by 3, it should return deep.
# * If it is divisible by 5, it should return mind.
# * If it is divisible by both 3 and 5, it should return deepmind.
# * Otherwise, it should return the same number.
# 
# 
# 

# In[4]:


## add code here

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



# **listA** =  [1,2,3,4,5,6,7,8,9,10]  
# 
# If an element of **listA** is smaller than 5, replace it with 0. And if an element of x is bigger than 5, replace it with 1. (**2 marks**)

# In[5]:


## add code here

listA =  [1,2,3,4,5,6,7,8,9,10] 

for x in range(0,len(listA)):
    if listA[x] < 5:
        listA[x] = 0
    elif listA[x] > 5:
        listA[x] = 1    

print(listA)


# Compute the square of **listA** elements in one line. (**2 marks**)
# 

# In[6]:


## add code here

listA = [1,2,3,4,5,6,7,8,9,10]

a = [x*x for x in listA]


# Concatenate b1 and b2. (**2 marks**)

# In[7]:


b1 = ['Hello', 'in','first']
b2 = ['Students','the','recitation']
## add code here

b2 = b1+ b2
print(b2)

# Create a dictionary of student **Ali** where the keys are courses and values are total and obtaining marks in each course. Print the dictionary items subjects wise **(2 marks)**

# In[8]:


## add code here

student_dic = {
    "oop" : 12 ,
    "dm" : 14
}
print(student_dic["oop"])


# Create a class 'calculator' with the following functions to compute i) addition, ii) subtraction, iii)multiplication, iv)division and v)square
# between two numbers. **(2 marks)**

# In[9]:


## add code here

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

