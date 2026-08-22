salary = int(input("Please Enter Your Salary: "))

ensurance = salary * 0.07
tax = salary * 0.10
salary = salary - (tax + ensurance)

print(f"Your Ensurance Bill is {ensurance}.")
print(f"Your Tax Bill is {tax}.")
print(f"Your Income Salary is {salary}.")