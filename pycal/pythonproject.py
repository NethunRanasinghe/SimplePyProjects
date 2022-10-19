# Python calculater

# Add Function
def add(x, y):
    return x + y

# Subtraction Function
def subtract(x, y):
    return x - y

# Multiplication function
def multiply(x, y):
    return x * y

# Divide Function
def divide(x, y):
    return x / y


print("Select an operation : \n")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplycation")
print("4.Division\n")

while True:
    # user input
    inpt = input("Enter an input : ")

    # check if the input is valid
    if inpt in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if inpt == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif inpt == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif inpt == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif inpt == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # checking the user wants another calculation if not break the loop
        cal_nxt = input("You want to perform another calculation : (yes/no): ")
        if cal_nxt == "no":
          break
    
    else:
        print("Invalid Input")