name="john doe" # this is a variable
name= "peter jane" # this is called variable overriding
output=""
age=10
weight=12.4
output=age
output=weight

"""
numbers:
-integer: values that span from 0 -> infinity and 0-> -ve infinity, Donot have decimals
integers have a class int()

-float: values that have decimals 

-complex: square-root of -2=> complex number. Hve a class of complex()

"""
numberOne= 10
output= numberOne
output= type(numberOne)
complexNumberOne= 2j
output=complexNumberOne
output= type(complexNumberOne)

numberOne= 12
output=float(numberOne)
output= int(numberOne)
output=complex(numberOne)

numberOne= 10
numberTwo=20
numberTwo=7

output= numberOne + numberTwo
output= numberOne - numberTwo
output= numberOne / numberTwo
output= numberOne // numberTwo
output= numberOne * numberTwo
output= numberOne ** numberTwo
output= numberOne % numberTwo

numberOne=10
numberTwo=20

output=numberOne/numberTwo
output=numberOne//numberTwo
output=numberOne%numberTwo


#userMathProblem=input("kindly input the problem to solve: ")
#output= eval(userMathProblem)


numberThree=20
numberFour=40
output=numberThree==numberFour
output=numberThree<numberFour
output=numberThree>=numberFour

age=18
height=150
output=(age <20 or height> 200)
output=not(age <20 and height> 200)
output=not(age <20 or height> 200)




numberOne=10
numberTwo=11

output=numberOne+numberTwo
#numberOne+=numberTwo
#output=numberOne
numberOne*=numberTwo



output=numberOne
i=0
#i=i+1
i+=1
i=i++1
output=i
i=10
#output=i is 10
#output="about" is "about"
#output="about" is not "about"

fruits=["mango", "banana","apple","melon"]
output="apples" in fruits

name="john doe"
name="Tonny's"
#multiline string 
bio="""
my name is john doe i am a data scientist located in kenya focusing on healthcare.
my core tools of tarde are python,pandas and cola
"""

#output=name
output=bio
output=name[5]
output=name[-1]
output=name[0:6] #slicing
output=name[-1:]
output=name[4:]
output=name[0:8:2]

output=name.upper()
output=name.lower()
output=name.replace("o","u")





age=10
year=2026
if age< 18:
    output="you go home"
else:
    output="go vote"
output="go vote" if age>18 else"smile"

if age<30 or year==2025:
    output="go and learn graphic"
else:
    output="go read!"
output="go vote" if age>18 else"smile"

#utput="hello world"
#output=id(output)

shoecolor="green"
pantscolor="black"
if(shoecolor=="black") and (pantscolor=="yellow") :
    output="we are not looking fo black yellow color!"

elif(shoecolor=="yellow") and (pantscolor=="purple") :
    output="oii not right!"

elif(shoecolor=="blue") and (pantscolor=="white") :
    output="this is nice but not today"
else:
    output="oiii go home"
"""

name="spider woman"
for l in name:
    print(l)
    # if l=="s" :
      # break

    if l=="p" :
        continue
    print(l)

"""
#for num in range(3,11) :
   # if num==4 :
        # continue
   # if num==8 :
       # break
    # print(num)

my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple = 1, 2, 3
print(my_tuple)

single = (5,)
print(single)

t=(10,20,30)
print(t[0])
print(t[-1])


person={
    "name" "maria j"

    "hobby" "dancing"
}
output=person

fruits=["apples","apples","apples","apples","apples","mango","pineapples"]
# output=set(fruits)
"""
function: 
    -achieve goal
"""
output=""
def greetings():
    print("good evening")
#greetings()

def welcomeHome(name) :
    print("welcome Home" +name)
welcomeHome("John doe")



def morningGreetings(goodmorning) :
    return"goodmorning"
def authenticateWithToken() :
    pass
name="francis peter"

# lambda function
x = lambda a,b: a+b
output= x(10,12,14)

# Simple Calculator

# Take input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator"

print("Result:", result)













print("=================================")
print(output)
print("=================================")
