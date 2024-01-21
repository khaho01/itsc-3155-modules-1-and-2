word_list = []

for i in range(5):
    word = input(f"Enter word #{i + 1}: ")
    word_list.append(word)

resultant_string = " ".join(word_list)

print("Word List:", word_list)
print("Resultant String:", resultant_string)
