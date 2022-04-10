def triplet(x): 
  return lambda n : n * x 
final_score = triplet(3) 
print(final_score(11))


#------------------------------------------------------------------------------------

def my_func(company_name): 

    """ 

    This function welcomes reader to 

    HackerTrail 

    """ 

    print("Welcome to, " + company_name + "!") 

my_func('HackerTrail') 
#-------------------------------------------------------------------------------------
str = 'Find the best Python Interview Questions here' 

# Splits at space  

print(str.split()) 


#--------------------------------------------------------------------------------

my_itr = ("Python", "Interview" , "Questions") 

my_str = " ".join(my_itr) 

print(my_str) 

#------------------------------------------------------------------------------------
num = [1, 1, 2, 7,4, 1, 9, 7, 1] 

x = num.count(1) 

print (x) 

#------------------------------------------------------------------------------------
str = "Zero plus three is three." 

x = str.replace("three", "five") 

print(x) 

#-------------------------------------------------------------------------------------
def Rev(lst):  

   mod_lst = lst[::-1]  

   return mod_lst 

lst = [10, 11, 12, 13, 14, 15]  

print(Rev(lst))  

#--------------------------------------------------------------------------------------
mydict={"a":45,"b":89}
print(sum(mydict.values()))


#---------------------------------------------------------------------------------------------
import time
print("dtsrting time")
time.sleep(16)
print("rstarting again")
#---------------------------------------------------------------------------------------------



strMsg="interview"
print("".join(sorted(strMsg)))


















