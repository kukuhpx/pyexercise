#Creating variable
var_num = 5
var_str = "John"
print(var_num)
print(var_str)

#casting
x = str("3") #String data type
y = int(3)  #Number data type
z = float(3) #Decimal data type
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#String single or double quotes?
#Single pr double quotes isn't different
x = 'Kukuh'
print(x)
x = "Kukuh"
print(x)

#Case sensitive variable's name
a = 6
A = "Prihastomo"
print(A)

#Legal & illegal var's name
""" Legal var's name
    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"
    
    Illegal var's name
    2myvar = "John"
    my-var = "John"
    my var = "John" """

#Type of var's names
""" Camel casemy
    VariableName = "John"
    Pascal Case
    MyVariableName = "John"
    Snake Case
    my_variable_name = "John" """

#Multiple var
a, b, c = "KukuhPx", "27", "182.5"
print(a)
print(b)
print(c)
i = j = k = "Devil"
print(i)
print(j)
print(k)
fruits = ["orange", "Apple", "Rambutan"]
x, y, z = fruits
print(x)
print(y)
print(z)
k = "Kukuh"
p = "Prihastomo"
print(k + " " + p)

#GLobal and local variable
x = "Final" #GLobal var 
def myfunc(): #Local var
    x = "Fantasy"
    print("Final" + " "  + x)
    y = "Final Fantasy"
myfunc() #Calling the function
print(x + " " + "Fantasy")
print(y)

#Global keyword
