import serial
import json
from funcs import *

ser = serial.Serial("COM4", 115200)

data = {
    "temperature": [],
    "pressure": [],
    "altitude": []
}
err = 0

for _ in range(5):
    try:
        line = ser.readline().decode("utf-8", errors="ignore").strip()
        if line:
            temp_str, pres_str = line.split(",")[:2]
            temp = float(temp_str)
            pres = float(pres_str)
            alt = pressure_to_altitude(pres)

            data["temperature"].append(temp)
            data["pressure"].append(pres)
            data["altitude"].append(alt)

            print(f"Temp: {temp} C, Pressure: {pres} hPa, Altitude: {alt} m")
    except UnicodeDecodeError:
        print("Decode error, skipping line")
        err += 1
    except ValueError:
        print("Malformed line, skipping")
        err += 1

print(f"Data collection finished. Errors: {err}")

# Save to JSON
with open("db.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data saved to db.json.")
print(">>> Please run plot.py separately.")
input("Press Enter to continue...")

'''
import serial
from funcs import *

ser = serial.Serial("COM4", 115200)

temp_arr = []
pres_arr = []
alt_arr = []
err: int = 0

for loop in range(5):
    try:
        line = ser.readline().decode("utf-8").strip()
        if line:
            temp_str, pres_str = line.split(",")
            temp = float(temp_str)
            pres = float(pres_str)
            alt = pressure_to_altitude(pres)

            temp_arr.append(temp)
            pres_arr.append(pres)
            alt_arr.append(alt)

            print(f"Temperature: {temp} C, Pressure: {pres} hPa, Altitude: {alt} m")
    except UnicodeDecodeError:
        print("Decode error, skipping line")
        err += 1
    except ValueError:
        print("Malformed line, skipping")
        err += 1

print(f"Readings are done. Errors: {err}")

# --- GRAPHING

# graph_data(alt_arr, temp_arr, "Pressure")
# from graph import graph_data
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.plot(alt_arr, temp_arr, marker='o', color='blue', linewidth=2, markersize=6)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel("Altitude (m, relative)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Relative Altitude")
plt.tight_layout()
plt.show()


import numpy as np
plt.figure(figsize=(8,6))
plt.scatter(alt_arr, temp_arr, color='blue', label='Data Points', s=50)  # s=marker size

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

# Show plot
plt.show()
'''