# AULA COMPLETA: NUMEROS EM PYHTON

    # """
    # Vamos Aprender:
    # 1 - Tipos Numéricos 
    # 2 - Conversões de Tipos
    # 3 - Hierarquia Númérica 
    # 4 - Operações Matemáticas
    # 5 - Coerção de Tipos
    # 6 - Verificação de Tipos 
    # 7 - Entrada de Dados
    # """
##############################
 ## PASSO 01 - TIPOS NUMÉRICOS 
##############################
# int -> Números inteiros
# float -> Números com casas decimais
# complex -> Númeeros complexos (usado em Matemática/engenharia)

print("===== TIPOS NUMÉRICOS =====")
 # EXEMPLO 01 - NUMERO INTEIRO 

 #criamos uma varíavel chamada número inteiro
numero_inteiro = 10

#Mostramos o valor
print ("Valor:", numero_inteiro)
#Type() mostra qual é o tipo da variável
print("TIPO:", type (numero_inteiro))

print("-------------------------")

# EXEMPLO 02 - NUMERO DECIMAL

numero_decimal = 3,14

print ("valor , numero_decimal")
print ("Tipo", type(numero_decimal))


print ("--------------------")

# EXEMPLO 03 - NUMEROS COMPLEXOS 
# um número complexo possui duas partes:
# parte real (Numero Real)
# Parte Imaginária (multiplicado por J)

# Estrutura Geral:
# Numero = a + bj 

# a = parte real
# b = parte imaginária 
# j = unidade imaginária 

numero_complexo = 2 + 3j

print("Valor", numero_complexo)
print("Tipo", type(numero_complexo))

print("--------------------")

# EXEMPLO 03 - ACESSANDO CADA PARTE DO NUMERO
# .real retorna a parte real
print("parte real", numero_complexo.real)

# .imag retorna a parte imaginária
print("parte imaginária", numero_complexo.imag)

# APENAS PARA SEPARAR VISUALMENTE A SAÍDA NO TERNMINAL
print("\n\n")

#######################
## PASSO 02 - CONVERSÃO TIPOS
#######################

# EXEMPLO CLÁSSICO:
# Dados vindos do usuário são texto (string), muitas vezes 

print("======== converções ========")

# float -> int

valor = int(3.9)

print("int(3,9):" , valor)
print("Tipo:" ,  type(valor))

#sting -> int
valor1 = "10"
print(type(valor))

valor2 = int ("10")
print = ('int("10"):', valor2)
print = ("tipo" , type(valor2))


#int --> Float 
valor3 = float(10)
print("float(10):" , valor3)
print("tipo:", type(valor3))
