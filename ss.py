
my_list = [1, 3, 6, 10]
generator=[x**2 for x in my_list]
print((generator))

for i in range(1,6):
        for j in range(i,0,-1):
                print(j,end='')
        print(" ")


val=2
for i in range(1,10):
        for j in range(1,i+1):
                val=val+1
                print(val,end=' ')
        print(" ")


string = "IT IS IN LOWERCASE."  
print(string.swapcase())
print(string.title())
string = "  javatpoint "  
string2 = "    javatpoint        "  
string3 = "       javatpoint"  

print(string2.strip())
print(string3.strip())

str1="Rohan"

print(str1.capitalize())
str2="Sahoo"
sr=(str1.join(str2))
print(sr)
import random
list1=[12,34,45,66]
random.shuffle(list1)
print(list1)

'''

import smtplib  
# Calling SMTP  
s = smtplib.SMTP('smtp.gmail.com', 587)  
# TLS for network security  
s.starttls()  
# User email Authentication  
s.login("kalpataru7905@gmail.com", "kanha@7905")  
# message to be sent  
message = "Helllo Good Morning"  
# sending the mail  
s.sendmail("kalpataru7905@gmail.com", "sahoo.kps1998@gmail.com", message)

'''
import re
x=['98765678990','8763079231','9337237678','909032123']
for val in x:
	if(re.match("[7-9]{1}[0-9]{9}",val))and(len(val)==10):
		print("phone number are valid")
	else:
		print("phone numbers  are invalid")


#dice of a roll
max1=6
min1=1
import random
x=random.randint(min1,max1)
print(x)












number=int(input("Enter the length of the array:"))
array=[]
for i in range(1,number+1):
       elements=int(input("Enter the elements of the array"))
       array.append(elements)
       print(array)
for m in range(number):
       for n in range(m+1,number):
              if(array[m]>array[n]):
                     temp=array[m]
                     array[m]=array[n]
                     array[n]=temp
print(array)

x=int(input("Enter the number"))
rev=0
while(x!=0):
       rem=x%10
       rev=(rev*10)+rem
       x=x//10
print(rev)


#python to print armstrong number
arm=0
y=int(input("Enter the number"))
while(y!=0):
       rem=y%10
       arm=arm +(rem)**3
       y=y//10
print(arm)

#python to print greater of a number
x=[10,90,45,221,674]
highest=x[0]
n=len(x)
for i in range(1,n):
       if(x[i]>highest):
              highest=x[i]
print(highest)

#fibonacci series(0,1,1,3,3,5)
n1=0
n2=1
for i in range(2,10):
       sum=n1+n2
       n1=n2
       n2=sum
       print(sum)
#swapping any two elements in alist
mylist=[10,20,30,40,50]
print("swap",mylist)
pos1=2
pos2=3
mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)
       
#remove nth ocurence from a list
words=["geeks","for","geeks"]
k="geeks"
count=0
n=len(words)
for i in range(0,n):
       if(words[i]=="geeks"):
              count=count+1
       if(count==2):
              del words[i]
print(words)
              
#Copy of a list

mylist=[10,20,30,40,50]
print(mylist[:])
mylist1=mylist[:]
print(mylist1)




