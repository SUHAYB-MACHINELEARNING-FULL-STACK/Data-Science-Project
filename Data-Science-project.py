# Task 1 

x = 7
y = x/3
z = x==7
s= "Hello python programmer!"
print(f"type of x: {type(x)}\ntype of y: {type(y)}\ntype of z: {type(z)}\ntype of s: {type(s)}\n")

# Task 2

quantity = 2
price = 10.5
text = f"I want to pay {price} riyals for {quantity} pieces of this item."
print(f"{text}\n")

# Task 3

def bigger_than_10(x):
  print(f"{x>10}\n")
bigger_than_10(19)

# Task 4

  # Task 4 - Level 1

fruites = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f"{fruites[-2:]}\n")
  # Task 4 - Level 2

[print(f"{i}\n") for i in fruites]

# Task 5

  # Task 5 - Level 1

colors = {
    "blue": "0000FF",
    "green": "00FF00",
    "yellow": "FFFF00",
    "red": "FF0000",
    "white": "unknown"
}

colors['black'] = '000000'

print(f"{colors}\n")

  # Task 5 - Level 2

colors['white'] = 'FFFFFF'

print(f"{colors}\n")

  # Task 5 - Level 3

def exchange_values(lista):
  print([colors[lista[i]] for i in range(len(lista))])
exchange_values(['blue', 'white', 'black', 'yellow', 'green', 'red'])  
