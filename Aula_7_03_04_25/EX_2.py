import matplotlib.pyplot as plt

def speedup(f, p_values):
    results = [(p, 1/((1-f)+ f/p)) for p in p_values]
    return results

f = 0.6 # "60% paralelizavel"
p_values = [1, 2, 3, 4, 8, 16, 32, 1000]
s_values = speedup(f, p_values)

for p, sp in s_values:
    print(f"{p}\t{sp}")

plt.plot(p_values, [s[1] for s in s_values], marker = 'o')
plt.xlabel("Numero de processadores (p)")
plt.ylabel("Speedup (s(p))")
plt.title("s(p) versus p para{f}")
plt.grid()
plt.show()