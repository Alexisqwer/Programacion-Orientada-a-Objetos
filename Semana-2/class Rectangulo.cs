// Clase para representar un Rectángulo
public class Rectangulo
{
    // Campos privados para almacenar la base y la altura
    private double baseRect;
    private double altura;

    // Constructor para inicializar base y altura
    public Rectangulo(double baseRect, double altura)
    {
        this.baseRect = baseRect;
        this.altura = altura;
    }

    // Método para calcular el área del rectángulo
    // CalcularArea devuelve el producto de la base y la altura
    public double CalcularArea()
    {
        return baseRect * altura;
    }

    // Método para calcular el perímetro del rectángulo
    // CalcularPerimetro devuelve la suma de todos los lados: 2 * (base + altura)
    public double CalcularPerimetro()
    {
        return 2 * (baseRect + altura);
    }
}
