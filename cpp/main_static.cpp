#include <iostream>
#include <chrono>
#include <omp.h>

bool is_prime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int limit = 400000000;  // Buscar primos hasta 400 millones
    int count = 0;

    int num_threads = 8;  
    omp_set_num_threads(num_threads);

    // Iniciar medición de tiempo
    auto start = std::chrono::high_resolution_clock::now();

    // Versión paralela con schedule(static, numero_de_chunk)
    #pragma omp parallel for schedule(static, 1000) reduction(+:count)
    for (int n = 2; n < limit; n++) {
        if (is_prime(n)) {
            count++;
        }
    }

    // Terminar medición de tiempo
    auto end = std::chrono::high_resolution_clock::now();
    
    // Calcular duración
    std::chrono::duration<double> duration = end - start;
    
    // Mostrar resultados
    std::cout << "=== Versión Secuencial ===" << std::endl;
    std::cout << "Primos encontrados: " << count << std::endl;
    std::cout << "Tiempo: " << duration.count() << " segundos" << std::endl;
    return 0;
}
