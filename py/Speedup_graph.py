import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = os.path.join(os.path.dirname(__file__), '../graficos')
os.makedirs(output_dir, exist_ok=True)

procesadores = np.array([8, 16])
tiempo_secuencial = 260.809

# STATIC
speedup_static = {
    10: [4.46, 6.87],
    1000: [4.41, 6.60],
    100000: [4.36, 6.37]
}

# DYNAMIC
speedup_dynamic = {
    10: [4.70, 6.64],
    1000: [4.41, 6.56],
    100000: [4.47, 7.17]
}

# GUIDED
speedup_guided = {
    10: [4.73, 6.76],
    1000: [5.60, 7.28],
    100000: [4.72, 7.15]
}

def graficar_speedup_eficiencia(schedule_name, speedup_data):
    plt.figure(figsize=(12, 5))

    # --- SPEEDUP ---
    plt.subplot(1, 2, 1)
    for chunk, values in speedup_data.items():
        plt.plot(procesadores, values, marker='o', label=f'Chunk={chunk}')
    plt.title(f'Speedup vs Nº de Procesadores ({schedule_name})')
    plt.xlabel('Número de Procesadores')
    plt.ylabel('Speedup')
    plt.xticks(procesadores)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    # --- EFICIENCIA ---
    plt.subplot(1, 2, 2)
    for chunk, values in speedup_data.items():
        eficiencia = [s/p for s, p in zip(values, procesadores)]
        plt.plot(procesadores, eficiencia, marker='o', label=f'Chunk={chunk}')
    plt.title(f'Eficiencia vs Nº de Procesadores ({schedule_name})')
    plt.xlabel('Número de Procesadores')
    plt.ylabel('Eficiencia')
    plt.xticks(procesadores)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.tight_layout()

    output_path = os.path.join(output_dir, f"Speedup_Eficiencia_{schedule_name}.png")
    plt.savefig(output_path)
    print(f"Gráfico guardado en: {output_path}")
    plt.close()

# Graficar cada schedule
graficar_speedup_eficiencia("Static", speedup_static)
graficar_speedup_eficiencia("Dynamic", speedup_dynamic)
graficar_speedup_eficiencia("Guided", speedup_guided)
