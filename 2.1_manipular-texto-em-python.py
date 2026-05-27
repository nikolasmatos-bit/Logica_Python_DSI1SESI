# AULA COMPLETA - STRING EM PYTHON

# - Criação de Strings 
# - Strings multilinha
# - Indices e slices 
# - Operações com Strings 
# - Imutabalidade
# - Métodos úteis 
# - Formatação de Texto 
# - Unicode e Bytes

#-------------------------------------------
# 1) CRIAÇÃO DE STRINGS 
#-------------------------------------------
# String são textos em python
#Podem ser criadas usando aspas simples ou duplas

texto1 = "pyhton"
texto2 = 'curso de python'
texto3 = "Copa 'Padrão fifa'" 
texto4 = 'Copa "Padrão FIFA"'

print(texto1, texto2, texto3, texto4)


# Python permite misturar aspas simples e duplas, dentro das strings sem precisar escapar caracteres

#-----------------------------------------------
# 2) STRINGS MULTILINHA
#-----------------------------------------------

# Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\
uso: programa [OPÇÕES]
-H Exibe Ajuda 
-U Url do dataset
"""
print(menu)

# - Esses formatos é muito usado para:
# - Menus 
# - Documentação 
# - textos longos 

#-----------------------------------------------
# 3) Concataneção Automática 
#-----------------------------------------------
# Quando duas strings aparecem lado a lado, juntam automaticamente 

texto = ("copa" "2026 " "Neymar é show mesmo" "SIM")
print(texto)

#-----------------------------------------------
# 4) STRINGS COMO SEQUêCIAS 
#-----------------------------------------------
# Uma string funciona como uma sequÊncia de carcteres, Cada caractere possi um indice 

st = "Maracanã"
print ("Primeira Letra:", st[0])
# Só exibir a letra: m

print("ultima Letra:", st[-1])

print ("Trecho 1:4:", st[1:4]) 

print("do inicio até 3:",st[:3])

print("Do 2 até o fim", st[2:1])

print ("Tamanho", len(st))

#-----------------------------------------------
# 5) OPERAÇÕESS COM STRINGS
#-----------------------------------------------
# python permite várias operações com strings

print("m" in st)
print("M" in st)
# Significa que a letra "m" existe dentro a string

print("x" not in st)
# Significa que "x" não existe na string 

print ("m" * 3)
# Multiplicação repete a string 

print("m" + "aracanã") 
# Operador + concatena strings

#-----------------------------------------------
# 6) STRINGS SÃO INUTÁVEIS
#-----------------------------------------------
# Strings não podem ser alteradas diretamente!!
# isso significa quew o conteúdo original não muda
# o que acontece é a criação de uma nova string

texto5 = "python 3" 

# Método replace cria uma nova string 
texto5 = texto.replace("3", "2") 

print(texto5) 

#----------------------------------------------
# 7) MÉTODOS IMPORTANTES 
#-----------------------------------------------
# Strings possuem vários métodos úteis. 
 
cidade = "maracana" 
# Coloca a primeira letra em maiúscula. 
print(cidade.capitalize()) 

# conta quando vezes "a" aparece
print(cidade.count("a"))

# Verificar se começa com "m"
print(cidade.startswith("m")) 

# Verifica se termina com "z" 
print(cidade.endswtich("z")) 

frase = "copa do mundo 2002" 

# Divida a string em uma lista 
print(frase.split(" ")) 

#----------------------------------------------
# 8) FORMATAÇÃO DE STRINGS 
#----------------------------------------------