import numpy as np

Vs1 = 20
Ri = 1000
R_Loads = [100, 200, 500, 800, 900, 1000, 1100, 1200, 1500, 2000, 5000, 10000]

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

#Figure 1
# for RL in range(0,len(R_Loads)):
#     R_Load = R_Loads[RL] 
#     V_Load = (R_Load / (R_Load + Ri))*Vs1
#     print(f"When R_Load is: {R_Loads[RL]}(Ohms) V_Load is: {V_Load}(V)")



'''
#Figure 2

R = np.array([[4.5, -2,     0],
             [-2,  8.7,  -3.3],
             [0,  -3.3,   4.9]])
 
V = np.array([[0.02],
              [0],
              [-0.005]])

I = np.linalg.solve(R,V)
IA = round((I[0].item())*1000, 3)
IB = round((I[1].item())*1000, 3)
IC = round((I[2].item())*1000, 3)

print(f'IA = {IA} mA')
print(f'IA = {IB} mA')
print(f'IA = {IC} mA')

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
print(f'I4 = {I4} mA')
print(f'I5 = {I5} mA')
print(f'I6 = {I6} mA')


VR1 = I1 *0.001 * R1
VR2 = I2 *0.001 * R2
VR3 = I3 *0.001 * R3
VR4 = I4 *0.001 * R4
VR5 = I5 *0.001 * R5
VR6 = I6 *0.001 * R6
VRi1 = I1 *0.001 * Ri1
VRi2 = I5 *0.001 * Ri2

print("")
print(f'VR1= {VR1}(v)')
print(f'VR2= {VR2}(v)')
print(f'VR3= {VR3}(v)')
print(f'VR4= {VR4}(v)')
print(f'VR5= {VR5}(v)')
print(f'VR6= {VR6}(v)')
print(f'VRi1= {VRi1}(v)')
print(f'VRi2= {VRi2}(v)')

'''
#Figure 3
I_total = 20 / (Ri1 + R1 + R3 + R5 + Ri2 + R6)
print(f'I_total= {round(I_total*1000, 3)}mA')

V12 = Vs1 - (R1 + Ri1) * I_total
print(f'V12= {round(V12, 3)}(v)')

V34 = (R5 + Ri2) * I_total
print(f'V34= {round(V34, 3)}(v)')

#Figure 4
'''
R = np.array([[4.5, -2,     0],
             [-2,  8.7,  -3.3],
             [0,  -3.3,   4.9]])
 
V = np.array([[0.02],
              [0],
              [0]])

I = np.linalg.solve(R,V)
IA = round((I[0].item())*1000, 3)
IB = round((I[1].item())*1000, 3)
IC = round((I[2].item())*1000, 3)

print(f'IA = {IA} mA')
print(f'IA = {IB} mA')
print(f'IA = {IC} mA')

I1 = IA
I2 = IA - IB
I3 = IB
I4 = IB - IC
I5 = IC
I6 = IB

print('')
print(f'I2 = {I2} mA')
print(f'I4 = {I4} mA')

V12 = I2 *0.001 * R2
V34 = I4 *0.001 * R4

print("")
print(f'V12= {VR12}(v)')
print(f'V34= {VR34}(v)')

'''