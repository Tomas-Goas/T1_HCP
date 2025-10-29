import matplotlib.pyplot as plt

threads = [1, 2, 4, 8, 16]
tiempos = [31.58, 45.36, 69.7, 90.3, 210.5]  # tus resultados

plt.plot(threads, tiempos, marker='o')
plt.title("Escalabilidad Débil - Tiempo vs Número de Threads")
plt.xlabel("Número de threads")
plt.ylabel("Tiempo de ejecución (s)")
plt.grid(True)

plt.savefig("weak_scaling.png")  # guarda el gráfico

