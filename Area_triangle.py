# Area of triangle by taking user input.
A = int(input("Enter first side:"))
B = int(input("Enter second side:"))
C = int(input("Enter third side:"))
S = (A+B+C)/2
Area = (S*(S-A)*(S-B)*(S-C)) ** 0.5
print("Area of triangle is",Area)
