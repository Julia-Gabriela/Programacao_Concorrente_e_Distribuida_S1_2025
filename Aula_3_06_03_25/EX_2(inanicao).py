import threading
import time

AP_contador = 0 #Contador de alta prioridade
BP_contador = 0 #Contador de baixa prioridade

L = threading.Lock()

def AltaPrioridade():
    global AP_contador
    while True:
        with L:
            print(F"[Alta prioridade] usando o recurso")
            AP_contador += 1
            time.sleep(0.5)

def BaixaPrioridade():
    global BP_contador
    while True:
        with L:
            print(F"[Baixa prioridade] usando o recurso")
            BP_contador += 1
            time.sleep(0.5)

# criando as threads

T_AP = threading.Thread(target = AltaPrioridade, daemon=True )
T_BP = threading.Thread(target = BaixaPrioridade, daemon=True)

T_AP.start()
T_BP.start()

time.sleep(10)


print("\nRelatorio:")
print(f"Thread de alta prioridade:{AP_contador} vezes")
print(f"Thread de Baixa prioridade:{BP_contador} vezes")