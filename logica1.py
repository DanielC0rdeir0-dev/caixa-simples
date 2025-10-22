# nome = "Daniel"
# idade = "25"
# peso = int(74)
# altura = float(1.70)

# print(nome, idade, peso, altura)

# resposta = bool(input("Está estudando?: (sim/nao) "))

# if resposta == "sim":
#     estudando = True
# else:
#     estudando = False

# print("está estudando?: ",estudando)
## Exercicio 7
# lista = []

# for i in range(3):
#     nome = input("Enter a name?: ")
#     lista.append(nome)

# print("\nThe name you entered are: ")
# for nome in lista:
#     print(nome)

idades = []
for i in range(5):
    idade = int(input("Enter an age: "))
    idades.append(idade)

print("\nThe ages you entered: ")
for idade in idades:
    print(idade)

maior = max(idades)
menor = min(idades)

print(f"The oldest age is: {maior}")
print(f"The youngest age is: {menor}")

media = sum(idades) / len(idades)

oldest = 0
for idade in idades:
    if idade >= 18:
        oldest += 1

print(f"The media of ages are:{media:.2f}")
print((f"Number people over 18: {oldest}"))
