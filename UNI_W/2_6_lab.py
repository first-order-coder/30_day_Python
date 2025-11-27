import math
#Lab data
L_values = {"L1":[7.25, 3.04e-3],
            "L2":[9.25, 3.79e-3],
            "L3":[11.75, 4.74e-3]}

C_values = {"C1":[3.44, 4.56e-3],
            "C2":[4.55, 6.0e-3],
            "C3":[7.55, 9.97e-3]}

Z_values = {"Z1":[5.42, 3.12e-3],
            "Z2":[7.02, 3.92e-3],
            "Z3":[10.5, 5.70e-3]}


R_coil_measured = 503.0      # Ω, from ohmmeter
R_coil_given    = 501.6      # Ω, reference value
L_given         = 6.446
C_given = 4e-6

f = 51.08                    # Hz, measured frequency
df = 0.13                    # Hz, frequency error (±)
omega = 2 * math.pi * f


# calibration limit (in %)
calibration_limit = 0.1

# instrument ranges
I_range = 0.02   # A, ammeter 0–0.02 A
U_range = 20   # V, voltmeter 0–20 V
R_range = 2000  # Ω, ohmmeter 0–2000 Ω

def device_error(calibration_limit_percent, X0):
    delta_limit = (calibration_limit_percent / 100.0) * X0   # step 1
    sigma = delta_limit / 3.0                    # step 2
    return 1.96 * sigma                          # step 3

dI = device_error(calibration_limit, I_range)
dU = device_error(calibration_limit, U_range)
dR = device_error(calibration_limit, R_range)

print("ΔI =", dI, "A")   # ≈ 0.0000131 A
print("ΔU =", dU, "V")   # ≈ 0.0131 V
print("ΔR =", dR, "Ω")   # ≈ 1.3067 Ω

relative_resistance_error = (dR / R_coil_measured) * 100
relative_frequency_error = (df / f) * 100

print(f'Relative resistance error = ', "{:.4f}".format(relative_resistance_error))
print(f'Relative frequency error = ', '{:.4f}'.format(relative_frequency_error))

impedances_L = []
impedances_C = []
def impedance_measurement(voltage_L:float, voltage_C:float, current_L:float, current_C:float,):
    impedance_L = voltage_L / current_L
    impedance_C = voltage_C / current_C
    impedances_L.append(impedance_L)
    impedances_C.append(impedance_C)
    return impedances_C, impedances_L

reactances_L = []
reactances_C = []
def reactance_measurement(impedance_ZL:float,impedance_ZC:float, capacitance=C_given, resistance=R_coil_given):
    reactance_L = math.sqrt((impedance_ZL **2) - (resistance **2))
    reactance_C = math.sqrt((impedance_ZC **2) - (capacitance **2))
    reactances_L.append(reactance_L)
    reactances_C.append(reactance_C)
    return reactances_C,  reactances_L

inductances = []
capacitances = []
def inductance_measurement(reactance_L:float, reactance_C, frequency_val=f):
    inductance = reactance_L / (2*math.pi*frequency_val)
    capacitance = 1 / (2*math.pi*frequency_val*reactance_C)
    inductances.append(inductance)
    capacitances.append(capacitance)
    return inductances, capacitances

phasors_L = []
def phasor_measurements(reactance_L:float, resistance=R_coil_given):
    phasor_L = math.degrees(math.atan(reactance_L/resistance))
    phasors_L.append(phasor_L)
    return phasors_L

pi_val = math.pi
partial_errors = []
def partial_error_inductance(voltage_L:float, current_L:float, resistance=R_coil_measured, frequencey=f, V_abs=dU, I_abs=dI, R_abs=1.306, delta_F=df):
    dL_U = (2*voltage_L*V_abs)/(2*pi_val*f*current_L*2*(math.sqrt(voltage_L **2 - (resistance **2 * current_L ** 2))))
    dL_I = (1 / (2 * pi_val * frequencey * (current_L ** 2))) * (-(voltage_L ** 2) / math.sqrt(voltage_L ** 2 - (resistance ** 2) * (current_L ** 2))) * I_abs
    dL_R = ((-1) * resistance *current_L * R_abs) /((2 * pi_val * frequencey) *  (math.sqrt(voltage_L **2 - ((resistance **2) * (current_L **2)))))
    dL_f = (math.sqrt(voltage_L ** 2 - (resistance ** 2) * (current_L ** 2)) / (2 * pi_val * current_L)) * (-1 / (frequencey ** 2)) * delta_F 

    dL_abs = math.sqrt((dL_U **2) + (dL_I **2) + (dL_R **2)+ (dL_f **2)) 

    partial_errors.append(dL_U)
    partial_errors.append(dL_I)
    partial_errors.append(dL_R)
    partial_errors.append(dL_f)
    partial_errors.append(dL_abs)
    return partial_errors

partial_errors_C = []
def partial_error_inductance_C(voltage_C:float, current_C:float, frequencey=f, V_abs=dU, I_abs=dI, R_abs=dR, delta_F=df):
    dC_U = -(current_C * V_abs) / (2*pi_val*frequencey*(voltage_C **2))
    dC_I = I_abs / (2 *pi_val * frequencey * voltage_C)
    dC_F = -(current_C * delta_F) / (2*pi_val*voltage_C*(frequencey **2))
    dC_abs = math.sqrt((dC_U **2) + (dC_I **2) + (dC_F **2)) 

    partial_errors_C.append(dC_U)
    partial_errors_C.append(dC_I)
    partial_errors_C.append(dC_F)
    partial_errors_C.append(dC_abs)
    return partial_errors_C


for i in range(0,3):
    partial_error_inductance(L_values[f"L{i+1}"][0], L_values[f"L{i+1}"][1])
    partial_error_inductance_C(C_values[f"C{i+1}"][0], C_values[f"C{i+1}"][1])


for i in range(0,3):
    impedance_measurement(L_values[f"L{i+1}"][0], C_values[f"C{i+1}"][0], L_values[f"L{i+1}"][1], C_values[f"C{i+1}"][1])
    reactance_measurement(impedances_L[i], impedances_C[i])
    inductance_measurement(reactances_L[i], reactances_C[i])
    phasor_measurements(reactances_L[i])

    
for i in range(0,3):
    print(f"ZL_{i+1}=","{:.3f}".format(impedances_L[i]))
    print(f"XL_{i+1}=","{:.3f}".format(reactances_L[i]))
    print(f"L{i+1}=","{:.3f}".format(inductances[i]))
    print(f"Φ_L{i+1}=",90)

    print(f"ZC_{i+1}=","{:.3f}".format(impedances_C[i]))
    print(f"XC_{i+1}=","{:.3f}".format(reactances_C[i]))
    print(f"C{i+1}=","%.4E"%(capacitances[i]))
    print(f"Φ_C{i+1}=",90)

for i in range(0,15):
    print(partial_errors[i])

print("--------------")

for i in range(0,12):
    print(f"{(partial_errors_C[i] / 1e-6) :.8f}e-06")

Z = math.sqrt((R_coil_given **2) +((2*pi_val*f*L_given - (1/(2*pi_val*f*C_given)))**2))
print(Z)

phase = math.atan(((2*pi_val*f*L_given) - (1/(2*pi_val*f*C_given)))/R_coil_given)
print(math.degrees(phase))

for i in range(0, 3):
    Zexperimental= Z_values[f"Z{i+1}"][0] / Z_values[f"Z{i+1}"][1]
    print(f"Zexperimental{i+1}: {Zexperimental}")

relative_errors_L = []
relative_errors_C = []

for i in range(3):
    # ΔL for this measurement is every 5th element: indices 4, 9, 14
    delta_L = partial_errors[4 + 5 * i]
    L_val = inductances[i]
    epsilon_L = (delta_L / L_val) * 100.0
    relative_errors_L.append(epsilon_L)

    # ΔC for this measurement is every 4th element: indices 3, 7, 11
    delta_C = partial_errors_C[3 + 4 * i]
    C_val = capacitances[i]
    epsilon_C = (delta_C / C_val) * 100.0
    relative_errors_C.append(epsilon_C)

print("Relative errors for inductance (L):")
for i in range(3):
    print(f"ε_L{i+1} = {relative_errors_L[i]:.3f}")

print("Relative errors for capacitance (C):")
for i in range(3):
    print(f"ε_C{i+1} = {relative_errors_C[i]:.3f}")