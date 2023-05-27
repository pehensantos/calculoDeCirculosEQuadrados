import math


class Circulo:

    def __init__(self, raio):
        self.raio = raio

    def calcular_circunferencia(self):
        return f'Valor da circunferencia:{2 * math.pi * self.raio}'

    def todos_os_dados(self):
        return f'raio:{float(self.raio)}\n' \
               f'Valor da circunferencia:{2 * math.pi * self.raio}'


class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return f'Área:{self.lado * self.lado:.2f}'

    def calcular_perimetro(self):
        return f'Perímetro:{self.lado * 4:.2f}'

    def todos_os_dados(self):
        return f'Lado do quadrado:{float(self.lado):.2f}\n' \
               f'Área:{self.lado * self.lado:.2f}\n' \
               f'Perímetro:{self.lado * 4:.2f}\n'


circulo = Circulo(3.5)                    # Instância.
print(circulo.calcular_circunferencia())  # Retorna apenas a circunferência.
print("\n")
print(circulo.todos_os_dados())           # Retorna todos os dados do círculo.
print("\n")

quadrado = Quadrado(5.5)                  # Instância.
print(quadrado.calcular_area())           # Retorna apenas a área.
print(quadrado.calcular_perimetro())      # Retorna apenas perímetro.
print(quadrado.todos_os_dados())          # Retorna todos os dados do quadrado.
