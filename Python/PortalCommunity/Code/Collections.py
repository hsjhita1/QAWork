## [] creates a list
cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

## Multi-dimensional lists
cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_animals[2][2]) ##Prints Hogwarts
print(cool_animals[0][1]) ##Prints Moolan

## Lists can contain multiple data types
farm = ["Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850]

animals = ["dog", "cat"]
animals.append("cow") ## Append adds an item to the list
print(animals)
animals.remove("cat") ## Remove removes an item from the list
print(animals)
animals.reverse() ##Reverses the order of the list
print(animals)
animals.count("cow") ##Counts the occurences of the item in the list

## Dictionary of books, defined by {"key" : "value"}
## Left hand side is the key, right hand side is the value
## Books are the key, values are the author
books = {"Harry Potter":"J.K. Rowling", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books['Harry Potter'])
print(books['The Hobbit'])
books["The Martian"] = "Andy Weir" ##Creates a new KVP with key 'The Martian' with value 'Andy Weir'
print(books)
print(books.keys()) ##Prints the keys in the dictionary
print(books.values()) ##Prints the values in the dictionary