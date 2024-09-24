# variables

name = "Beau" # inline comment
age = 39
print(name)

# expressions 

1+1
"Beau"

# data types

name = "Jake"
print(isinstance(name, str)) # print(type(name) == str) check the type

age = 2.9
print(isinstance(age, float))

# make data type according to your own - can be done with all data types.

age = float(2)
print(isinstance(age, float))

#convert str into int 
# casting

number = "20"  # - number = "test" - ValueError: invalid literal for int() with base 10: 'test'
age = int(number)
print(isinstance(age, int))

# OPERATORS - refer any documentation

# ASSIGNMENT OPERATORS

# CONDITIONAL OPERATORS

# BITWISE OPERATORS

# is - identity operators
# in - membership operators

# ternary operators

def is_adult2(age) :
    return True if age > 18 else False

name = "Beau"
name +=  " is my name"

print(name)

print(
    """Beau is
    
    39
    
    years old
    """
)

print("bEAu pERsOn".title()) 

# isUpper - all list - docs

name = "Beau"
print(name.lower())
print(name)

# global function

print(len(name))
print("au" in name)

# escaping 

name = "Be\au"
print(name)

# squared brackets

name = 'JAKE'

print(name[1])