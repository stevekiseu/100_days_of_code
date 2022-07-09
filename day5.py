4#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
let_num = len(letters) - 1
l_pass = ""

for l in range(0,(nr_letters)):
  l_rand = random.randint(0, let_num)
  l = letters[l_rand]
  l_pass += l

sym_num = len(symbols) - 1
s_pass = ""

for s in range(0,(nr_symbols)):
  s_rand = random.randint(0, sym_num)
  s = symbols[s_rand]
  s_pass += s

num_num = len(numbers) - 1
n_pass = ""

for n in range(0,(nr_numbers)):
  n_rand = random.randint(0, num_num)
  n = numbers[n_rand]
  n_pass += n
password = (l_pass + s_pass + n_pass)
rpass = "".join(random.sample(password, len(password)))
print("Here is your password: " + rpass)