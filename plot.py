import json
import matplotlib.pyplot as plt
import numpy as np
import time

with open("db.json", "r") as f:
    data = json.load(f)

temp_arr = data["temperature"]
pres_arr = data["pressure"]
alt_arr = data["altitude"]

plt.figure(figsize=(8,6))
plt.scatter(alt_arr, temp_arr, color='blue', label='Data Points', s=50)
coeffs = np.polyfit(alt_arr, temp_arr, 1)
poly_eqn = np.poly1d(coeffs)
best_fit = poly_eqn(alt_arr)
plt.plot(alt_arr, best_fit, color='red', linestyle='--', label='Best Fit Line')
plt.xlabel("Altitude (m, relative)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Relative Altitude")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

input("Press Enter to continue...")

plt.figure(figsize=(8,6))
plt.scatter(alt_arr, pres_arr, color='blue', label='Data Points', s=50)

coeffs = np.polyfit(alt_arr, pres_arr, 1)
poly_eqn = np.poly1d(coeffs)
best_fit = poly_eqn(alt_arr)
plt.plot(alt_arr, best_fit, color='red', linestyle='--', label='Best Fit Line')

plt.xlabel("Altitude (m, relative)")
plt.ylabel("Pressure (hPa)")
plt.title("Pressure vs Relative Altitude")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()