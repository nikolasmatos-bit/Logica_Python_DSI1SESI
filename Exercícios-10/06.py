# ==========================================
# ETAPA 1 - Valores definidos no código
# ==========================================

salario = 3000.00
taxa_imposto = 10  # em %

valor_imposto = salario * (taxa_imposto / 100)
salario_final = salario - valor_imposto

print("=== ETAPA 1 ===")
print(f"Salário: R$ {salario:.2f}")
print(f"Taxa de imposto: {taxa_imposto}%")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")

# ==========================================
# ETAPA 2 - Dados informados pelo usuário
# ==========================================

print("\n=== ETAPA 2 ===")

salario = float(input("Digite o salário: R$ "))
taxa_imposto = float(input("Digite a taxa de imposto (%): "))

valor_imposto = salario * (taxa_imposto / 100)
salario_final = salario - valor_imposto

print("\n=== RESULTADO ===")
print(f"Salário informado: R$ {salario:.2f}")
print(f"Taxa de imposto: {taxa_imposto:.2f}%")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Salário após desconto: R$ {salario_final:.2f}")