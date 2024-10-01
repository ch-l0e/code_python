def triangle(prompt):
    while True:
        angle = input(prompt)
        try:
            angle = float(angle)
            return angle
        except:
            print("invalid input. please try again.")

while True:
    angle1 = triangle("enter first angle: ")
    angle2 = triangle("enter second angle: ")
    angle3 = triangle("enter third angle: ")
    if angle1 + angle2 + angle3 != 180:
        print("Error. please try again.")
    else:
        break

if angle1 == angle2 and angle2 == angle3:
    print("equilateral")
elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
    print("isosceles")
else:
    print("scalene")