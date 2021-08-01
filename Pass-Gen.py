import random

lower = "abcdefghijklmnopqrstuvwxyzç" # Em algumas aplicaçãoes, não é permitido o "ç".
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ"  # Em algumas aplicaçãoes, não é permitido o "Ç".
numbers = "0123456789"
symbols = "[]{}()!@#$%&*-+=:;.,"    # Em algumas aplicaçãoes, não é permitido alguns caracters.
numbers = "0123456789"

all = lower + upper + numbers + symbols
length = 16 # O valor pode ser alterado para quantos caracters quiser
password = "".join(random.sample(all, length))

print(password)
