<<<<<<< HEAD
#SIstema de Caixa Simples
print("Bem Vindo à Loja DaniVerso")

produtos = []
total = 0
while True:
    #Inserir produto ou terminar progama
    product = input("Enter the product name (or 'sair' to finish): ")
    
    if product.lower() == "sair":
        print("Thank you for preference!")
        break
    #Inserir preço
    price = float(input("Enter the price: "))
    #Lista de produto e preço
    print("Product Purchased:\n"
          f"{product} - R${price:.2f}")
    print("Product Added!\n")

    #Guarda nome e preço
    produtos.append((product, price))
    total += price

print("\n === Purchase Summary ===")
#Mostra os itens dentro da lista
for item in produtos:
    print(f"{item[0]} - R${item[1]:.2f}")
#total
print(f"Total:  R${total:.2f}")
#Produtos adicionados ao final
print(f"{len(produtos)} products added.")


=======
#SIstema de Caixa Simples
print("Bem Vindo à Loja DaniVerso")

produtos = []
total = 0
while True:
    #Inserir produto ou terminar progama
    product = input("Enter the product name (or 'sair' to finish): ")
    
    if product.lower() == "sair":
        print("Thank you for preference!")
        break
    #Inserir preço
    price = float(input("Enter the price: "))
    #Lista de produto e preço
    print("Product Purchased:\n"
          f"{product} - R${price:.2f}")
    print("Product Added!\n")

    #Guarda nome e preço
    produtos.append((product, price))
    total += price

print("\n === Purchase Summary ===")
#Mostra os itens dentro da lista
for item in produtos:
    print(f"{item[0]} - R${item[1]:.2f}")
#total
print(f"Total:  R${total:.2f}")
#Produtos adicionados ao final
print(f"{len(produtos)} products added.")


>>>>>>> c4c1b064acefb81288c78a995e79829f6ccb69fe
