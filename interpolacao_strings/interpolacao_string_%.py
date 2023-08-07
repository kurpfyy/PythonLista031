nome = "Carla Joaquina"
idade = 27
altura = 1.759

print(f"Tipo de var nome: {type(nome)}")
print(f"Tipo de var idade: {type(idade)}")
print(f"Tipo de var altura: {type(altura)}")


print("Nome: %s" % nome)
print("Idade: %d" % idade)
print("Altura: %.2f" % altura)
print("%s possui %d anos e tem %.2f de altura" % (nome, idade, altura))