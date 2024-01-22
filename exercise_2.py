user_input = input("Type a word: ")

reversed_word = ""

for letter in user_input[::-1]:
    reversed_word += letter

print("Reversed Word:", reversed_word)
