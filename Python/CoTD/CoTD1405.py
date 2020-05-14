import random

numbers = []
for i in range(0, 5):
    number = random.randrange(100, 201, 2)
    numbers.append(number)
print(numbers)