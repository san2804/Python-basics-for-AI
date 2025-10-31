import numpy as np




# Variables and data types 
name = "Sandil" 
age = 25 
is_learning_ai = True  
print(f"My name is {name}, I am {age} years old, and learning AI: {is_learning_ai}")

numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print("Squares:", squares)

# Dictionary example
student = {"name": "Sandil", "course": "AI Foundations"}
print("Student Info:", student["name"], "-", student["course"])

def add(a, b):
    return a + b

print("Sum:", add(5, 3))

array = np.array([1, 2, 3, 4])
print("Array multiplied by 2:", array * 2)

array = np.array([10,20,30,40])
print("Array divided by 10:", array / 10)

#dot product 

a = np.array([2, 3])
b = np.array([4, 1])
dot_product = np.dot(a, b)
print("Dot Product:", dot_product)
