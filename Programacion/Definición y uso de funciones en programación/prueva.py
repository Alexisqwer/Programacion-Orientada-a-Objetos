# crear una funcion para convertir en grado centigrados a grados Fahrenheit, a grados kelvin
def conversion(tem_grad_cent):
    Fahrenheit = (9/5) * (tem_grad_cent) + 32
    Kelvin = 273.15 + tem_grad_cent
    # Utilizando una tupla para retornar ambos resultados
    return Fahrenheit, Kelvin

# Solicitar al usuario que ingrese grados Centigrados
grad_cent = int(input("Ingrese grados centigrados: "))

# Utilizar la funcion conversion y asignar los valores de la tupla a las variables Fahren y Kelv
Fahren, Kelv = conversion(grad_cent)

# Imprimir los valores de Fahren y Kelv
print("Grados Fahrenheit:", Fahren)
print("Grados Kelvin:", Kelv)