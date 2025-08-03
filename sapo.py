def calcular_jeitos_diferentes(pedras):
    if pedras <= 2:
        return pedras
    return calcular_jeitos_diferentes(pedras - 1) + calcular_jeitos_diferentes(pedras - 2)

print(calcular_jeitos_diferentes(5))