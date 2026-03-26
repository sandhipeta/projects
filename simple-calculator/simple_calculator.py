num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")


user_choice = input("Enter choice (1/2/3/4): ")

if user_choice == "1":
    print("Result =", num1+num2)
    
elif user_choice == "2":
    print("Result =", num1 - num2)

elif user_choice == "3":
    print("Result =", num1*num2)
elif user_choice == "4":
    if num2 !=0:
        print("Result =", num1/num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid input")