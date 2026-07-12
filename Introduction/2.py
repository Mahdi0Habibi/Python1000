pi = 3.14

height = float(input("Please Enter Height: "))
radius = float(input("Please Enter Radius: "))

TotalArea = 2*pi*radius*height + 2*pi*(radius**2)
Volume = height*(radius**2)*pi

print(f"Total Area is: {TotalArea}")
print(f"Volume is: {Volume}")

