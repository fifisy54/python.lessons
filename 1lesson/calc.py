command = input("введите команду:")
num1 = int(input("введите число 1:"))
num2 = int(input("введите число 2:"))

if command == "+":
    print(num1 + num2)
elif command == "*":
    print(num1 * num2)
elif command == "-":
     print(num1 - num2)

elif command == "/":
    print(num1 / num2)
else:
    print("комманда не найдена") 

