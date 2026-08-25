A4 = int(input("Please Enter A4 Price: "))
pen = int(input("Please Enter Pen Price: "))
Inflation = float(input("Please Enter Inflation Rate: "))
Inflation /=100
Cost = ((pen * 150 * Inflation)) + (A4*50*Inflation)
print(f"Extra Cost is {Cost}")
