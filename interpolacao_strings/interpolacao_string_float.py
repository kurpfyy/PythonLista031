valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349

# formatação apenas como valor float
print("Valor 1: {:f}".format(valor1))

# formatação float com decimal em 2 digitos
print("Valor 1: {:.2f}".format(valor1))
print("Valor 2: {:.2f}".format(valor2))
print("Valor 3: {:.2f}".format(valor3))

# formatação float com separador de milhares e decimal em 2 digitos
print("Valor 2: {:,.2f}".format(valor2))

#-------------------------
# formatação float, com total de 10 digitos *nmeors e ponto)m sebdo 2 decimais.
print("Valor1: {:10.2f}".format(valor1))
print("Valor2: {:10.2f}".format(valor2))
print("Valor3: {:10.2f}".format(valor3))

# semelhante ao anterior, mas preenche casas antes do ponto com zero quando necessario.

print("Valor1: {:010.2f}".format(valor1))
print("Valor2: {:010.2f}".format(valor2))
print("Valor3: {:010.2f}".format(valor3))