import math

Velocity = float(input("Please Enter Velocity in Km/h: "))
Temperature = float(input("Please Enter Temperature in Celsius Degrees: "))

wsi = (13.12) + (0.62158*Temperature) - (11.37*math.pow(Velocity,0.16))
+ (0.3965*Temperature*math.pow(Velocity,0.16))

print(f"The wind chill index is: {wsi}")