
# function implementation
base = float(input("Enter base length: "))
height = float(input("Enter height: "))
def rectangle_area(base, height):  # define suitable input data
    area = base*height               # implement the function
    return(area)              # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(base, height)}cm")   # provide suitable data matching your inputs
