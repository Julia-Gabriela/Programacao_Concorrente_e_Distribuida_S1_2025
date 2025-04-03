import time 
import random

def CalcularVariancia(Dados):
    
    # deteremina a media aritmetica simples
    N = len(Dados)
    Soma = 0
    for X in Dados: Soma = Soma + X
    Media = Soma / N

    # Calcular a soma dos desvios quadrados

    SomaDQ = 0
    for X in Dados: SomaDQ + (X - Media) ** 2
    Variancia = SomaDQ / N

    return Variancia

#exemplo de uso 

Lista = [2,4,6,8,10]
Lista = [2,3,4,5,6]
Lista = [2,2,2,2,2]

Lista = [random.randint(1, 100) for _ in range(1000000)]

t0 = time.time()

V = CalcularVariancia(Lista)

tf = time.time()
print(f"Tempo de execução: {tf - t0} segundos")
print(f"Variancia: {V}")