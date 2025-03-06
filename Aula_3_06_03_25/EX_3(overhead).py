import threading
import time

contador = 0
L = threading.Lock()

def incrementar():
    global contador
    t0 = time.time() 

    for _ in range(1000000):
         with L:
            contador += 1
    tf = time.time()
    delta_t = tf - t0
    print(f"Tempo gasto: {delta_t}")

threads = [threading.Thread(target=incrementar) for _ in range(10)]

for t in threads: t.start()
for t in threads: t.join()

print(f"Contador final: {contador}")
