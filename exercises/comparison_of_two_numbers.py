"""
Create two variables, assign a value read from the keyboard to each one,
and indicate which of the two values is greater.
"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
    print(a, "is greater than", b)
elif b > a:
    print(b, "is greater than", a)
else:
    print("The numbers are the same")
