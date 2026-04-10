n = int(input("Digite um número inteiro positivo: "))

while n <= 0:
    n = int(input("Número inválido. Digite novamente: "))

soma = 0
expressao = ""

for i in range(1, n + 1):
    soma += i
    if i == n:
        expressao += str(i)
    else:
        expressao += str(i) + " + "

print(expressao + " = " + str(soma))