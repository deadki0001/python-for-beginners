import math
# Write your code below this line

def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You will need {cans} cans of paint")    

# Write your code above this line

# Dont change the code below

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

