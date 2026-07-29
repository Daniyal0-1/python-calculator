#print pyhton calculator

print ( " Calculator ")
#getnumbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
#getchoice
print ( "\nChoose an operation : ")
print ( " 1. Sum")
print ( " 2. Subtract")
print ( " 3. Multiply")
print ( " 4. Divide")
choice = input( " According to your choice , press 1/2/3/4 ")

if ( choice == "1" ):
    sum = a + b
    print ( "Sum : " , a , " + " , b , " = ", sum )
elif ( choice == "2" ):
    sub = a - b
    print ( "Sub : " , a , " - " , b , " = " ,  sub )
elif ( choice == "3" ):
    mul = a * b
    print ( "Mul : ", a , " * " , b , " = " ,  mul )
elif ( choice == "4" ):
    if b != 0:
        div = a / b
        print ( "Div : ", a , " / " , b , " = " ,  div )
    else:
        print ( "Division by zero is not possible")
else:
    print ( "Error !! Wrong Choice , Rerun the program to try again." )


