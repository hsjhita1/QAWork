## Checking for certain parameters

def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  elif weekday == True and vacation == False:
    return False
  elif weekday == False and vacation == True:
    return True
  else:
    return True
print("sleep_in")
print(sleep_in(True, False)) ## Change variables to alter program

def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  elif a_smile == False and b_smile == False:
    return True
  elif a_smile == False and b_smile == True:
    return False
  else:
    return False
print("monkey_trouble")
print(monkey_trouble(True, True)) ## Change variables to alter program

def parrot_trouble(talking, hour):
  if talking == True and (hour > 20 or hour < 7):
    return True
  else:
    return False
print("parrot_trouble")    
print(parrot_trouble(True, 7))

def pos_neg(a, b, negative):
  if negative == True:
    return (a < 0 and b < 0)
  else :
    return (a > 0 and b < 0) or (a < 0 and b > 0)
print("pos_neg")
print(pos_neg(1, -1, True))

## Checking if values equal each other
def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return 2 * (a + b)
print("sum_double")
print(sum_double(2, 2))

def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  else:
    return False
print("makes10")
print(makes10(9, 9))

## Check difference between 2 numbers
def diff21(n):
  if n < 21:
    return 21 - n
  elif n > 21:
    return 2 * (n -21)
  else:
    return 0
print("diff21")
print(diff21(11))

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
print("near_hundred")
print(near_hundred(90))

## String functions
def not_string(str): ## Adds the word not to the front of the string
  if str[:3] == "not" and len(str) >= 3:
    return str
  return "not " + str
print("not_string")
print(not_string("not"))

def missing_char(str, n): ## Deletes a character from the string
  front = str[:n]
  back = str[n + 1:]
  return front + back
print("missing_char")
print(missing_char("test", 2))

def front_back(str): ## Function switches first and last character
  if len(str) <= 1:
    return str
  unchanged = str[1: -1]
  return str[-1] + unchanged + str[0]
print("front_back")
print(front_back("frontBack"))

def front3(str):
  if len(str) < 3:
    return str + str + str
  else:
    front = str[:3]
    return front + front + front
print("front3")
print(front3("Python"))
