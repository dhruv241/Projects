print("\t\t\t\t\t\tCALCULATOR")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = input("Select your operator: +,-,/,* : ")
if c == '+':
      d = a + b
      print("Your sum is ",  str(d))
elif c == '-':
      e = a - b
      print("Your subtraction is " , str(e))
elif c == '/':
      f = a/b
      print("Your division is ", str(f))
elif c == '*':
      g = a*b
      print("Your multiplication is " , str(g))
else:
      print('Invalid operator')
