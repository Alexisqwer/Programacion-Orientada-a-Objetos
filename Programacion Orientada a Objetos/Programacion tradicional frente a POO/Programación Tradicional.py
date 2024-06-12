# Función para ingresar datos diarios de temperaturas
def ingresar_temperaturas():
    # Inicializa una lista vacía para almacenar las temperaturas
    temperaturas = []
    # Bucle para ingresar las temperaturas de los 7 días de la semana
    for i in range(7):
        # Solicita al usuario ingresar la temperatura del día i+1
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        # Agrega la temperatura ingresada a la lista de temperaturas
        temperaturas.append(temp)
    # Devuelve la lista de temperaturas ingresadas
    return temperaturas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio(temperaturas):
    # Calcula y devuelve el promedio de las temperaturas en la lista
    return sum(temperaturas) / len(temperaturas)

# Código principal
def main():
    # Llama a la función para ingresar temperaturas y almacena el resultado en la variable 'temperaturas'
    temperaturas = ingresar_temperaturas()
    # Llama a la función para calcular el promedio de las temperaturas y almacena el resultado en la variable 'promedio'
    promedio = calcular_promedio(temperaturas)
    # Muestra el promedio de las temperaturas en la consola con dos decimales
    print(f"La temperatura promedio de la semana es: {promedio:.2f}")

# Ejecuta la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
