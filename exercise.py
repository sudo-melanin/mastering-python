#1. Movie Ticket Pricer: Write a program using if/elif/else to determine a movie ticket price based on age, 
    # using the following tiers: 0-5 (Free), 6-17 ($8.00), 18-64 ($12.00), and 65+ ($5.00).

# Ask the user for their age
age = int(input("Enter your age: "))

# Determine ticket price based on age brackets
if age >= 0 and age <= 5:
    print("Your ticket is Free!")
elif age >= 6 and age <= 17:
    print("Your ticket price is $8.00")
elif age >= 18 and age <= 64:
    print("Your ticket price is $12.00")
elif age >= 65:
    print("Your ticket price is $5.00")
else:
    print("Invalid age entered.")



#2. Data Validator and Average Calculator: Use an outer for loop to collect exactly 5 numbers. 
    # Inside the for loop, use an inner while loop to repeatedly prompt the user until they enter 
    # a valid positive number (greater than 0). Calculate and print the average of the 5 valid numbers.

total = 0
count = 0

# Outer loop to collect exactly 5 valid numbers
for i in range(5):
    valid = False
    while not valid:
        num = input(f"Enter positive number #{i+1}: ")

        # Check if input is a valid number (integer or float)
        if num.replace('.', '', 1).isdigit():
            number = float(num)
            if number > 0:
                total += number
                valid = True
            else:
                print("Number must be greater than 0.")
        else:
            print("Invalid input. Please enter a positive number.")

# Calculate and print the average
average = total / 5
print(f"The average of the 5 valid numbers is: {average}")