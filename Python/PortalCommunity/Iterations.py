## While loop

number = 0
while number < 5:
    print(number)
    number += 1

## For loop
for i in range(51): ## Will print from 0 - 50
    print(i)

animals = ["cow", "pig", "duck"] ## Can also print lists
for animal in animals:
    print(animal)

## Breaking a loop
for i in range(101):
    print(i)
    if i == 20:
        break ## Once i = 20, the loop will break

## Nested loops
for i in range(3): ## Will increment once for loop below has been done
    for j in range(4): 
        print(i, "x", j, "=", i*j)

## Incrementing custom value
for i in range(10,21,2): ## Will increment by 2
    print(i)