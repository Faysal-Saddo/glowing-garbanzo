import random

name = input()
names_list = name.split(",")#splits on "," and splits the value into a list
a = len(names_list)
biller = random.randrange(0,a) 
print(names_list[biller])
print(biller)