from numba import jit, prange
from time import time
@jit(nopython=True)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

@jit(nopython=True, parallel=True)
def count_primes(limit):
    count = 0
    for i in prange(2, limit):
        if is_prime(i):
            count += 1
    return count
if __name__ == "__main__":
    limit = 400000000
    start_time = time()
    count = count_primes(limit)
    end_time = time()
    print("=== Versión Paralela ===\n")
    print(f"Rango 2 a {limit}\n")
    print(f"Primos encontrados: {count}\n")
    print(f"Tiempo: {end_time - start_time} segundos\n")
