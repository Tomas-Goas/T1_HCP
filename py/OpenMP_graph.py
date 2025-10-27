import matplotlib.pyplot as plt

# --- Schedule STATIC ---
static = {
    8: {10: 47.5133, 1000: 48.044, 100000: 48.5659},
    16: {10: 37.9286, 1000: 39.520, 100000: 40.9047}
}

# --- Schedule DYNAMIC ---
dynamic = {
    8: {10: 45.2478, 1000: 48.0436, 100000: 47.4016},
    16: {10: 39.2581, 1000: 39.752, 100000: 36.3698}
}

# --- Schedule GUIDED ---
guided = {
    8: {10: 44.956, 1000: 46.535, 100000: 45.042},
    16: {10: 38.5945, 1000: 35.820, 100000: 36.4544}
}

chunks = [10, 1000, 100000]

plt.figure(figsize=(10, 6))
plt.title("Comparación de Tiempos de Ejecución según Schedule y Hilos", fontsize=14, weight='bold')

# --- Graficar 8 hilos ---
plt.plot(chunks, [static[8][c] for c in chunks], 'o--', label="Static (8 hilos)")
plt.plot(chunks, [dynamic[8][c] for c in chunks], 's--', label="Dynamic (8 hilos)")
plt.plot(chunks, [guided[8][c] for c in chunks], 'd--', label="Guided (8 hilos)")

# --- Graficar 16 hilos ---
plt.plot(chunks, [static[16][c] for c in chunks], 'o-', label="Static (16 hilos)")
plt.plot(chunks, [dynamic[16][c] for c in chunks], 's-', label="Dynamic (16 hilos)")
plt.plot(chunks, [guided[16][c] for c in chunks], 'd-', label="Guided (16 hilos)")

plt.xscale('log')  # escala logarítmica para chunks (mejor visualización)
plt.xticks(chunks, ["10", "1000", "100000"])
plt.xlabel("Cantidad de Chunks", fontsize=12)
plt.ylabel("Tiempo de Ejecución (segundos)", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.7, alpha=0.7)
plt.legend(title="Tipo de Schedule", fontsize=10)
plt.tight_layout()
plt.savefig("grafico_schedules.png")
print("✅ Gráfico guardado como 'grafico_schedules.png'")

