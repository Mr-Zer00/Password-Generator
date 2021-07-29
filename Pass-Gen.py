import random

lower = "abcdefghijklmnopqrstuvwxyzç"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()!@#$%&*-+=:;.,"

all = lower + upper + numbers + symbols
length = 16 # O valor pode ser alterado para quantos caracters quiser
password = "".join(random.sample(all, length))

print(password)
