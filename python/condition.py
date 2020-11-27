print("Positive or Negative")
name = input("Enter your name:")
number = int(input("Enter a number:"))

print(f"Hello {name}")
if (number%2==0):
  print(f"The number {number} is even.")
else:
  print(f"The number {number} is odd.")