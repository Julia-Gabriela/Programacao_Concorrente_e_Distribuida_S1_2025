import threading 
import time 

def saudacao(nome, tempo):
    print(f"Olá, {nome}")
    time.sleep(tempo)
    print(f"Tchau, {nome}")

A = threading.Thread(target = saudacao, args = ("Julia", 6))
B = threading.Thread(target = saudacao, args = ("Bruna", 2))

A.start()
A.join()
B.start()
B.join()

print("Thread principal encerrada")