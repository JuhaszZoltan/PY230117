from random import randint

# CIKLUSOK

# előre meghatározott lépésszámú ciklus
# [pythonban ún. "bejáró" ciklus]

#                      0         1        2       3
nevek:list[str] = ['Tercsi', 'Fercsi', 'Kata', 'Klára']

for nev in nevek:
    print(f'{nev} {randint(160, 190)} cm magagas')

nevem:str = 'Juhász Zoltán'

for i in range(10):
    print(f'{i}.: {nevem}')

for n in range(-10, 11, 2):
    print(f'{n}', end=' ')
print('\n------------')

# feltételes ciklus

x:int = 10
while x < 100:
    print(f"x:={x}")
    x += 10

print('vége')