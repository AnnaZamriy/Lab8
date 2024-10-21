from array import*
import random

a = int(input("Введіть перший діапозон:"))
b = int(input("Введіть кінцевий діапозон:"))

masiv = array('i', [random.randint(a, b) for i in range(12)])
print(masiv)