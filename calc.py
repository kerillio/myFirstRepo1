import cmath
import array

userString = str(input("Input string: "))
strArray = userString.split(' ')

print(strArray)

char = strArray[1]
num1 = int(strArray[0])
num2 = int(strArray[2])


if char == '+':
    print('result: ', num1+num2)
elif char == '-':
    print('result: ', num1-num2)
elif char == '*':
    print('result: ', num1*num2)
elif char == '/':
    print('result: ', num1+num2)

#A simple calculator
class Calculator:
  #empty constructor
  def __init__(self):
    pass
  #add method - given two numbers, return the addition
  def add(self, x1, x2):
    return x1 + x2
  #multiply method - given two numbers, return the 
  #multiplication of the two
  def multiply(self, x1, x2):
    return x1 * x2
  #subtract method - given two numbers, return the value
  #of first value minus the second
  def subtract(self, x1, x2):
    return x1 - x2
  #divide method - given two numbers, return the value
  #of first value divided by the second
  def divide(self, x1, x2):
    if x2 != 0:
      return x1/x2