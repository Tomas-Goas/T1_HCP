# 🧮 T1_HCP

## 📊 Resultados

### 🔹 Resultados de referencia (versión secuencial)

| Parámetro | Valor |
|------------|--------|
| **Rango evaluado** | 2 → 400,000,000 |
| **Primos encontrados** | 21,336,326 |
| **Tiempo de ejecución** | ⏱️ 260.809 segundos |

### 🔹 Resultados Version Paralela

#### Schedule(static)

| Chunks | Parámetro | 8 Hilos | 16 Hilos |
|:-------|:-----------|:--------|:----------|
| **10** | **Tiempo de ejecución** | ⏱️ 47.5133 s | ⏱️ 37.9286 s |
|  | **Speedup** | 4.46× | 6.87× |
| **1000** | **Tiempo de ejecución** | ⏱️ 48.044 s | ⏱️ 39.520 s |
|  | **Speedup** | 4.41× | 6.60× |
| **100000** | **Tiempo de ejecución** | ⏱️ 48.5659 s | ⏱️ 40.9047 s |
|  | **Speedup** | 4.36× | 6.37× |

#### Schedule(dynamic)

| Chunks | Parámetro | 8 Hilos | 16 Hilos |
|:-------|:-----------|:--------|:----------|
| **10** | **Tiempo de ejecución** | ⏱️ 45.2478 s | ⏱️ 39.2581 s |
|  | **Speedup** | 4.70× | 6.64× |
| **1000** | **Tiempo de ejecución** | ⏱️ 48.0436 s | ⏱️ 39.752 s |
|  | **Speedup** | 4.41× | 6.56× |
| **100000** | **Tiempo de ejecución** | ⏱️ 47.4016 s | ⏱️ 36.3698 s |
|  | **Speedup** | 4.47× | 7.17× |

---

#### Schedule(guided)

| Chunks | Parámetro | 8 Hilos | 16 Hilos |
|:-------|:-----------|:--------|:----------|
| **10** | **Tiempo de ejecución** | ⏱️ 44.956 s | ⏱️ 38.5945 s |
|  | **Speedup** | 4.73× | 6.76× |
| **1000** | **Tiempo de ejecución** | ⏱️ 46.535 s | ⏱️ 35.820 s |
|  | **Speedup** | 5.60× | 7.28× |
| **100000** | **Tiempo de ejecución** | ⏱️ 45.042 s | ⏱️ 36.4544 s |
|  | **Speedup** | 4.72× | 7.15× |


### 📈 Gráfico Comparativo de Tiempos

Los siguientes resultados ilustran el comportamiento de los tres *schedules* (`static`, `dynamic`, `guided`) con diferentes cantidades de *chunks* y hilos.

![Gráfico de Schedules](assets/grafico_schedules.png)