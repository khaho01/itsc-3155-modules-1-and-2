# Get the number 'n' from the user
n = int(input("Enter a number: "))

float_list = []

for i in range(n):
    user_float = float(input(f"Enter number {i + 1}: "))
    float_list.append(user_float)

print("List:", float_list)

mean = sum(float_list) / n
print("Mean:", mean)
