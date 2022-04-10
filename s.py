data="June 15th,August 9,Dec 12,Feb 22,jul ,2020,2019"
pattern="([a-zA-z]+) \d+"
import re
n=re.findall(pattern,data)
print(n)




data='''Miller DOB: June 15th,
Blake DOB: August 9th
Ajay DOB: Febrauary 21st
Amar DOB: march 17th'''
k=":([a-zA-Z]+) \d+"
n=re.findall(k,data)
print(n)
k="([a-zA-Z]+) DOB"
l=re.findall(k,data)
print(l)
x=[]
y=[]
for i in l:
       x.append(i)
       print(x)
for j in k:
       y.append(j)
k=zip(x,y)
m=list(k)
n=dict(m)
print("l",n)

import re
scorecard='''Rohith=45
Kohli=104
Dhoni=34
Raina=44
Dhawn=38
Ghambir=8
'''

data=re.findall("\d+",scorecard)
print(data)
scores=[]
for i in data:
       scores.append(int(i))
       print(sum(scores))

import re
x=['9983764321','7384963897','8376412769','938476182']
xk=(re.match("[7-9]{1}[0-9]{9}",x))
print(x)

     
















data='''
1st worldcup held in the year 1975
2nd worldcup held in the year 1979
3rd worldcup held in the year 1983
4th worldcup held in the year 1987
5th worldcup held in the year 1992
6th worldcup held in the year 1996
7th worldcup held in the year 1999'''
import re
s=re.findall("\d{4}",data)
print(s)


txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


import re
data="JAN 15,MARCH 05,APRIL 16"
s=re.findall("\w",data)
print(s)




#python program to sort a list without sorting the element

arr_length=int(input("Enter the length of the array"))
array=[]
for i in range(1,arr_length+1):
       k=int(input("Enter the values"))
       array.append(k)
       print(array)
for k in range(arr_length):
       for j in range(k+1,arr_length):
              if(array[k]>array[j]):
                     temp=array[k]
                     array[k]=array[j]
                     array[j]=temp

print(array)

#python to reverse a number using while loop

rev=0
num=int(input("Please enter the number"))
while(num!=0):
       rem=num%10
       rev=(rev*10)+rem#32
       num=num//10
print(rev)
#python to print prime numbers
x=int(input("Enter the number"))
count=0
if(x>0):
       for i in range(1,x+1):
              if(x%i==0):
                     count=count+1
if(count==2):
       print("no is prime")
else:
       print("no is not prime")


n=int(input("Enter the number"))
i=0
for i in range(0,n+1):
       k=k+i
       print(k)
'''
import cv2
k=cv2.imread("")
cv2.imshow(k)

'''
import sqlite3
with open(r"C:\Users\admin\Pictures\hug-kiss-images.jpg","rb")as f1:
       m=f1.read()
with open("recieve.png","wb")as f2:
       f2.write(m)
name="kalpataru"
with open ("recieve.png","rb") as f:
       data=f.read()
conn=sqlite3.connect("hello.db")
#cur1=conn.cursor()
#cur1.execute("CREATE TABLE IF NOT EXISTS OK(NAME TEXT,DATA BLOP)")
cur2=conn.cursor()
#cur2.execute("INSERT INTO OK(NAME,DATA) VALUES (?,?)"(name,data))

cur2.execute("""INSERT INTO OK(name,data) VALUES (?,?)""",(name,data))
conn.commit()

              
