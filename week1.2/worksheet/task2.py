# Worksheet 1.2: Task 2 Solution
def read_numbers():

    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers
    