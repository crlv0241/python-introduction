import sys

print("Welcome to division calculator")

try:
  number1 = int(input("Enter Divedend:"))
  number2 = int(input("Enter Divisor:"))
except ValueError:
  print("Error: Invalid Input")
  sys.exit(1)

try:
  quotient = number1/number2
except ZeroDivisionError:
  print("Error: cannot devide by 0")
  sys.exit(1)

print(f"Result : {number1}/{number2} = {quotient}")