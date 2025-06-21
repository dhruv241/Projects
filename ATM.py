print("\t\t\t\t\t\t SBI BANK")
amount = 40000
pin = 2411
if 'card'== input("Insert your card: "):
    print("Welcome")
    if pin == int(input("Enter your pin: ")):
         la = input("\t\t\t\t\t\t a. Check balance\n \t\t\t\t\t\t b. Withdraw balance\n \t\t\t\t\t\t Answer: ")
         la = la.lower()
         if la == 'a':
             print("\t\t\t\t\t\tYour balance is ", amount)
         elif la == 'b':
             money = int(input("Enter your amount: "))
             if money <= amount:
                 amount = amount - money
                 print("Withdrawl successful, your remaining balance is", str(amount))
             elif money > amount:
                 print("Not enough funds")
         else:
             print("Invalid option")
    else:
        print("Invalid pin")
            
             
else:
    print("Invalid card")