import module

print("Menu")
print("--------------")
print("1. add")
print("2. sub")
print("3. multiply")
print("4. divide")
print("5. stop")

print(":", end = " ") 
n = int(input())

if n == 1:
    print("num1 : ", end = " ")
    num1 = int(input())
    print("num2 : ", end = " ")
    num2 = int(input())
    print("Added result = ", end = " ")
    print(module.add(num1,num2))
    print("Calculation done :)")
elif n == 2:
    print("num1 : ", end = " ")
    num1 = int(input())
    print("num2 : ", end = " ")
    num2 = int(input())
    print("Submitted result = ", end = " ")
    print(module.sub(num1,num2))
    print("Calculation done :)")
elif n == 3:
    print("num1 : ", end = " ")
    num1 = int(input())
    print("num2 : ", end = " ")
    num2 = int(input())
    print("Multiplied result = ", end = " ")
    print(module.mul(num1,num2))
    print("Calculation done :)")
elif n == 4:
    print("num1 : ", end = " ")
    num1 = int(input())
    print("num2 : ", end = " ")
    num2 = int(input())
    if num1 or num2 == 0:
        print("Invalid input")
    else:    
        print("Divided result = ", end = " ")
        print(module.div(num1,num2))
        print("Calculation done :)")
elif n == 5:
    print("Stop")
else : 
    print("Try other Menu :p")
