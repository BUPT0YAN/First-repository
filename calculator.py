def add(num1:int, num2:int):
    return num1 + num2

def subtract(num1:int, num2:int):
    return num1 - num2

def multiply(num1:int, num2:int):
    return num1 * num2

def divide(num1:int, num2:int):
    return num1 / num2

def calculator():
    print("Select operation:")
    print("1.Add")
    print("2.subtract")
    print("3.multiply")
    print("4.calculator")
    while True:
        choice = input("Enter chioce (1/2/3/4)")
 
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))

        if choice == "1":
            print("Result:", add(num1,num2))
              
        elif choice == "2":
            print("Result:", subtract(num1,num2))
              
        elif choice == "3":
            print("Result:", multiply(num1,num2))
              
        elif choice == "4":
            print("Result:", divide(num1,num2))
       
        else:
            print("Invalid input, try again")
        
        flag = input("Continue?(Y/N)")
        if flag == 'N' or flag == 'n':    
            break
 
calculator()
            


    
