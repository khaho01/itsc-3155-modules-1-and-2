# Initialize lists
all_numbers = []
unique_numbers = []

# Take 10 integers from the user
for i in range(10):
    while True:
        try:
            user_input = int(input(f"Enter number {i + 1}: "))
            all_numbers.append(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Create a new list with only unique elements
for number in all_numbers:
    if all_numbers.count(number) == 1:
        unique_numbers.append(number)

# Print both lists
print("All Numbers:", all_numbers)
print("Numbers that appear once:", unique_numbers)
