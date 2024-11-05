
def q1():
  #Write Assignment code here

  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  #Write Assignment code here

  integer1 = input("Input an integer: ")
  bool1 = (int(integer1) > 0)
  print(bool1)

def q3():
  #Write Assignment code here

  number1 = input("Enter a number: ")
  bool1 = (int(number1) > 0 and int(number1) < 10)
  print(bool1)

def q4():
  #Write Assignment code here

  food1 = input("Input food: ")
  drink1 = input("Input drink: ")
  bool1 = not(food1 == "pizza" and drink1 == "pop")
  print(bool1)

def q5():
  #Write Assignment code here

  integer1 = int(input("Enter an integer: "))
  bool1 = integer1 % 2 == 0
  print(f"The integer {num1} is {bool1}")

#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()
