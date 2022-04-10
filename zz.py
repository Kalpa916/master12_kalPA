'''
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                             user='root',
                             password='kanha@12345',
                             database='tutorial',)
cur1=connection.cursor()
cur1.execute("create table emp4m(esal LONGBLOB)")

def InsertBlob(filepath):
       with open(filepath,'rb') as file:
              BinaryData=file.read()
       SQLStatement="INSERT INTO Images23(id1,Photo) VALUES(%s,%s)"
       cur1.execute(SQLStatement,(1,BinaryData,))
       
connection.commit()

       
MenuInput=input("Enter the value")
if int(MenuInput)==1:
       UserFilePath=input("Enter File path:")
       InsertBlob(UserFilePath)
       
else:
       pass
'''
x=[10,20,40,53]
a=len(x)
max1=x[0]
for i in range(1,a):
       if(max1<x[i]):
              max1=x[i]
print(max1)

             

def mergesort(list1):
       if(len(list1)>1):
              mid=len(list1)//2
              left=list1[:mid]
              right=list1[mid:]
              mergesort(left)
              mergesort(right)
              i=0
              j=0
              k=0
              while(i<len(left)) and (j<len(right)):
                     if(left[i]<right[j]):
                            list1[k]=left[i]
                            i=i+1
                            k=k+1
                     else:
                            list1[k]=right[j]
                            j=j+1
                            k=k+1
              while(i<len(left)):
                     list1[k]=left[i]
                     i=i+1
                     k=k+1
              while(j<len(right)):
                     list1[k]=right[j]
                     j=j+1
                     k=k+1
num=int(input("Enter the len of the list:"))
list1=[int(input("enter the values")) for x in range(num)]
s=mergesort(list1)
print(list1)

#[12, 12, 12, 21, 21, 21, 23, 121, 123, 212, 1212, 1223]
