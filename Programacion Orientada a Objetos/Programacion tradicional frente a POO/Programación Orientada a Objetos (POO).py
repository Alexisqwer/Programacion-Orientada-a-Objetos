class ClimaDiario:
    def __init__(self):
        # Inicializa una lista vacía para almacenar las temperaturas
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        # Agrega la temperatura proporcionada a la lista de temperaturas
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        # Calcula y devuelve el promedio de las temperaturas en la lista
        return sum(self.temperaturas) / len(self.temperaturas)


# Código principal
def main():
    # Crea una instancia de la clase ClimaDiario
    clima_semanal = ClimaDiario()

    # Repite 7 veces para ingresar las temperaturas de cada día de la semana
    for i in range(7):
        # Solicita al usuario que ingrese la temperatura del día i + 1
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        # Agrega la temperatura ingresada a la lista de temperaturas
        clima_semanal.ingresar_temperatura(temp)

    # Calcula el promedio de las temperaturas ingresadas
    promedio = clima_semanal.calcular_promedio()
    # Muestra el promedio de las temperaturas en la consola
    print(f"La temperatura promedio de la semana es: {promedio:.2f}")


# Ejecuta la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
