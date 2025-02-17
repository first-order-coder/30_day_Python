import numpy as np
import matplotlib.pyplot as plt

# Original Hg calibration data as provided (wavelengths and corresponding angles)
wavelengths_hg_orig = np.array([690.7, 671.6, 623.6, 612.3, 579, 577, 567.6, 546.1, 512.1, 496.2, 491.6, 435.8, 434.7, 433.9, 407.8, 404.7])
angles_hg_orig = np.array([3208, 3148, 2972, 2928, 2768, 2758, 2708, 2580, 2258, 2200, 2160, 1498, 1480, 1468, 1010, 946])

# Reverse the Hg data so that the monochromator angles are in ascending order,
# which pairs the smallest angle with the smallest wavelength.
wavelengths_hg = wavelengths_hg_orig[::-1]  # Now in ascending order: 404.7 ... 690.7
angles_hg = angles_hg_orig[::-1]            # Now in ascending order: 946 ... 3208

# Fit a quadratic polynomial: wavelength = f(angle)
coeffs = np.polyfit(angles_hg, wavelengths_hg, 2)

# Test light source Ne data: provided monochromator angles (in descending order)
angles_ne_orig = np.array([3244, 3214, 3150, 3136, 3110, 3086, 3078, 3038, 3042, 3012, 3000, 2986, 2966, 2942, 2934, 2914, 2906])
# Reverse (or sort) the Ne angles so they are in ascending order
angles_ne = np.sort(angles_ne_orig)

# Calculate corresponding wavelengths for Ne data using the calibration polynomial
wavelengths_ne = np.polyval(coeffs, angles_ne)

# Plotting the calibration curve and the test data
plt.figure(figsize=(10, 6))
plt.plot(wavelengths_hg, angles_hg, 'bo-', label='Hg Calibration Data')
plt.plot(wavelengths_ne, angles_ne, 'rs-', label='Ne Test Data (calculated wavelengths)')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Monochromator Angle (°)')
plt.title('Monochromator Calibration Curve and Ne Test Data')
plt.grid(True)
plt.legend()

# Optionally, annotate the Ne points with their computed wavelengths
for wl, ang in zip(wavelengths_ne, angles_ne):
    plt.annotate(f'{wl:.1f}', (wl, ang), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()
