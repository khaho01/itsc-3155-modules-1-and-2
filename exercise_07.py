all_numbers = []
even_numbers = []

while True:
    user_input = input("Enter an integer or type 'QUIT' to quit: ")

    if user_input.upper() == "QUIT":
        break

    try:
        number = int(user_input)
        all_numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("All Nums:", all_numbers)
print("Even Nums:", even_numbers)
