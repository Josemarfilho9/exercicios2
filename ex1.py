contador = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        contador += 1

print("Quantidade:", contador)
