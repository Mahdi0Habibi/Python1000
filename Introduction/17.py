amount = int(input("Please Enter Current Amount: "))
rate = float(input("Please Enter Rate: "))
count = int(input("Please Enter Year Count"))

future_value = amount * ((1+(0.01*rate))** count)

print(f"Future Value is {future_value}")