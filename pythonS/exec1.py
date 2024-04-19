num = int(input("Digite um numero: "))

divisores = 0

for div in range(1, num +1):
    if num % div == 0:
        divisores = divisores +1

if divisores == 2:
    print(f"{num} é um numero primo")
else:
    print(f"{num} Não é um numero")