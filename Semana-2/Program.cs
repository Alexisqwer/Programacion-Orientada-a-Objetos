// Ejemplo de uso
class Program
{
    static void Main(string[] args)
    {
        // Crear un objeto de la clase Circulo
        Circulo circulo = new Circulo(5);
        Console.WriteLine($"Área del círculo: {circulo.CalcularArea()}"); // Ejemplo de cálculo del área
        Console.WriteLine($"Perímetro del círculo: {circulo.CalcularPerimetro()}"); // Ejemplo de cálculo del perímetro

        // Crear un objeto de la clase Rectangulo
        Rectangulo rectangulo = new Rectangulo(4, 7);
        Console.WriteLine($"Área del rectángulo: {rectangulo.CalcularArea()}"); // Ejemplo de cálculo del área
        Console.WriteLine($"Perímetro del rectángulo: {rectangulo.CalcularPerimetro()}"); // Ejemplo de cálculo del perímetro
    }
}
