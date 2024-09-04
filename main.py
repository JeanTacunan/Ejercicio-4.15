class Cuadrado:
    def __init__(self, dimension: int):
        self.dimension = dimension

    def dibujar_lado_superior_inferior(self):
        # Dibuja la primera y última línea de asteriscos
        print('*' * self.dimension)

    def dibujar_lados_laterales(self):
        # Dibuja las líneas laterales del cuadrado
        for _ in range(self.dimension - 2):
            print('*' + ' ' * (self.dimension - 2) + '*')

    def dibujar(self):
        self.dibujar_lado_superior_inferior()  # Lado superior
        self.dibujar_lados_laterales()         # Lados laterales
        self.dibujar_lado_superior_inferior()  # Lado inferior

def main():
    try:
        N = int(input("Escribe la dimensión N > 2 del cuadrado a dibujar: \n"))
        if N <= 2:
            print("La dimensión debe ser mayor que 2.")
        else:
            cuadrado = Cuadrado(N)
            cuadrado.dibujar()
    except ValueError:
        print("Por favor, ingrese un número válido para la dimensión.")

if __name__ == "__main__":
    main()
