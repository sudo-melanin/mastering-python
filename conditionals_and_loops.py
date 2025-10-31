
#Conditional statements and loops in python

#This lesson covers the essential control flow structures in Python: 
#Conditional Statements (if, elif, else) for decision-making and Loops (for, while) for repetition. 
#Understanding these is crucial for writing any meaningful program.



#I. Conditional Statements (The if Family):

#Conditional statements allow your program to make decisions based on 
#whether a condition is True or False.


# 1. Basic 'if' statement
temperature = 35

# The code block only executes if the condition is True.
if temperature > 30:         # This block executes if temperature is greater than 30
    print("It's a hot day!")

# 2. 'if-else' structure
time = 14

if time < 12:               # Executes if the condition is True
    print("Good morning.")
else:                       # Executes if the condition is False
    print("Good afternoon.")

# 3. 'if-elif-else' structure (For multiple conditions)
grade = int(input("Please, Enter your grade: "))

if grade >= 90:
    print("Grade: A")
elif grade >= 80:       # 'elif' stands for 'else if'. 
    print("Grade: B")   #It checks this condition only if the previous 'if' was False.
elif grade >= 70:
    print("Grade: C")
else:                   # The final 'else' block executes if none of the preceding conditions were True.
    print("Grade: Below C")

# Use Case Example: Input Validation
user_input = int(input("Enter a number between 1 and 10: "))

if user_input < 1:
    print("Error: Input is too low.")
elif user_input > 10:
    print("Error: Input is too high.")
else:
    print(f"Valid input: {user_input}")




#II. Combining Conditions with Logical Operators

#Logical operators and, or, and not allow you to combine multiple conditions within a single if statement.

#Discount for students
is_student = True
has_coupon = False
purchase_amount = 60

# 1. Using 'and' (Both must be True for the discount)
if is_student and purchase_amount > 50:
    print("Eligible for student discount on large purchase.")

# 2. Using 'or' (Either condition grants a discount)
if is_student or has_coupon:
    print("A discount will be applied.")
else:
    print("No discount: criteria met.")

# 3. Using 'not' (Negating a condition)
is_weekday = True

if not is_weekday:
    print("It's the weekend!")
else:
    print("Back to work.")

#Ternary Operator (Conditional Expression)
#The ternary operator (also called a Conditional Expression) provides a concise, 
#single-line way to write simple if-else logic, primarily used for assigning a value to a variable.

# 1. Traditional 'if-else' block for assignment
score = 95
status = ""

if score >= 70:
    status = "Passing"
else:
    status = "Failing"
print(f"Traditional Status: {status}")

# 2. Using the Ternary Operator (Conditional Expression)
# Syntax: [value_if_true] if [condition] else [value_if_false]

# The entire expression evaluates to one of the two values ('Passing' or 'Failing')
# based on the boolean result of the condition (score >= 70).
new_status = "Passing" if score >= 70 else "Failing"

print(f"Ternary Status: {new_status}")

# Use Case Example: Setting a configuration based on a flag
is_prod = False

# Set the database connection dynamically in one line
db_host = "prod_db_server" if is_prod else "dev_db_server"

print(f"Database Host: {db_host}")

score = 85

# --- 1. The Standard if/elif/else (Best Practice for multiple conditions) ---
# This is the clear, readable way to handle multiple decision branches.
if score >= 90:
    grade_standard = "A"
elif score >= 80:
    grade_standard = "B"
else:
    grade_standard = "C or lower"

print(f"Standard Grade: {grade_standard}") # Output: B

# --- 2. Nested Ternary Operator (Emulating elif) ---
# The 'else' part of the first condition is replaced entirely by a *second* ternary operator.
# This structure handles the 'elif' logic.
grade_nested = "A" if score >= 90 else ("B" if score >= 80 else "C or lower")

print(f"Nested Ternary Grade: {grade_nested}") # Output: B


#Iteration (Loops)
#Loops are used to execute a block of code repeatedly.

#A. The for Loop (Iterating over Sequences)
#The for loop is typically used to iterate over the elements of a sequence 
# (like a list, tuple, string, or range).

# 1. Iterating over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    # 'fruit' takes on the value of each element in the list, one by one.
    print(f"I like {fruit}.")

# 2. Iterating using the 'range()' function
# range(5) generates numbers 0, 1, 2, 3, 4 (up to, but not including, the stop value).
for i in range(5):
    print(f"Count: {i}")

# range(start, stop, step)
# This will print odd numbers from 1 to 9 (1, 3, 5, 7, 9).
for num in range(1, 10, 2):
    print(f"Odd number: {num}")

# Use Case Example: Calculating a total
prices = [10.50, 5.00, 2.75, 12.00]
total = 0

for price in prices:
    total += price # total = total + price

print(f"Total cost of items: ${total}")


#The while Loop (Condition-Controlled)
#The while loop executes a block of code as long as a specified condition remains True. 
# It's used when the number of iterations is unknown beforehand.

# Initializer
counter = 0

# The loop continues as long as 'counter' is less than 3
while counter < 3:
    print(counter)
    counter += 1 # IMPORTANT: Must update the variable to avoid an infinite loop!

# Use Case Example: Simple user menu until a specific input is given
command = ""
while command != "exit":
    command = input("Enter a command (type 'exit' to quit): ").lower()
    if command == "print":
        print("Executing print command.")
    elif command == "exit":
        print("Exiting application.")
    else:
        print(f"Unknown command: {command}")

#Loop Control Statements
#These statements allow you to change the execution flow within a loop.

#break	Immediately exits the entire loop.
#continue	Skips the current iteration and moves to the next iteration.

# Example: Using 'break' to stop searching
names = ["Alice", "Bob", "Charlie", "David"]
target = "Charlie"

for name in names:
    if name == target:
        print(f"Found {target}!")
        break # Exit the loop immediately once the target is found
    print(f"Checking {name}...")

# Example: Using 'continue' to skip processing
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 != 0: # If the number is odd (remainder when divided by 2 is not 0)
        continue # Skip the print statement and go to the next number
    
    # This print statement only executes for even numbers
    print(f"Processing even number: {num}")



#Nested Structures
#Conditional statements and loops can be nested inside one another to handle more complex logic.

# Nested if/else for detailed access control
user_role = "admin"
access_level = 5

if user_role == "admin":
    # Outer condition met
    if access_level >= 5:
        # Inner condition met
        print("Full administrative privileges granted.")
    else:
        print("Limited administrative access.")
else:
    print("Standard user access.")


# Nested for loops (Useful for working with 2D data like matrices or coordinates)
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Outer loop iterates over the rows
for row in matrix:
    print(f"Starting new row: {row}")
    # Inner loop iterates over the elements (columns) within the current row
    for element in row:
        print(f"  Element value: {element}")


#Nested While Loop
# Initializer for the Outer Loop
i = 1

# Outer Loop: Continues as long as i is less than or equal to 3
while i <= 3:
    print(f"--- Starting Session {i} ---")

    # Initializer for the Inner Loop (MUST be reset *inside* the outer loop)
    j = 0
    
    # Inner Loop: Continues as long as j is less than 2
    while j < 2:
        print(f"  Action {j + 1} completed within Session {i}")
        j += 1 # IMPORTANT: Increment the inner counter
    
    i += 1 # IMPORTANT: Increment the outer counter

print("All sessions complete.")