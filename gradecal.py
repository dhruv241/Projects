marks = input("Enter your marks: ")
marks = int(marks)
if marks>=90:
    print("You're grade is A+")
elif marks>=80:
    print("You're grade is A")
elif marks>=70:
    print("You're grade is B")
elif marks>=60:
    print("You're grade is C")
elif marks>=50:
    print("You're grade is D")
elif marks>= 40:
    print("You're grade is E")
elif 0 <= marks <= 40:
    print("You have failed")
else:
    print("Enter valid marks")
