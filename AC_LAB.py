Vs1 = 20
Ri = 1000
R_Loads = [100, 200, 500, 800, 900, 1000, 1100, 1200, 1500, 2000, 5000, 10000]


for RL in range(0,len(R_Loads)):
    R_Load = R_Loads[RL] 
    V_Load = (R_Load / (R_Load + Ri))*Vs1
    print(f"When R_Load is: {R_Loads[RL]}(Ohms) V_Load is: {V_Load}(V)")
