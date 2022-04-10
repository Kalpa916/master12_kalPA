#count no of capital letters in as string
count=0
def upper(string):
       for i in range(len(string)):
              if(ord(string[i]>=65) and ord(string[i]<=90)):
                     count=count+1
                     print(count)
string='God Is greaT'
upper(string)
       
x=1021
rev=0
while(x!=0):
       rem=x%10
       rev=rev*10+rem
       x=x//10
print(rev)

age=36
txt="my name is john and my age is {}"
print(txt.format(age))
quanity=90
#txtx="1kg of rice costs Rs{}"
#print(txtx.format(quantity))


x=['kala','lake']
print(' and '.join(x))
a="Hello World"
print(len(a))



txt="the best things are free"
if "free" in txt:
       print("Yes")

m="'kala','lake','bajrangi','krupa'"

print("m",m.replace(',','and'))

a = "Hello orld!"
print("a",a.split(",")) 
print(a.translate(a))
a="Hello,World"
print(a.replace(",","and"))
import requests
r = requests.get('https://www.receitaws.com.br/v1/cnpj/27865757000102')
r.json()



Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}    
print (Girls, Boys)







def make_pretty(func):
    def inner(x):
        print("hello")
        func(x)
    return inner
@make_pretty
def ordinary(n):
    print(n)
k=ordinary(10)

def pretty(func):
    def inner():
        print("I am from pretty")
        func()
    return inner    
def mk_pretty(func):
    def inner():
        print("I am from mk_pretty")
        func()
    return inner
#@pretty
#@mk_pretty
def fun(x):
    print(x+90)
K=pretty(fun(10))

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
a=my_gen()
next(a)
next(a)

k=['0','1','2','2','3']
l=(iter(k))
print(next(l))
print(next(l))

print(next(l))

print(next(l))
print(next(l))

def make_pretty(func):
	def inner(a,b):
		print("I am decorator")
		func(a,b)
	return inner
@make_pretty
def printer(a,b):
	print(a/b)
p=printer(999,333)









def star(func):
	def inner(*args,**kwargs):
		print("*"*30)
		func(*args,**kwargs)
	return inner
def percent(func):
	def inner(*args,**kwargs):
		print("#"*30)
		func(*args,**kwargs)
	return inner
@star
@percent
def printer(msg):
	print(msg)
printer('hello')

def smart_Divide(func):
       def p1(a,b):
              print("calling from decorator")
              return func(a,b)
       
       return p1
@smart_Divide
def divide(a,b):
	print(a/b)
divide(10,20)















def make_pretty(func):
       def inner():
              print("It is printed")
              func()
       return inner
def pord():
	print('ordinary')
p=pord()
p1=make_pretty(pord)
p1()

def smart_divide(func):
       def inner(a,b):
              print("dividing both of them")
              return func(a,b)
       return inner
@smart_divide
def divide(a,b):
       print(a/b)
divide(2,4)

def is_called():
       def is_returned():
              print("hello")
       return is_returned

a=is_called()
a()
def make_prety(func):
       print("I got decorated")
       func()
       return make_prety
def ordinary():
       print("I am ordinary")
ordinary()
p=make_prety(ordinary)


n=int(input("enter the length of the array"))
k=[]
for i in range(1,n+1):
       m=int(input("enter the no of digits"))
       k.append(m)
       print(k)
for l in range(n):
       for o in range(l+1,n):
              if(k[l]>k[o]):
                     temp=k[l]
                     k[l]=k[0]
                     k[0]=temp

print(k)































       










              

       
