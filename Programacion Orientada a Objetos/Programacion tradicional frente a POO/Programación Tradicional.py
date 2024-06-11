# Función para ingresar datos diarios de temperaturas
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Código principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"La temperatura promedio de la semana es: {promedio:.2f}")

if __name__ == "__main__":
    main()
