#  This is My Operators Learning Project 
#  I am Going to Create a Simple Calulator wich will take 2 number from User and Calculate it on operation.

num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))
opr = input("Enter Operation + , - , * , / :  ")


if opr == "+" :
    print("Addition of Number is : " , num_1 + num_2)
elif opr == "-" :
    print("Subtraction of Number is : " , num_1 - num_2)
elif opr == "*" :
    print("Multiplication of Number is : " , num_1 * num_2)
elif opr == "/" :
    print("Division of Number is : " , num_1 / num_2)
else:
    print(" Invalid Input ! ")