''' 
Rules for Defining Variables in Python

Name: Akshay Khapare
Roll Number: 3

A variable in Python is a name used to store a value.
Example:
name = "Akshay"
age = 20

1. Rules for Naming Variables

1. A variable name must start with a letter (A-Z or a-z) or an underscore (_).
   Valid: name, _age
   Invalid: 1age

2. A variable name cannot start with a number.
   Valid: age1
   Invalid: 1age

3. A variable name can contain letters, numbers, and underscores only.
   Valid: user_name, student1
   Invalid: user-name, age@

4. Variable names are case-sensitive.
   Example: age, Age, and AGE are three different variables.

5. Python keywords cannot be used as variable names.
   Invalid: class, if, for, return
   Valid: my_class, user_age

6. Variable names cannot contain spaces.
   Valid: student_name
   Invalid: student name

7. Python does not require a special keyword to declare a variable.
   A variable is created when a value is assigned.
   Example: marks = 85

2. Valid Variable Names

name = "Akshay"
age = 20
_count = 10
student1 = "Rahul"
total_marks = 450

3. Invalid Variable Names

1name = "Akshay"     # Starts with a number
my-name = "Akshay"   # Contains a hyphen
my name = "Akshay"   # Contains a space
class = 10           # Uses a Python keyword
age@ = 20             # Contains a special character

Note: The invalid examples above are for learning purposes and will cause syntax errors if used as code.

4. Python Keywords

Examples of Python keywords include:
if, else, for, while, class, def, return, True, False, None, and import.

You can check whether a word is a keyword with:
import keyword
print(keyword.iskeyword("class"))  # True
print(keyword.iskeyword("name"))   # False

5. Naming Conventions (Best Practices)

- Use meaningful names, such as student_age instead of x.
- Use snake_case for ordinary variables, such as total_marks and first_name.
- Use uppercase for constants by convention, such as PI = 3.14159.
- Avoid single-letter names except in short, obvious cases.

6. Practice Program: variables.py

# Name: Akshay Khapare
# Roll Number: 3
# Topic: Rules for Defining Variables

print("Name: Akshay Khapare")
print("Roll Number: 3")
print("-" * 35)

# Valid variables
student_name = "Akshay"
age = 20
total_marks = 450
_is_student = True

print("Student Name:", student_name)
print("Age:", age)
print("Total Marks:", total_marks)
print("Is Student:", _is_student)

# Case sensitivity
x = 10
X = 20

print("x =", x)
print("X =", X)

Summary:
A variable name must start with a letter or underscore, cannot start with a number, cannot contain spaces or hyphens, and cannot be a Python keyword.

'''