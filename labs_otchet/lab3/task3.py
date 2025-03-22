#print((1132226527 % 70)+1)
import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def mixed_combat(t, y):
    x, y = y 
    dxdt = -0.39 * x - 0.91 * y + abs(np.sin(2 * t))
    dydt = -0.54 * x * y - 0.29 * y + abs(np.cos(6 * t))
    return [dxdt, dydt]


x0 = 84000
y0 = 61000  
y0_vec = [x0, y0]  

t_span = (0, 10)  
t_eval = np.linspace(0, 10, 1000)  


sol = solve_ivp(mixed_combat, t_span, y0_vec, t_eval=t_eval)


plt.plot(sol.t, sol.y[0], label='Армия X')
plt.plot(sol.t, sol.y[1], label='Армия Y')
plt.xlabel('Время (дни)')
plt.ylabel('Численность войск')
plt.legend()
plt.title('Модель боевых действий с участием регулярных войск и партизанских отрядов')
plt.grid()
plt.show()