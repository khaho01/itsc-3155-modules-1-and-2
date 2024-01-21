def get_integer_list(list_name):
    integer_list = []
    print(f"Enter numbers for the {list_name} list:")
    for i in range(5):
        while True:
            try:
                num = int(input(f"Enter a number for the {list_name} list: "))
                integer_list.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return integer_list

list1 = get_integer_list("first")
list2 = get_integer_list("second")

common_list = list(set(list1) & set(list2))

print("First List:", list1)
print("Second List:", list2)
print("Common List:", common_list)
