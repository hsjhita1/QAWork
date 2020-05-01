def uniqueSum(num1, num2, num3):
    temp1 = num1
    temp2 = num2
    temp3 = num3
    if temp1 == temp2:
        num1 = 0
        num2 = 0
    if temp1 == temp3:
        num1 = 0
        num3 = 0
    if temp2 == temp3:
        num2 = 0
        num3 = 0
    return num1 + num2 + num3

print(uniqueSum(1, 2, 3))
print(uniqueSum(3, 3, 3))
print(uniqueSum(1, 1, 2))