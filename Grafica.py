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

def run_experiment(size, repetitions=20):
    lin_total, bin_total = 0, 0
    for _ in range(repetitions):
        arr = [random.randint(0, size * 10) for _ in range(size)]
        target = random.choice(arr)
        lin_total += linear_search(arr, target)
        sorted_arr = sorted(arr)
        bin_total += binary_search(sorted_arr, target)
    return lin_total // repetitions, bin_total // repetitions  # promedio

sizes = [10, 50, 100, 200, 500, 750, 1000, 2000, 5000]
linear_results = []
binary_results = []

for size in sizes:
    lin, bin_ = run_experiment(size)
    linear_results.append(lin)
    binary_results.append(bin_)
    print(f"n={size:5d} | Lineal: {lin:5d} pasos | Binaria: {bin_:3d} pasos")

log_ref = [math.log2(n) for n in sizes]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Número de pasos vs. Tamaño del arreglo', fontsize=14)

# ── Subplot 1: escala normal (se ve el contraste) ────────────────────────────
ax1.plot(sizes, linear_results, marker='o', color='#378ADD', linewidth=2,
         markersize=6, label='Búsqueda lineal  O(n)')
ax1.plot(sizes, binary_results, marker='s', color='#1D9E75', linewidth=2,
         markersize=6, label='Búsqueda binaria  O(log n)')
ax1.set_title('Escala lineal')
ax1.set_xlabel('Tamaño del arreglo (n)')
ax1.set_ylabel('Número de pasos (promedio 20 ejecuciones)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# ── Subplot 2: escala logarítmica (se ve la curva de la binaria) ─────────────
ax2.plot(sizes, linear_results, marker='o', color='#378ADD', linewidth=2,
         markersize=6, label='Búsqueda lineal  O(n)')
ax2.plot(sizes, binary_results, marker='s', color='#1D9E75', linewidth=2,
         markersize=6, label='Búsqueda binaria  O(log n)')
ax2.plot(sizes, log_ref, linestyle='--', color='#1D9E75', alpha=0.35,
         label='log₂(n)  referencia')
ax2.set_yscale('log')
ax2.set_title('Escala logarítmica')
ax2.set_xlabel('Tamaño del arreglo (n)')
ax2.set_ylabel('Número de pasos (escala log)')
ax2.legend()
ax2.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('busqueda_pasos.png', dpi=150)
plt.show()
