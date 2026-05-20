# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.

ano = 2024
print(type(ano))


# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().

print(isinstance(3.14159, float))


# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.

print(type(100) == type(True))


# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.

print(isinstance(True, int))


# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().

resultado = 5 / 2

print(type(resultado))
print(isinstance(resultado, float))


# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.

def verificar_numero(valor):
    if isinstance(valor, (int, float, complex)):
        print("É número!")
    else:
        print("Não é número!")

verificar_numero(10)
verificar_numero(3.5)
verificar_numero(2 + 4j)
verificar_numero("Python")


# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.

print(type(True) == int)
print(isinstance(True, int))


# EX8
# Descubra o tipo do número 3+4j
# usando type().

numero = 3 + 4j
print(type(numero))


# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().

print(isinstance(None, type(None)))


# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.

numero = 3.0

print(isinstance(numero, (int, float, complex)))
print(isinstance(numero, int))