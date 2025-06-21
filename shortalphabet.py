alpha ='abcdefghijklmnopqrstuvwxyz'
print(len(alpha))
user = input("Enter your word: ")
for i in user:
    if i in alpha:
        print(alpha.index(i))
    else:
        print("Invalid operation")