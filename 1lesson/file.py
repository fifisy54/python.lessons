age = 10 #int (integer) целое число
name = "Sophia" #str (string) строка, любой набор символов в кавычках
pi = 3.14 #float число с плавающей точкой

print(age * pi) #умножение
print(age / 10) #деление
print(age - 21) #вычитание
print(age + age) #сложение
var1 = age + age / pi
print(var1)

var2 = name + " Nesterenko"
print(var2)
var3 = var2[4:10]
print(var3)

var4 = age > pi
print(var4)
var5 = age < pi
print(var5)

if age > pi:
    print("условие верно")
elif age < pi:
    print("условие не верно") 