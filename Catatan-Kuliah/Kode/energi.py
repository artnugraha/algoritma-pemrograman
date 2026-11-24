energy = [4.5, 2.1, 0.5, 9.8, 1.2]
b = sorted(energy)
n = len(b)
median = b[n // 2] if n % 2 else (b[n // 2 - 1] + b[n // 2]) / 2
print(f"Min = {b[0]:.2f} J")
print(f"Median = {median:.2f} J")
print(f"Max = {b[-1]:.2f} J")
