import cmath
import array

userString = str(input("Input string: "))
strArray = userString.split(' ')

print(strArray)

char = strArray[1]
num1 = int(strArray[0])
num2 = int(strArray[2])

print (char, ', ', num1, ', ', num2)


if char == '+':
    print('result: ', num1+num2)
elif char == '-':
    print('result: ', num1-num2)
elif char == '*':
    print('result: ', num1*num2)
elif char == '/':
    print('result: ', num1+num2)
