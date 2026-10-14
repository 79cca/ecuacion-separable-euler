import math

# Problema: dy/dt = -2y, y(0) = 1
# Intervalo [0, 1] y paso h = 0.2

def f(t, y):
    return -2 * y

def solucion_exacta(t):
    return math.exp(-2 * t)

t = 0.0
y_euler = 1.0
h = 0.2
t_final = 1.0

n = int(round((t_final - t) / h))

print(f"{'t':>5} {'Euler':>12} {'Exacta':>12} {'Error':>12}")

for paso in range(n + 1):
    exacta = solucion_exacta(t)
    error = abs(exacta - y_euler)
    print(f"{t:5.1f} {y_euler:12.6f} {exacta:12.6f} {error:12.6f}")

    if paso < n:
        y_euler = y_euler + h * f(t, y_euler)
        t = round(t + h, 10)
