import matplotlib.pyplot as plt
import numpy as np

# Данные
n = [10, 100, 1000]
cpu_times = [28, 2185, 29976]
gpu_times = [179200, 179800, 199057]
speedup = [28/179200, 2185/179800, 29976/199057]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# ===== ГРАФИК 1: Время выполнения =====
ax1.plot(n, cpu_times, 'o-', color='blue', linewidth=2, markersize=8, label='CPU')
ax1.plot(n, gpu_times, 's-', color='red', linewidth=2, markersize=8, label='GPU')
ax1.set_xlabel('Размер сетки n', fontsize=12)
ax1.set_ylabel('Время выполнения (мкс)', fontsize=12)
ax1.set_title('(a) Время выполнения CPU и GPU', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)

# ===== ГРАФИК 2: Ускорение =====
ax2.plot(n, speedup, 'o-', color='blue', linewidth=2, markersize=8)
ax2.axhline(y=1, color='red', linestyle='--', linewidth=2, label='CPU = GPU')
ax2.set_xlabel('Размер сетки n', fontsize=12)
ax2.set_ylabel('Ускорение (CPU / GPU)', fontsize=12)
ax2.set_title('(b) Ускорение GPU относительно CPU', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_yscale('log')

# Подписи точек
for i, (x, y) in enumerate(zip(n, speedup)):
    ax2.annotate(f'{y:.4f}×', (x, y), xytext=(5, 5), textcoords='offset points', fontsize=9)

plt.tight_layout()
plt.savefig('speedup_comparison.png', dpi=150, bbox_inches='tight')
plt.show()