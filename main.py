a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
fun = input("Enter the fun")

if fun == "add":
    print("the addition of two number is ",a+b)
elif fun == "sub" :
    print("the subtraction of two number is ",a-b)
elif fun == "mul" :
    print("the multiplication of two number is ",a*b)
elif fun == "div" :
    print("the division  of two number is ",a/b)
else :
    print("Invalid fun")
