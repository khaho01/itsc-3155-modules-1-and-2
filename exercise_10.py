user_input = input("Enter a string: ")

nested_list = [list(user_input[i:i+3]) for i in range(0, len(user_input), 3)]

print(nested_list)
