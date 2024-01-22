user_input = input("Enter a sentence: ")

cleaned_input = user_input.replace(" ", "")

lowercase_letters = ""
uppercase_letters = ""

for char in cleaned_input:
    if char.islower():
        lowercase_letters += char  
    else:
        uppercase_letters += char  

result = lowercase_letters + uppercase_letters

print(result)
