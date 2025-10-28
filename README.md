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

## ⚙️ Gráficos de Speedup y Eficiencia vs Nº de Procesadores

A continuación se presentan los gráficos generados a partir de los resultados experimentales para cada tipo de *schedule*.  
Estos gráficos permiten analizar cómo varía la **aceleración (Speedup)** y la **eficiencia del paralelismo** al aumentar el número de procesadores.

---

### 🔸 Schedule Static
![Speedup y Eficiencia - Static](../graficos/Speedup_Eficiencia_Static.png)

---

### 🔸 Schedule Dynamic
![Speedup y Eficiencia - Dynamic](../graficos/Speedup_Eficiencia_Dynamic.png)

---

### 🔸 Schedule Guided
![Speedup y Eficiencia - Guided](../graficos/Speedup_Eficiencia_Guided.png)

---

### 🧠 Comentarios Generales

- El **Speedup** aumenta con el número de procesadores, pero tiende a estabilizarse a medida que crecen los hilos debido a la sobrecarga de coordinación.  
- El **schedule guided** obtiene la mejor eficiencia general, especialmente con `chunk = 1000`, mostrando un balance más adecuado entre carga de trabajo y overhead.  
- La **eficiencia** disminuye al aumentar el número de procesadores, lo que es esperado en sistemas paralelos reales, debido a la ley de Amdahl y las pérdidas por sincronización.

---