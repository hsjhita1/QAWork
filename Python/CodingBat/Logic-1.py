def cigar_party(cigars, is_weekend): # Returns true or false if conditions are matched
  if is_weekend == True:
    return cigars >= 40
  return cigars >= 40 and cigars <= 60
print("cigar_party")
print(cigar_party(45, True))

def date_fashion(you, date):
  if you <=2 or date <= 2:
    return 0
  elif you >=8 or date >= 8:
    return 2
  return 1
print("\date_fashion")
print(date_fashion(4, 8))

def squirrel_play(temp, is_summer):
    if is_summer == True:
      return 60 <= temp <= 100
    return 60 <= temp <= 90

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    speed = speed - 5
  if speed <= 60:
    return 0
  elif speed >= 61 and speed <= 80:
    return 1
  else:
    return 2

def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <=19:
    return 20
  return sum

def alarm_clock(day, vacation):
  if day >= 1 and day <= 5:
    if vacation == True:
      return "10:00"
    return "7:00"
  elif vacation == False:
    return "10:00"
  else:
    return "off"

def love6(a, b):
  if a == 6 or b == 6 or a + b == 6 or abs(a-b) == 6:
    return True
  return False

def in1to10(n, outside_mode):
  if outside_mode == True:
    if n <= 1 or n >= 10:
      return True
    return False
  else:
    if n >= 1 and n <= 10:
      return True
    return False

def near_ten(num):
  nearTen = [0, 1, 2, 8, 9, 10]
  for i in range(len(nearTen)):
    if num % 10 == nearTen[i]:
      return True
  return False
