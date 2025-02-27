import threading
import time

# variavel global(acessada por todas as threads)

Contador = 0 
lock = threading.Lock()

def incrementar():
    global Contador
    for _ in range(100):
        lock.acquire() #Adquire acesso ao recurso(Variavel)
        try:
            Contador += 1
            print(Contador)
            time.sleep(0.1)
        finally: 
            lock.release() #Liberar o recurso(variavel)

threads = []

for i in range(10):
    thread = threading.Thread(target = incrementar)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Contador: {Contador}")