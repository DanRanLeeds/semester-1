import sys
grade = int(input("Enter your grade: "))
try:
    if grade < 40:
        print(grade, "is a Fail")
    elif grade > 39 and grade < 70:
        print(grade, "is a Pass")
    elif grade > 69 and grade <= 100:
        print(grade, "is a Distinction")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")
