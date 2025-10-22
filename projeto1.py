#SIstema de Caixa Simples
print("Bem Vindo à Loja DaniVerso")

produtos = []

while True:
    product = input("Enter the product name (or 'sair' to finish): ")
    if product.lower() == "sair":
        print("Thank you for preference!")
        break
    price = float(input("Enter the price: "))

    print("Product Purchased:\n"
          f"{product} - R${price:.2f}")
    print("Product Added!")

