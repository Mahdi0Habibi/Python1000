r1 = int(input("Please Enter First Resistance: "))
r2 = int(input("Please Enter Second Resistance: "))
r3 = int(input("Please Enter Third Resistance: "))

total = (1/r1) + (1/r2) + (1/r3)
result = 1/total

print(f"Final Resistance is {result}.")