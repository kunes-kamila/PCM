import numpy as np
import matplotlib.pyplot as plt
import os

# Load data (adjust delimiter if needed)
data16 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/021225_PCM_Rings_Annealed/PCM_D2 TRing16 25dB atten f2fs.dat")
data15 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/021225_PCM_Rings_Annealed/PCM_D2 TRing15 25dB atten f2fs.dat")
data14 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/021225_PCM_Rings_Annealed/PCM_D2 TRing14 25dB atten f2fs.dat")
data13 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/021225_PCM_Rings_Annealed/PCM_D2 TRing13 25dB atten f2fs.dat")
data12 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/021225_PCM_Rings_Annealed/PCM_D2 TRing12 25dB atten f2fs.dat")
data11 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/021225_PCM_Rings_Annealed/PCM_D2 TRing11 25dB atten f2fs.dat")

# Load data (adjust delimiter if needed)
dataPCM16 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/052925_PCM_Rings/PCM_D2 TRing16 25dB atten f2fs.dat")
dataPCM15 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/052925_PCM_Rings/PCM_D2 TRing15 25dB atten f2fs.dat")
dataPCM14 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/052925_PCM_Rings/PCM_D2 TRing14 25dB atten f2fs.dat")
dataPCM13 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/052925_PCM_Rings/PCM_D2 TRing13 25dB atten f2fs.dat")
dataPCM12 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/052925_PCM_Rings/PCM_D2 TRing12 25dB atten f2fs.dat")
dataPCM11 = np.loadtxt("/Users/kamilakunes/Desktop/PhDwork/Phase Change Modulator/052925_PCM_Rings/PCM_D2 TRing11 20dB atten f2fs.dat")

x16 = data16[:, 0]  # First column
y16 = data16[:, 1]  # Second column

x15 = data15[:, 0]  # First column
y15 = data15[:, 1]  # Second column

x14 = data14[:, 0]  # First column
y14 = data14[:, 1]  # Second column

x13 = data13[:, 0]  # First column
y13 = data13[:, 1]  # Second column

x12 = data12[:, 0]  # First column
y12 = data12[:, 1]  # Second column

x11 = data11[:, 0]  # First column
y11 = data11[:, 1]  # Second column

# PCM Rings
xPCM16 = dataPCM16[:, 0]  # First column
yPCM16 = dataPCM16[:, 1]  # Second column

xPCM15 = dataPCM15[:, 0]  # First column
yPCM15 = dataPCM15[:, 1]  # Second column

xPCM14 = dataPCM14[:, 0]  # First column
yPCM14 = dataPCM14[:, 1]  # Second column

xPCM13 = dataPCM13[:, 0]  # First column
yPCM13 = dataPCM13[:, 1]  # Second column

xPCM12 = dataPCM12[:, 0]  # First column
yPCM12 = dataPCM12[:, 1]  # Second column

xPCM11 = dataPCM11[:, 0]  # First column
yPCM11 = dataPCM11[:, 1]  # Second column

plt.figure(1,figsize=(16, 6))
plt.subplot(1, 2, 1)
plt.plot(x16, y16, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,6) - 0.7 um Gap")

plt.subplot(1, 2, 2)
plt.plot(xPCM16, yPCM16, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,6) - 0.7 um Gap with PCM")

save_path = os.path.join('/Users/kamilakunes/Desktop/Rings', "ringPCM16.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

plt.figure(2,figsize=(16, 6))
plt.subplot(1, 2, 1)
plt.plot(x15, y15, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,5) - 0.8 um Gap")

plt.subplot(1, 2, 2)
plt.plot(xPCM15, yPCM15, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,5) - 0.8 um Gap with PCM")

save_path = os.path.join('/Users/kamilakunes/Desktop/Rings', "ringPCM15.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

plt.figure(3,figsize=(16, 6))
plt.subplot(1, 2, 1)
plt.plot(x14, y14, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,4) - 0.9 um Gap")

plt.subplot(1, 2, 2)
plt.plot(xPCM14, yPCM14, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,4) - 0.9 um Gap with PCM")

save_path = os.path.join('/Users/kamilakunes/Desktop/Rings', "ringPCM14.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

plt.figure(4,figsize=(16, 6))
plt.subplot(1, 2, 1)
plt.plot(x13, y13, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,3) - 0.95 um Gap")

plt.subplot(1, 2, 2)
plt.plot(xPCM13, yPCM13, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,3) - 0.95 um Gap with PCM")

save_path = os.path.join('/Users/kamilakunes/Desktop/Rings', "ringPCM13.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

plt.figure(5,figsize=(16, 6))
plt.subplot(1, 2, 1)
plt.plot(x12, y12, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,2) - 1.0 um Gap")

plt.subplot(1, 2, 2)
plt.plot(xPCM12, yPCM12, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,2) - 1.0 um Gap with PCM")

save_path = os.path.join('/Users/kamilakunes/Desktop/Rings', "ringPCM12.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()

plt.figure(6,figsize=(16, 6))
plt.subplot(1, 2, 1)
plt.plot(x11, y11, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,1) - 1.1 um Gap")

plt.subplot(1, 2, 2)
plt.plot(xPCM11, yPCM11, linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Ring (1,1) - 1.1 um Gap with PCM")

save_path = os.path.join('/Users/kamilakunes/Desktop/Rings', "ringPCM11.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")
plt.show()
