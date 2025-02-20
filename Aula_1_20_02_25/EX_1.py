NumDivisores = 0
n = 30
# Loop de 1 até n (inclusive)
for i in range(1, n + 1):

    if n % i == 0: # Verifica se X é divisível por i
        NumDivisores += 1 # Incrementa o contador de divisores
print(NumDivisores)
