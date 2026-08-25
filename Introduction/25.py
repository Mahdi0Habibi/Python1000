CurrentSpeed = int(input("Please Enter Current Speed: "))
PrimarySpeed = int(input("Please Enter Primary Speed: "))
Nminutes =  int(input("Please Enter The Number Of Minutes: "))
Acceleration = (CurrentSpeed-PrimarySpeed)*60/Nminutes
print(f"The Acceleration is {Acceleration} .")
