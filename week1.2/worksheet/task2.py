# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")
numbers.sort()
maximum = max(numbers)
minimum = min(numbers)
mean = sum(numbers) / len(numbers)
middle = len(numbers) // 2

if len(numbers) % 2 == 1:
    median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2

print(f"Minimum = {minimum:.1f}")
print(f"Maximum = {maximum:.1f}")
print(f"Mean = {mean:.1f}")
print(f"Median = {median:.2f}")
