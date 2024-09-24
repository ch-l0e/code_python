import math

while True:
    tiles = input("Enter number of tiles: ")
    try:
        tiles = float(tiles)
        break
    except:
        print("Invalid input. Please try again.")

square = math.floor(math.sqrt(tiles))
print(f"The largest square has side length {square}")