import math

def fenceLength(prompt):
    fence = input(prompt).upper()
    return fence

section1 = fenceLength("Using 'F' to denote each fence, enter length in first section: ")
section2 = fenceLength("Using 'F' to denote each fence, enter length in second section: ")
section3 = fenceLength("Using 'F' to denote each fence, enter length in third section: ")

fence = len(section1) + len(section2) + len(section3)
paint_bought = (math.ceil(fence / 12)) * 12
paint_left = fence - paint_bought
cost = paint_bought / 12 * 14.95

print(f"Total Paint Cans Bought: {paint_bought}")
print(f"Paint Cans Leftover: {paint_left}")
print(f"Cost: ${cost}")