import numpy as np
import matplotlib.pyplot as plt

R_EARTH = 6371  # km
ALTITUDE = 500  # km above Earth's surface
R_ORBIT = R_EARTH + ALTITUDE
T = 90 * 60  # Orbit period in seconds
omega = 2 * np.pi / T

t = np.linspace(0, T, 1000)
x = R_ORBIT * np.cos(omega * t)
y = R_ORBIT * np.sin(omega * t)

plt.figure(figsize=(8,8))
plt.plot(x, y, label='CubeSat Orbit')
plt.plot(0, 0, 'bo', label='Earth')
plt.xlabel('X (km)')
plt.ylabel('Y (km)')
plt.title('CubeSat Orbit Simulation')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
