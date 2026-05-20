# EX1
# O usuário digitou "25" como sua idade em um formulário.
# Converta para inteiro e calcule a idade que ele terá
# daqui a 5 anos.

Idade = 25 + 5

print("Idade daqui 5 anos será", Idade)


# EX2
# Converta o número de ponto flutuante 7.999
# para inteiro e observe o resultado.

numero = int(7.999)

print("Número convertido:", numero)
print("Tipo da variável numero:", type(numero))


# EX3
# Converta a string "-3.14" para float
# e multiplique o resultado por 2.

valor = float("-3.14")

print("Resultado:", valor * 2)
print("Tipo da variável valor:", type(valor))

# EX4
# Tente converter a string "cento e vinte"
# para inteiro e observe o que acontece.

# print(int("cento e vinte"))
# Vai gerar erro porque a string não representa um número.


# EX5
# Converta o número 42 para string
# e concatene com a palavra " respostas".

texto = str(42) + " respostas"

print(texto)
print("Tipo da variável texto:", type(texto))


# EX6
# Use a função complex() para criar
# um número complexo com parte real 3
# e parte imaginária 5.

numero_complexo = complex(3, 5)

print(numero_complexo)
print("Tipo da variável numero_complexo:", type(numero_complexo))


# EX7
# Converta o número 0 para booleano
# e mostre o resultado.

resultado_bool_0 = bool(0)

print(resultado_bool_0)
print("Tipo:", type(resultado_bool_0))


# EX8
# Converta o número -100 para booleano
# e mostre o resultado.

resultado_bool_neg = bool(-100)

print(resultado_bool_neg)
print("Tipo:", type(resultado_bool_neg))


# EX9
# Converta o número 3.1415 para inteiro
# e depois para string, tudo em uma única linha.

resultado = str(int(3.1415))

print(resultado)
print("Tipo:", type(resultado))
# EX10
# Some um número inteiro (5) com um float (2.3)
# e verifique qual é o tipo do resultado.

resultado = 5 + 2.3

print("Resultado:", resultado)
print("Tipo:", type(resultado))
