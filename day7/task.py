"""
write four functions that perform the following tasks:
add(a, b): returns the sum of a and b
multiply(a, b): returns the product of a and b
power(a, b): returns a raised to the power of b
subtract(a, b): returns the difference of a and b
"""

def add(a, b):
  return a + b

def multiply(a, b):
  return a * b

def power(a, b):
  return a ** b

def subtract(a, b):
  return a - b

input_values = input("Enter two numbers separated by space: ")
a, b = map(int, input_values.split())
print(f"The addition =", add(a, b))        
print(f"The multiplcation =", multiply(a, b))   
print(f"The raised to power =", power(a, b))      
print(f"The subtraction is =", subtract(a, b))  
