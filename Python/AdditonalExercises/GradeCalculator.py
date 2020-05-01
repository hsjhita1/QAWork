print("Welcome to Grade Calculator")
maths = int(input("Please enter your maths mark: "))
chemistry = int(input("Please enter your chemistry mark: "))
physics = int(input("Please enter your physics mark: "))
overall = (maths + chemistry + physics)/3
print("\nYour percentage score is: ", overall, "%" )
if overall >= 70:
    print("You scored a grade of: A")
elif overall >= 60:
    print("You scored a grade of: B")
elif overall >= 50:
    print("You scored a grade of: C")
elif overall >= 40:
    print("You scored a grade of: D")
else:
    print("You scored a grade of: You failed")
