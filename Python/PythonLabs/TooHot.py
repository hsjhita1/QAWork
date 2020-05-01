def tooHot(temperature, isSummer):
    if isSummer:
        if temperature >=60 and temperature <=100:
            return True
        elif temperature <60 or temperature >100:
            return False
    else:
        if temperature >=60 and temperature <=90:
            return True
        elif temperature <60 or temperature >90:
            return False


summer = True
temperature = int(input("Enter a temperature: "))
print(tooHot(temperature, summer))