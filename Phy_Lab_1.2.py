import math

def v_theor(h):
    v_theor_val = math.sqrt((2*8.4*9.81*1000*h)/((122.2) + 8.4))
    print(v_theor_val)

def v_exp(H, t_avg):
    v_exp_val = H / t_avg
    print(v_exp_val)

vals = [240, 260, 310, 360, 160, 110, 280]
for val in vals:
    v_theor(val)

print('------')

t_avg_vals = [0.503, 0.413, 0.270, 0.178, 0.817, 1.232, 0.354]
H_vals = [220, 200, 150, 100, 300, 350, 180]

for H_val,t_val in zip(H_vals,t_avg_vals):
    v_exp(H_val, t_val)    

#3.3 phys_2_lab
angles = [math.radians(1.7),math.radians(1.55), math.radians(1.82),math.radians(1.86),math.radians(3.7),math.radians(3.68),math.radians(-1.01),math.radians(-1.28),math.radians(-1.33),math.radians(-2.45),math.radians(-2),math.radians(-2.39)]
lengths = [435e-9, 546e-9, 579e-9,435e-9, 546e-9, 579e-9,435e-9, 546e-9, 579e-9,435e-9, 546e-9, 579e-9]
k_s = [1,1,1,2,2,2,-1,-1,-1,-2,-2,-2]

for length, k, angle in zip(lengths, k_s, angles):
    print(k *length * ((math.cos(angle)/ math.sin(angle))*(1 / math.sin(angle))) * 0.0114)

d_val = [0.401, 0.333, 0.29, 0.24, 0.22, 0.18, 0.14]
g = 9.80665
T_vals = [1.3112,1.2222,1.0914,1.0365,0.9642,0.8819,0.8236]

for d,T in zip(d_val, T_vals):
    T_theor = 2 * math.pi * (math.sqrt(d / g))
    # print(T_theor)
    # print(f'diff for {1 + T_vals.index(T)}: {T - T_theor}')
    print(f' percentage: {((T - T_theor) / T_theor) * 100}')