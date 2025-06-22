import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

# --- Монте-Карло ---
N = 100_000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)
under_curve = y_rand < f(x_rand)
area_rect = (b - a) * f(b)
monte_carlo_area = area_rect * np.sum(under_curve) / N

print(f"Площа під кривою методом Монте-Карло: {monte_carlo_area:.5f}")

# --- Аналітичне значення ---
analytical_area = (b**3 - a**3) / 3
print(f"Аналітичне значення інтеграла: {analytical_area:.5f}")

# --- Quad ---
quad_area, _ = spi.quad(f, a, b)
print(f"Значення інтеграла через scipy.integrate.quad: {quad_area:.5f}")

# --- Висновок ---
print(f"Похибка Монте-Карло: {abs(monte_carlo_area - analytical_area):.5e}")

# --- Графік ---
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, "r", linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()
