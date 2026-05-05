import random
import math
import matplotlib.pyplot as plt

def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return steps
    return steps

def binary_search(arr, target):
    steps = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return steps

def run_experiment(size):
    arr = [random.randint(0, size * 10) for _ in range(size)]
    target = random.choice(arr)
    linear_steps = linear_search(arr, target)
    sorted_arr = sorted(arr)
    binary_steps = binary_search(sorted_arr, target)
    return linear_steps, binary_steps

sizes = [10, 50, 100, 200, 500, 750, 1000, 2000, 5000]

linear_results = []
binary_results = []

for size in sizes:
    lin, bin_ = run_experiment(size)
    linear_results.append(lin)
    binary_results.append(bin_)
    print(f"n={size:5d} | Lineal: {lin:5d} pasos | Binaria: {bin_:3d} pasos")

# ── Gráfica ──────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 6))

plt.plot(sizes, linear_results, marker='o', color='#378ADD', linewidth=2,
         markersize=6, label='Búsqueda lineal  O(n)')

plt.plot(sizes, binary_results, marker='s', color='#1D9E75', linewidth=2,
         markersize=6, label='Búsqueda binaria  O(log n)')

# Curva teórica de referencia (log2)
log_ref = [math.log2(n) for n in sizes]
plt.plot(sizes, log_ref, linestyle='--', color='#1D9E75', alpha=0.35,
         label='log₂(n)  referencia')

plt.title('Número de pasos vs. Tamaño del arreglo', fontsize=14)
plt.xlabel('Tamaño del arreglo (n)', fontsize=12)
plt.ylabel('Número de pasos', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('busqueda_pasos.png', dpi=150)
plt.show()
