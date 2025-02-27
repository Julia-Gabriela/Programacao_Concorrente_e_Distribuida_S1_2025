import threading 
import time 

def tarefa():
    print("Início...")
    time.sleep(5)
    print("Fim")

    #bloco principal (main)

thread = threading.Thread(target = tarefa)
thread.start() # inicia a thread
thread.join() # Aguarda a conclusão do thread
print("Thread principal finalizada")
