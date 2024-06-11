class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


# Código principal
def main():
    clima_semanal = ClimaDiario()
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima_semanal.ingresar_temperatura(temp)

    promedio = clima_semanal.calcular_promedio()
    print(f"La temperatura promedio de la semana es: {promedio:.2f}")


if __name__ == "__main__":
    main()
