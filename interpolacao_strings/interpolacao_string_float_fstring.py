valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349

# formatação apenas como valor float
print(f"Valor 1: {valor1:f}")

# formatação float com decimal em 2 digitos
print(f"Valor 1: {valor1:.2f}")
print(f"Valor 2: {valor2:.2f}")
print(f"Valor 3: {valor3:.2f}")

# formatação float com separador de milhares e decimal em 2 digitos
print(f"Valor 2: {valor2:,.2f}")

#-------------------------
# formatação float, com total de 10 digitos *nmeors e ponto)m sebdo 2 decimais.
print(f"Valor1: {valor1:10.2f}")
print(f"Valor2: {valor2:10.2f}")
print(f"Valor3: {valor3:10.2f}")

# semelhante ao anterior, mas preenche casas antes do ponto com zero quando necessario.

print(f"Valor1: {valor1:010.2f}")
print(f"Valor2: {valor2:010.2f}")
print(f"Valor3: {valor3:010.2f}")

valor4 = 0.7536

# Formatação float exibindo em percentual com decimal em 1 digito
print(f"Valor 4: {valor4:.1%}")

# Incluindo R$ antes do valor e substituindo a vírgula do milhar por underline
texto_valor2 = f"R$ {valor2:_.2f}"
print(f"Texto Valor 2: {texto_valor2}")

texto_valor_br = texto_valor2.replace(".",".").replace("_",".")
print(f"Texto Valor BR: {texto_valor_br}")