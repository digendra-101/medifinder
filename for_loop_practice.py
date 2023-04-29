
#print n numbers using for loop
'''
num = int(input("enter the a number"))
for i in range(0,num):
    print (i)
  #  ...............................................................................................................
'''


#to print all evean numbers between a given range
'''
num = int(input("enter the a number"))
for i in range(0,num):
    if i%2==-0:
        print (i)
....................................................................................................................
        '''


#sum of all given natural number
'''
temp=0
num = int(input("enter the a number"))

for i in range (1,num+1):
    temp =temp+i
print (temp)   
 .....................................................................................................................
'''


#sum of all odd numbers between given range
'''
sum=0
num = int(input("enter the a number"))
for i in range(1,num+1):
    if i%2!=0:
        sum=sum+i
print(sum)
 .....................................................................................................................
'''

#program to print a multiplication table of a given number
'''
num=int(input("enter a number"))
for i in range (1,11):
    print(num,"*",i,"=",num*i) 
'''

#program to display numbers from a list using a for loop.
'''
list=[1,2,3,4,5,6,732,83,9]
for i in (list) :
    print(i) 
'''

#program to count the total number of digits in a number.
'''
num=int(input("enter a number "))
num=str(num)
count =0
for i in (num):
    count+=1
print (count)    
'''

#program to check if the given string is a palindrome.

'''
string= input("enter your string : ")
reverse_string = string[::-1]
if string == reverse_string:
    print ("entered string is pellidrom ")
else :
    print("entered string is not a pellidrom")    
'''

#program to check if a given number is an Armstrong number
'''
num= int(input("enter your number"))
num=str(num)

count=0
for i in num:
    count+=1
a=0
for i in num:
   
    a += (int(i) ** count)

num=int(num)
     
if (num==a):
    print("it is an armstrong number")
else :
    print("it is not an armstrong number")               

'''

# program to display all numbers within a range except the prime numbers.
'''
import numpy as np

num= int(input("enter a number: "))
array=np.arange(num) 
print(array)

def is_prime(num):
    count=0
    for i in range(2,num+1):
        a=num%i
        if a==0:
            count+=1
                
    if count==1:
           a=0
    else:
            print(num)
    return (count)

for i in array:
    is_prime(i+1)


'''




