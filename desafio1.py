# n = int(input('Digite uma nota, entre zero e dez: '))
# while n > 10 or n < 0:
#     n = int(input("Errou, tente dnv: "))
# print("boa")

user = input("Digite o usuario: ")
senha = input("Digite a senha: ")

for senha in user:
    print("Tente novamente")
    user = input("Digite o usuario: ")
    senha = input("Digite a senha: ")