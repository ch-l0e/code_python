def xyCoordinates(prompt):
    while True:
        coordinate = input(prompt)
        try:
            coordinate = float(coordinate)
        except:
            print("invalid input. please try again.")
        if coordinate != 0:
            return coordinate
        else:
            print("invalid input. please try again.")

x = xyCoordinates("Enter x coordinate: ")
y = xyCoordinates("Enter y coordinate: ")

if x > 0:
    if y > 0:
        print("1")
    else:
        print("4")
else:
    if y > 0:
        print("2")
    else:
        print("3")