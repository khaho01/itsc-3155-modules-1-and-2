def number_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Get user input
student_grade = int(input("Enter a grade from 0 to 100: "))

# Check if the input is within the valid range
if 0 <= student_grade <= 100:
    result = number_grade(student_grade)
    print(f'Your grade is: {result}')
else:
    print('Invalid input. Please enter a grade between 0 and 100.')
