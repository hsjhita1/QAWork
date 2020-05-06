def double_char(str):
  result = ""
  for char in str:
    result = result + (char * 2)
  return result
print("\ndouble_char")
print(count_hi("Hello"))

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      count = count + 1
  return count
print("\ncount_hi")
print(count_hi("hihhhi"))

def cat_dog(str):
  catCount = 0
  dogCount = 0
  for i in range(len(str)-1):
    if str[i:i+3] == "cat":
      catCount = catCount + 1
    elif str[i:i+3] == "dog":
      dogCount = dogCount + 1
  if dogCount == catCount:
    return True
  return False
print("\ncat_dog")
print(cat_dog("catdog"))

def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == "co" and str[i+3] == "e":
      count = count + 1
  return count
print("\ncount_code")
print(count_code("cdoecodecdcode"))

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a[-len(b):] == b or b[-len(a):] == a:
    return True
  return False

def xyz_there(str):
  count = 0
  if str[0:3] == "xyz":
    return True
  for i in range(len(str)):
    if str[i+1:i+4] == "xyz" and str[i] != ".":
      return True
  return False
