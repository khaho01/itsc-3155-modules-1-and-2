while True:
    try:
        row_number = int(input("Enter a row number 1 to 5: "))
        column_number = int(input("Enter a column number 1 to 5: "))
        if 1 <= row_number <= 5 and 1 <= column_number <= 5:
            break
        else:
            print("Please enter valid row and column numbers.")
    except ValueError:
        print("Invalid input. Please enter valid integers.")

for i in range(1, 6):
    for j in range(1, 6):
        if i == row_number and j == column_number:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
