present_price = int(input("Please Enter The present Price of the Product: "))
previous_price = int(input("Please Enter The previous Price of the Product: "))

Inflation = float((present_price - previous_price) / previous_price)
future_price = int(previous_price + (present_price * Inflation))

print(f"Inflation of the product is {Inflation}")
print(f"Future Price of the product is {future_price}")
