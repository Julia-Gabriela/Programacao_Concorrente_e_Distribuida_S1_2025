import threading
s = threading.Semaphore(3)
x = 1
def Acesso(thread_id):
    global x
    print(f"Thread {thread_id} Tentando acessar recurso")
    with s:
        print(f"Thread {thread_id} acessou o recusro")
        threading.Event().wait(1)
        x = x * 2
    print(f"Thread {thread_id} liberou o recurso")

threads = [threading.Thread(target = Acesso, args = (i,))for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(f"encerrando") 