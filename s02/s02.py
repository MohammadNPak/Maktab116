# name = input("please enter your name: ")
# print(name)


bool_variable=False
int_variable=5
float_variable=3.14
complex_variable=2+3.3j

print(bool(int_variable))
# if input variable has any value except 0 or 0.0 or "" 
# bool() will return True 
# if input variable has value 0 0.0 or ""
# bool will return False

print(int(bool_variable))
print(float(bool_variable))
print(int(float_variable))
print(float(int_variable))
# print(complex(float_variable))

# convert numbers to str
# we can convert all numbers to str without any error
str(int_variable)
str(float_variable)
str(bool_variable)


# we can convert strings to number if string only contains 
# numbers
print(bool(" "))
