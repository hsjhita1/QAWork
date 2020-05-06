def hello_name(name):# Print Hello 'name'!retur
  return ("Hello " + name + "!")
print("hello_name")
print(hello_name("Harpreet"))

def make_abba(a, b): #Returning strings in abba order
  return a + b + b + a
print("make_abba")
print(make_abba("Hi", "Bye"))

def make_tags(tag, word): # Returning HTML tags
  return "<"+ tag + ">" + word + "</" + tag + ">"
print("make_tags")
print(make_tags("i", "Yay"))

def make_out_word(out, word): ## Surrounds word with out
  return out[:2] + word + out[-2:]
print("make_out_word")
print(make_out_word("<<>>", "Yay"))

def extra_end(str): #Return last 2 characters of a string 3 times
  if len(str) <=2:
    return str + str + str
  else:
    return str[-2:] + str[-2:] + str[-2:]
print("extra_end")
print(extra_end("Hello"))

def first_two(str):# Return first two characters of a string
  if str == "":
    return str
  elif len(str) <=2:
    return str
  else:
    return str[:2]
print("first_two")
print(first_two("Hello"))

def first_half(str):#Returns the first half of a string
  return str[:(len(str)/2)]
print("first_half")
print(first_half("WooHoo"))

def without_end(str):# Returnsa string without the first and last characters
  return str[1:-1]
print("without_end")
print(without_end("Hello"))

def combo_string(a, b): #Returns a short-long-short format
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a
print("combo_string")
print(combo_string("hi", "Hello"))

def non_start(a, b):#Returns strings without the first character
  return a[1:] + b[1:]
print("non_start")
print(non_start("Hello", "There"))

def left2(str): ##Returns a string with the first 2 characters at the end
  if len(str) <= 2:
    return str
  else:
    return str[2:] + str[:2]
print("left2")
print(left2("Hello"))



