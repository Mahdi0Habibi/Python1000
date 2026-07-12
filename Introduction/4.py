from math import pi,tan

sides_count = int(input("Please Enter Count of Sides: "))
sides_length = int(input("Please Enter Length of Sides: "))

polygon_area = (sides_count*((sides_length**2))/(4 * tan(pi/sides_count)))

print(f"Polygon Area is: {polygon_area}")