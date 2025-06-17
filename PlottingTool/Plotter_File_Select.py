import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from tkinter import filedialog as fd

#Popup Menu to select File
root = tk.Tk()
root.withdraw()  
filepath = fd.askopenfilename()
filename = filepath.split('/')[-1]

wavelength = []
voltage = []

with open(filepath, 'r') as file:
    for line in file:
        data = line.strip().split('\t')
        wavelength.append(data[0])
        if len(data) > 1:  # Ensure there are at least two elements
            voltage.append(data[1])
        else:
            print(f"Skipping line due to insufficient data: {data}")
            print(line)
        
wavelength_array = np.array(wavelength, dtype='float64')
voltage_array = np.array(voltage, dtype='float64')
#find the Maxima of the graph
distance = 85000
maxima, _ = signal.find_peaks(voltage_array, distance=distance)
np.diff(maxima)

avg_wave=0
divisions = len(maxima)
wave = wavelength_array[maxima]

#Average Wavelength between Maxima
for i in range(1,len(wave)-1):
    avg_wave +=  wave[i] - wave[i-1]
if(divisions>0):
    avg_wave = avg_wave/divisions


min_voltage = np.min(voltage_array)
max_voltage = np.max(voltage_array)

#Graph Setup
plt.figure(figsize=(12, 8))
plt.title(f"{filename}")
plt.xticks(np.arange(wavelength_array[0]-10, wavelength_array[-1]+10, 5.0))
plt.xticks(rotation=45, ha='right')
plt.xlabel("Wavelength")
plt.ylabel("Voltage")


plt.plot(wavelength_array,voltage_array)
plt.figtext(0.5,0.95, f"Average Wavelength between Maxima: {avg_wave:.5f}", horizontalalignment='center')
plt.vlines(wavelength_array[maxima],min_voltage,max_voltage,linestyles="dashed",colors="lightblue")
plt.plot(wavelength_array[maxima],voltage_array[maxima],"x")

for points in maxima:
    plt.annotate(f"{wavelength_array[points]:.5f}", (wavelength_array[points],voltage_array[points]))

plt.savefig(f"{filename}.png", dpi=650, bbox_inches="tight")
plt.show()