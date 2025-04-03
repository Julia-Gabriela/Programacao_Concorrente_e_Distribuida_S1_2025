import threading

B = threading.Barrier(3)

def trabalho():
    print(f"Thread{thread_id} iniciada.")
    threading.Event().wait(1)
    print(f"Thread{thread_id} chegou a barreira.")
    B.wait()
    print(f"Thread{thread_id} passou da barreira.")

    