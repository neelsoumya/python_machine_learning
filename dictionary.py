# teaching dict in Python

# Example of a Python dictionary

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Accessing values in the dictionary
print("Name:", student["name"])  # Output: Name: Alice
print("Age:", student["age"])    # Output: Age: 21
print("Major:", student["major"])  # Output: Major: Computer Science

# Adding a new key-value pair
student["graduation_year"] = 2025
print("Updated student dictionary:", student)

# Updating an existing value
student["age"] = 22
print("Age after update:", student["age"])  # Output: Age after update: 22

# Removing a key-value pair
del student["major"]
print("After removing 'major':", student)

# Looping through the dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Check if a key exists
if "name" in student:
    print("Name is a key in the student dictionary.")

# Get the length of the dictionary
print("Number of key-value pairs:", len(student))
