#Create a calculator program
#minus, add, multiplication, division
#enter first number
#enter operator
#enter second number
#use if conditions

first = float(input("Enter first number: "))
operator =(input("Enter operator(+,-,*,/): "))
second = float(input("Enter second number: "))

if operator == "+":
    print( "Answer is",first + second)
elif operator == "-":
    print( "Answer is",first - second)
elif operator == "*":
    print( "Answer is",first * second)
elif operator == "/":
    print( "Answer is",first / second)
else :
    print("Invalid operator")










