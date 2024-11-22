import numpy as np

Ri1 = 1000
Ri2 = 100
R1 = 1500
R2 = 2000
R3 = 2400
R4 = 3300
R5 = 1500
R6 = 1000
Vs1 = 20
Vs2 = 5

G1 = 1/(R1+Ri1)
G2 = 1/R2
G3 = 1/R3
G4 = 1/R4
G5 = 1/(R5+Ri2)
G6 = 1/R6


#node analysis
'''G = np.array([[G1+G2+G6,         0,          -(G6)],
             [        0,  (G4+G5+G3),     -(G4+G5)],
             [      -(G6),  -(G4+G5),   (G4+G5+G6)]])
 
I = np.array([[-Vs1*G1],
              [Vs2*G5],
              [-Vs2*G5]])

node_V = np.linalg.solve(G,I)
V2 = round((node_V[0].item()), 4)
V3 = round((node_V[1].item()), 4)
V4 = round((node_V[2].item()), 5)

print(f'V2 = {V2} v')
print(f'V3 = {V3} v')
print(f'V4 = {V4} v')

I1 = (Vs1+V2)/(R1+Ri1)
I2 = -V2/R2
I3 = -(V3)/R3
I4 = (V3-V4)/R4
I5 = (V3-V4-Vs2)/(Ri2+R5)
I6 = V4-V2/R6

print('')
print(f'I1 = {I1*1000} mA')
print(f'I2 = {I2*1000} mA')
print(f'I3 = {I3*1000000} uA')
print(f'I4 = {I4*1000} mA')
print(f'I5 = {I5*1000000} uA')
print(f'I6 = {I6*1000000} uA')'''

#mesh analysis

# R = np.array([[4.5, -2,     0],
#              [-2,  8.7,  -3.3],
#              [0,  -3.3,   4.9]])
 
# V = np.array([[0.02],
#               [0],
#               [-0.005]])

# I = np.linalg.solve(R,V)
# IA = round((I[0].item())*1000, 3)
# IB = round((I[1].item())*1000, 3)
# IC = round((I[2].item())*1000, 3)

# print(f'IA = {IA} mA')
# print(f'IB = {IB} mA')
# print(f'IC = {IC} mA')

# I1 = IA
# I2 = IA - IB
# I3 = IB
# I4 = IB - IC
# I5 = IC
# I6 = IB

# print('')
# print(f'I1 = {I1} mA')
# print(f'I2 = {I2} mA')
# print(f'I3 = {I3} mA')
# print(f'I4 = {I4} mA')
# print(f'I5 = {I5} mA')
# print(f'I6 = {I6} mA')


# VR1 = I1 *0.001 * R1
# VR2 = I2 *0.001 * R2
# VR3 = I3 *0.001 * R3
# VR4 = I4 *0.001 * R4
# VR5 = I5 *0.001 * R5
# VR6 = I6 *0.001 * R6
# VRi1 = I1 *0.001 * Ri1
# VRi2 = I5 *0.001 * Ri2

# print("")
# print(f'V1_node= {VR2}(v)')
# print(f'V3_node= {VR6 + VR4}(v)')
# print(f'V4_node= {VR6}(v)')

#mesh for short circuit
'''R = np.array([[3, -2,     0],
             [-2,  8.7,  -3.3],
             [0,  -3.3,   4.9]])
 
V = np.array([[0.02],
              [0],
              [-0.005]])

I = np.linalg.solve(R,V)
IA = round((I[0].item())*1000, 3)
IB = round((I[1].item())*1000, 3)
IC = round((I[2].item())*1000, 3)

Isc = IA

print(f'Isc = {Isc} mA')'''


#node analysis - open circuit
# G = np.array([[G2+G6,   0,                -G6],
#              [     0,   G3+G4+G5,    -(G4+G5)],
#              [   -G6,  -(G4+G5),   (G4+G5+G6)]])
 
# I = np.array([[0],
#               [Vs2*G5],
#               [-Vs2*G5]])

# node_V = np.linalg.solve(G,I)
# V2 = round((node_V[0].item()), 4)
# V3 = round((node_V[1].item()), 4)
# V4 = round((node_V[2].item()), 4)

# I1 = 0
# I2 = -V2/R2
# I3 = (-V3)/R3
# I4 = (V3-V4)/R4
# I5 = (V3-V4-Vs2)/(Ri2+R5)
# I6 = V4-V2/R6

# Voc = Vs1+V2
# print(f'Voc= {Voc} V')

#Thevenin Equivalent Resistance
'''R_thevenin = Voc/Isc
print(f'R_thevenin= {R_thevenin} Kilo ohms')'''

#mesh for Us1 acting alone
# R = np.array([[4.5, -2,     0],
#              [-2,  8.7,  -3.3],
#              [0,  -3.3,   4.9]])
 
# V = np.array([[0.02],
#               [0],
#               [0]])

# I = np.linalg.solve(R,V)
# IA = round((I[0].item())*1000, 5)
# IB = round((I[1].item())*1000, 5)
# IC = round((I[2].item())*1000, 5)

# print(f'IA = {IA} mA')
# print(f'IB = {IB} mA')
# print(f'IC = {IC} mA')

# I1 = IA
# I2 = IA - IB
# I3 = IB
# I4 = IB - IC
# I5 = IC
# I6 = IB

# print('')
# print(f'I1 = {I1} mA')
# print(f'I2 = {I2} mA')
# print(f'I3 = {I3} mA')
# print(f'I4 = {I4*1000} uA')
# print(f'I5 = {I5} mA')
# print(f'I6 = {I6} mA')

# VR3 = I3 *0.001 * R3
# print(f'VR3= {VR3} v')

#mesh for Us2 acting alone
'''R = np.array([[4.5, -2,     0],
             [-2,  8.7,  -3.3],
             [0,  -3.3,   4.9]])
 
V = np.array([[0],
              [0],
              [-0.005]])

I = np.linalg.solve(R,V)
IA = round((I[0].item())*1000, 5)
IB = round((I[1].item())*1000, 5)
IC = round((I[2].item())*1000, 5)

print(f'IA = {IA} mA')
print(f'IB = {IB} mA')
print(f'IC = {IC} mA')

I1 = IA
I2 = IA - IB
I3 = IB
I4 = IB - IC
I5 = IC
I6 = IB

print('')
print(f'I1 = {I1*1000} uA')
print(f'I2 = {I2*1000} uA')
print(f'I3 = {I3*1000} uA')
print(f'I4 = {I4*1000} uA')
print(f'I5 = {I5} mA')
print(f'I6 = {I6*1000} uA')

VR3 = I3 *0.001 * R3
print(f'VR3= {VR3} v')'''

#3.4 Us1 and UR3
R = np.array([[4.5, -2,     0],
             [-2,  6.3,  -3.3],
             [0,  -3.3,   4.9]])
 
V = np.array([[0.02],
              [-3.8172*0.001],
              [0]])

I = np.linalg.solve(R,V)
IA = round((I[0].item())*1000, 5)
IB = round((I[1].item())*1000, 5)
IC = round((I[2].item())*1000, 5)

print(f'IA = {IA} mA')
print(f'IB = {IB} mA')
print(f'IC = {IC} mA')

I1 = IA
I2 = IA - IB
I3 = IB
I4 = IB - IC
I5 = IC
I6 = IB

print('')
print(f'I1 = {I1} mA')
print(f'I2 = {I2} mA')
print(f'I3 = {I3} mA')
print(f'I4 = {I4*1000} uA')
print(f'I5 = {I5} mA')
print(f'I6 = {I6} mA')
