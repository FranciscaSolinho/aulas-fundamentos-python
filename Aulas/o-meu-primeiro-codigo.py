#importação de biblioteca
import math

# Definição de função
def calcular_area_retangulo(l, a):
    """Calcula a área de um retângulo."""
    return l * a

# Código principal
# Definir as dimensões do retângulo
largura = 5
altura = 3

#Chamada da função para calcular a área
area = calcular_area_retangulo(largura, altura)

#Imprimindo o resultado
print(f"A área do retângulo é {area}")

