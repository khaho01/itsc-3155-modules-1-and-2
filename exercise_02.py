string1 = input("Enter a string: ")

string2 = input("Enter another string: ")

if string1.endswith(string2) or string2.endswith(string1):
    print("True")
else:
    print("False")
