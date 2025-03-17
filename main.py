print ("Mini Calculator")

num1 = float (input("enter 1st number here: "))
num2 = float (input("enter 2nd number here: "))
print ("press + for addition \npress - for substraction \npress * for multiplication \npress / for division")
choice = (input("enter your choice of arithmatic symbol: "))
if choice == '+': 
    print("Answer::", num1 + num2)
elif choice == '-':
    print("Answer:", num1 - num2)
elif choice == '*':
    print("Answer:", num1 * num2)
elif choice == '/':
    if num2 != 0:
        print("Answer:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print("Invalid choice. Please enter a valid arithmetic symbol.")        