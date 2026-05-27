import sys

num = int(input("Enter a number: "))

if num < 0:
    print("Negative number not allowed")
    sys.exit()

print("Valid number")
