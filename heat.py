import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf, erfc

def i_erfc(x): # I have verified that this function is correct
    return (1 / np.sqrt(np.pi)) * np.exp(-x**2) - x * (1 - erf(x))

def delta_T(H, k, alpha, a, z, t):
    term1 = i_erfc(z / (2 * np.sqrt(alpha * t)))
    term2 = i_erfc(np.sqrt(z**2 + a**2) / (2 * np.sqrt(alpha * t)))
    
    delta_T_value = (2 * H / k) * np.sqrt(alpha * t) * (term1 - term2)
    return delta_T_value

def fluence(E, a):
    return(E/(np.pi*(a*100)**2)) # turn a from m to cm

# Example parameters (for copper) (https://www.sfu.ca/~gchapman/e894/e894l20n.pdf)
Hco = 1e10  # transferred intensity (W/m²)
kco = 385  # thermal conductivity of copper (W/mK)
alphaco = 1e-4  # thermal diffusivity of copper (m²/s)
aco = 1e-3  # spot radius (m)
zco = 0  # distance from beam center (m)
tco = 1e-6  # Pulse duration (s)

# Crystal
E = 125e-9 # Energy (J)
t =  1e-9 #1.4e-13  #pulse duration (s)
P = E/t # power (W)
a = 34e-6  # spot radius (m)
Rc = 0.37 # reflectivity
Ra = .4875
I = P/(np.pi*a**2) # intensity
print(I)
Hc = I*(1-Rc)  # transferred intensity (W/m²)
Ha = I*(1-Ra)
kc = 0.36  # thermal conductivity (W/(m*K))
ka = 0.22
alpha = 1.44e-10  # thermal diffusivity (m²/s)


depthco = np.linspace(0, 1e-4, num=500)
depth = np.linspace(0, 50e-9, num=500)
depth2 = np.linspace(0, .5e-8, num=500)

plt.figure()
plt.plot(depthco, delta_T(Hco, kco, alphaco, aco, depthco, tco), label="Copper")

# Add labels, title, and legend
plt.xlabel("Depth into Copper (m)")
plt.ylabel("Temperature Change (K)")
plt.title("Temperature Penetration in Copper")
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(depth, delta_T(Hc, kc, alpha, a, depth, t), label="Crystalline Sb2Se3")

# Add labels, title, and legend
plt.xlabel("Depth into PCM (m)")
plt.ylabel("Temperature Change (K)")
plt.title("Temperature Penetration in Crystalline Sb2Se3")
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(depth2, delta_T(Hc, kc, alpha, a, depth2, t))

# Add labels, title, and legend
plt.xlabel("Depth into PCM (m)")
plt.ylabel("Temperature Change (K)")
plt.title("Temperature Penetration in Crystalline Sb2Se3")
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

# Amorphous #######################################################################################

plt.figure()
plt.plot(depth, delta_T(Ha, ka, alpha, a, depth, t), label="Amorphous Sb2Se3")

# Add labels, title, and legend
plt.xlabel("Depth into PCM (m)")
plt.ylabel("Temperature Change (K)")
plt.title("Temperature Penetration in Amorphous Sb2Se3")
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(depth2, delta_T(Ha, ka, alpha, a, depth2, t))

# Add labels, title, and legend
plt.xlabel("Depth into PCM (m)")
plt.ylabel("Temperature Change (K)")
plt.title("Temperature Penetration in Amorphous Sb2Se3")
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

# Single point #######################################################################################

# Compute temperature rise
z = 3e-11  # depth into the material (m)
delta_T_result = delta_T(Ha, ka, alpha, a, z, t)
flu = fluence(E,a)
print(f"Temperature rise: {delta_T_result:.10f} K")
print(f"Energy Fluence: {flu:.10f} J/cm^2")
print(f"Power: {P} W")
