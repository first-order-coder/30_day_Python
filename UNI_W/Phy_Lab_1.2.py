import math

# def v_theor(h):
#     v_theor_val = math.sqrt((2*8.4*9.81*1000*h)/((122.2) + 8.4))
#     print(v_theor_val)

# def v_exp(H, t_avg):
#     v_exp_val = H / t_avg
#     print(v_exp_val)

# vals = [240, 260, 310, 360, 160, 110, 280]
# for val in vals:
#     v_theor(val)

# print('------')

# t_avg_vals = [0.503, 0.413, 0.270, 0.178, 0.817, 1.232, 0.354]
# H_vals = [220, 200, 150, 100, 300, 350, 180]

# for H_val,t_val in zip(H_vals,t_avg_vals):
#     v_exp(H_val, t_val)    

# #3.3 phys_2_lab
# angles = [math.radians(1.7),math.radians(1.55), math.radians(1.82),math.radians(1.86),math.radians(3.7),math.radians(3.68),math.radians(-1.01),math.radians(-1.28),math.radians(-1.33),math.radians(-2.45),math.radians(-2),math.radians(-2.39)]
# lengths = [435e-9, 546e-9, 579e-9,435e-9, 546e-9, 579e-9,435e-9, 546e-9, 579e-9,435e-9, 546e-9, 579e-9]
# k_s = [1,1,1,2,2,2,-1,-1,-1,-2,-2,-2]

# for length, k, angle in zip(lengths, k_s, angles):
#     print(k *length * ((math.cos(angle)/ math.sin(angle))*(1 / math.sin(angle))) * 0.0114)

# d_val = [0.401, 0.333, 0.29, 0.24, 0.22, 0.18, 0.14]
# g = 9.80665
# T_vals = [1.3112,1.2222,1.0914,1.0365,0.9642,0.8819,0.8236]

# for d,T in zip(d_val, T_vals):
#     T_theor = 2 * math.pi * (math.sqrt(d / g))
#     # print(T_theor)
#     # print(f'diff for {1 + T_vals.index(T)}: {T - T_theor}')
#     print(f' percentage: {((T - T_theor) / T_theor) * 100}')


# V_vals = [94, 100, 118]
# I_vals = [0.022, 0.024, 0.028]

# for I,V in zip(I_vals, V_vals):
#     L_V = (1/(math.pi * 100 * I)) * (V * 0.98 /(math.sqrt((V*V) - (I*I * (1073)*(1073)))))
#     L_I = (1/(math.pi * 100 * I * I)) * (-V * V * 0.000653 /(math.sqrt((V*V) - (I*I * (1073)*(1073)))))
#     L_R = (-1/(math.pi * 100)) * ((1073 * I * 6.53) /(math.sqrt((V*V) - (I*I * (1073)*(1073)))))
#     L_F = -((math.sqrt((V*V) - (I*I * (1073)*(1073)))) / (math.pi * I * 2 * 2500)) * 0.2
    # print(L_V)
    # print(L_I)
    # print('0------')
    # print(L_R)
    # print(L_V)

    # value = math.sqrt(L_V*L_V + L_I * L_I + L_R * L_R + L_F * L_F)
    # print(value)

# V_vals = [32, 45, 69]
# I_vals = [0.042, 0.059, 0.084]

# for I,V in zip(I_vals, V_vals):
#     C_V = (-I * 0.98 / (2 *math.pi * 50 * V * V))
#     C_I = 0.000653 / (2 *math.pi * 50 * V)
#     C_F = -(I * 0.2) / (2 *math.pi * 2500 * V)
#     # print(C_V)
#     # print(C_I)
#     # print(C_F)

#     value = math.sqrt(C_V*C_V + C_I * C_I + C_F * C_F)
#     print(value)

# value = (2*math.pi*50*12.989) - (1/(2*math.pi*50*4e-6))
# Z = math.sqrt((981.9 * 981.9) + (value * value))
# print(Z)
# print(2*math.pi*50*12.989)
# print(1/(2*math.pi*50*4e-6))

# S = 1.879e-6
# sigma = 5.7e-8
# powers = [132, 192, 260, 360, 448, 544, 648, 760, 880, 1440]

# for p in powers:
#     T = ((p * 0.001) / (sigma * S)) ** (1/4)
#     print(T)

VCC = 9 #supply voltage 
VBE = 0.7 #forward bias voltage of transistor Q1

#from Task 1, at Q point
IC = 7.2e-3
IB = 35e-6
Beta = round(IC / IB)
VCE = 6.06
IE = IC #Ie = Ic since Ib is so small

#According to theory
VE = VCC / 10 
RE = VE / IC
print(f'RE = {round(RE, 2)} ohms') #round up to 2 digits using built in round function

RC = (VCC - VE - VCE) / IC
print(f'RC = {round(RC, 2)} ohms')

VC = VCE + VE
# print(f'{VC} volts')

R1 = (VCC - VBE - VE) / IB
print(f'R1 = {round(R1/1000, 2)} kilo ohms')

VB = VBE + VE
R2 = (VB * R1) / (VCC - VB)
print(f'R2 = {round(R2/1000, 2)} kilo ohms')