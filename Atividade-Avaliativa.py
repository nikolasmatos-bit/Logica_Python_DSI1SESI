# Projeto EcoSort - Express-Cargo

pesos = []
fretes = []

total_peso = 0
total_frete = 0

for i in range(10):
    print(f"\nPacote {i + 1}")

    # Validação do peso
    while True:
        peso = float(input("Informe o peso do pacote (kg): "))

        if peso > 0:
            break

        print("Erro! O peso deve ser maior que zero.")

    # Validação do destino
    while True:
        destino = input("Destino (N = Nacional | I = Internacional): ").upper()

        if destino == "N" or destino == "I":
            break

        print("Erro! Digite apenas N ou I.")

    # Cálculo do frete
    if peso <= 2:
        categoria = "Leve"
        frete = 10.00

    elif peso <= 10:
        categoria = "Padrão"
        frete = 20.00

    else:
        categoria = "Pesado"
        frete = 30.00

    # Acréscimo internacional
    if destino == "I":
        frete *= 1.20

    # Armazenamento nos vetores
    pesos.append(peso)
    fretes.append(frete)

    # Acumuladores
    total_peso += peso
    total_frete += frete

    print(f"Categoria: {categoria}")
    print(f"Frete: R$ {frete:.2f}")

# Relatório final
ticket_medio = total_frete / 10

print("\n========== RESULTADO FINAL ==========")
print("Total de pacotes:", len(pesos))
print(f"Carga total acumulada: {total_peso:.1f} kg")
print(f"Faturamento bruto do lote: R$ {total_frete:.2f}")
print(f"Ticket médio por pacote: R$ {ticket_medio:.2f}")
print("====================================")