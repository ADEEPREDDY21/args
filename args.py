#Arbitrary Arguements In Python, arbitrary arguments allow a function to accept an unspecified number of arguments.
#Arbitrary Arguements,*arge
#Arbitrary Keyword Arguments,**kwargs
def my_function(*name):#here *name is an arbitrary argument
    for each in name:#here for each is a variable that can access each element in the name
        print("Hello",each)

my_function('a','b','c','d')    
my_function('a','b','c','d','r','t','y')
print("example 2")
def add_number(*add):
    return sum(add)# here sum is a predefined function that perform addtion operation
    
print(add_number(1,2,3))    
print(add_number(4,6,7,8,5))

print("Example 3")
def my_items(*things):
    for items in things:
        print(items)
my_items("Apple","Banana","Mango")       
#my_items(name="Apple",name2="Banana",name3="Mango")     
                   
print("Example for arbitrary Key Word Arguement")   
#Arbitrary Keyword Arguments,**kwargs
def my_profile(**details):#Here Double Asterisk(**) is used to accept arbitrary keyword arguments(key:value)
    for key,value in details.items():
        print(key,value)
        
my_profile(name="Adeep",age=21,Address="Tadepalligudem")        

def my_function(**kwargs):
    for key,value in kwargs.items():
        print(f"{key.capitalize()}:{value}")
my_function(name="Adeep",age=21,address="tadepalligudem",height=175)        
print("Example 4")        
#Arbitrary Keyword Arguments,**kwargs
def my_code(**kwargs):
    if "name" in kwargs:
        print(f"Hello {kwargs['name']}")
    else:
        print("Hello, Stranger..!")    
    if "age" in kwargs:
        print(f"You are {kwargs["age"]} years old")    
my_code(name="Adeep",age=21)  
my_code()  
print("Example for combining both args and kwargs")
def show_details(*args,**kwargs):
    print("Positional arguement:",args)
    print("Arbitrary Arguements:",kwargs)

show_details(111,22,33,44,name="Adeep",age=21)    
print("Example for Arguements in real time")
def Shopping_cart(*items,**prices):
    print("Items:",items)
    print("Prices:")
    for item,price in prices.items():
        print(f"{item}:${price:.4f}")
Shopping_cart("apple","banana",apple=1.2,banana=2.4) 

print("Defining a function with default value") 
def my_course(course_name="Indemand course"):#Here Indemand course will assign default value to course_name
    print(course_name)
my_course("python")
my_course("java")   
my_course()#in this case it will print "Indemand course" because we have given default value to course_name
my_course("DSA")
