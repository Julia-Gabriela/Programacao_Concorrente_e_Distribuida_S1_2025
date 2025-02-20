import psutil
def verificar_processo_ativo(pid):
    return psutil.pid_exists(pid)
pid = int(input("Digite o PID do processo: "))
if verificar_processo_ativo(pid):
    print(f"O processo com PID {pid} está ativo.")
else:
    print(f"O processo com PID {pid} não está ativo ou terminou.")
