import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]

print("\t\tPyPASSWORD GENERATOR PROGRAM\t\t")
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you want in your Password\n"))
nr_numbers = int(input("How many symbols would you like\n"))
nr_symbols = int(input("How many symbols would you like\n"))

password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for symb in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Here is your password : {password}")
