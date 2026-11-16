import random

# Get user to input how many random numbers they want
num_numbers = int(input("How many random numbers would you like to generate? "))
# Generate this many random numbers
random_nums = [random.randint(1, num_numbers) for _ in range(num_numbers)]
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as outfile:
    for num in random_nums:
        outfile.write(f"{num}\n")

