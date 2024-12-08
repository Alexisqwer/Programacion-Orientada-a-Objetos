// Clase para representar un Círculo
public class Circulo
{
    // Campo privado para almacenar el radio
    private double radio;

    // Constructor para inicializar el radio
    public Circulo(double radio)
    {
        this.radio = radio;
    }

    // Método para calcular el área del círculo
    // CalcularArea es una función que devuelve un valor double
    // Se utiliza para calcular el área de un círculo con el radio especificado
    public double CalcularArea()
    {
        return Math.PI * radio * radio;
    }

    // Método para calcular el perímetro del círculo
    // CalcularPerimetro devuelve el perímetro utilizando la fórmula 2 * PI * radio
    public double CalcularPerimetro()
    {
        return 2 * Math.PI * radio;
    }
}
