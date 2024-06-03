# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado al monto total de la compra.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    # Cálculo del descuento aplicando el porcentaje al monto total
    descuento = monto_total * porcentaje_descuento / 100
    # Retorno del monto del descuento calculado
    return descuento    

# Llamadas a la función desde el programa principal
if __name__ == "__main__":
    # Primera llamada a la función: proporciona solo el monto total de la compra
 monto_compra_1 = 1000
    # Llamada a la función calcular_descuento con un solo parámetro (monto_total)
descuento_1 = calcular_descuento(monto_compra_1)
    # Cálculo del monto final a pagar después del descuento
total_con_descuento_1 = monto_compra_1 - descuento_1
    # Impresión del monto del descuento y el monto final a pagar después del descuento
print("Monto del descuento 1:", descuento_1)
print("Monto final a pagar después del descuento 1:", total_con_descuento_1)
    # Segunda llamada a la función: proporciona tanto el monto total de la compra como el porcentaje de descuento
monto_compra_2 = 2000
porcentaje_descuento_2 = 20
    # Llamada a la función calcular_descuento con dos parámetros (monto_total y porcentaje_descuento)
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    # Cálculo del monto final a pagar después del descuento
total_con_descuento_2 = monto_compra_2 - descuento_2
    # Impresión del monto del descuento y el monto final a pagar después del descuento
print("\nMonto del descuento 2:", descuento_2)
print("Monto final a pagar después del descuento 2:", total_con_descuento_2)