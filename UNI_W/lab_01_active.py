import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv(r"C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\UNI_W\network_data.csv")
df2 = pd.read_csv(r"C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\UNI_W\lt_spice_data.csv")

#crete a figure with 2 subplots arranged vertically 2 rows and 1 column 
#10 inch height and 8 inch width
#fig object represents the enitre figure and used to manage the overall figure
#this is subplots 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,8)) 

#for lt spice
lt_spice_filter = df2['Frequency (Hz)'].between(502, 1900000)
frequency_spice = df2.loc[lt_spice_filter, 'Frequency (Hz)']
ch1_mgtd_spice = df2.loc[lt_spice_filter, 'Magnitude (dB)']
ch2_phase_spice = df2.loc[lt_spice_filter, 'Phase (degrees)']

#for analog discovery
frequency_discovery = df1['Frequency (Hz)']
ch1_mgtd_discovery = df1['Channel 1 Magnitude (dB)']
ch2_mgtd_discovery = df1['Channel 2 Magnitude (dB)']
ch2_phase_discovery = df1['Channel 2 Phase (deg)']

ax1.semilogx(frequency_discovery, ch1_mgtd_discovery, label='Ch1_discovery', color='orange')
ax1.semilogx(frequency_discovery, ch2_mgtd_discovery, label='Ch2_discovery', color='blue')
ax1.semilogx(frequency_spice, ch1_mgtd_spice, label='Ch1_spice', color='green')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_xlabel('Frequency (Hz)')
ax1.legend()
ax1.grid(True)

ax2.semilogx(frequency_discovery, ch2_phase_discovery, label='Ch2_discovery')
ax2.semilogx(frequency_spice, ch2_phase_spice, label='Ch2_spice')
ax2.set_xlabel('Frequuency (Hz)')
ax2.set_ylabel('Phase angle (degrees)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()