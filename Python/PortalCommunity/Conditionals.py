devsMoney = 100
devCanPlaySmash = False

if devsMoney > 10 and devCanPlaySmash:
    print("Dev enters a smash tornament!")
elif devsMoney < 1 and devCanPlaySmash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")

mark = int(input("Enter your mark: "))
if mark >= 85:
    print("Distinction")
elif mark >= 65 and mark < 85:
    print("Pass")
else:
    print("Fail")