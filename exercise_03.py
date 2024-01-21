while True:
    try:
        user_input = int(input("Enter a number greater than 1: "))
        if user_input > 1:
            break
        else:
            print("Please enter a valid number greater than 1.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

for i in range(user_input + 1):
    cube = i ** 3
    print(f"The cube of {i} is: {cube}")
