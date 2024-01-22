#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

# Define parameters for the simulation
num_samples = 1000
mach_numbers = np.linspace(1.5, 10, num_samples)  # Hypersonic range
angles_of_attack = np.linspace(0, 45, num_samples)  # Degrees
wall_temperatures = np.linspace(300, 1500, num_samples)  # Kelvin

# Generate synthetic temperature and pressure data
# These functions are placeholders and do not represent real physics accurately.
def generate_temperature(mach, angle_of_attack, wall_temp):
    return wall_temp * (1 + 0.2 * mach * np.cos(np.radians(angle_of_attack)))

def generate_pressure(mach, angle_of_attack):
    return 101325 * (1 + 0.6 * mach * np.cos(np.radians(angle_of_attack)))  # Pa, simplistic model

temperatures = [generate_temperature(mach, aoa, wall_temp) for mach, aoa, wall_temp in zip(mach_numbers, angles_of_attack, wall_temperatures)]
pressures = [generate_pressure(mach, aoa) for mach, aoa in zip(mach_numbers, angles_of_attack)]

# Create a DataFrame
df = pd.DataFrame({
    'Mach Number': mach_numbers,
    'Angle of Attack': angles_of_attack,
    'Wall Temperature': wall_temperatures,
    'Temperature': temperatures,
    'Pressure': pressures
})

# Save to CSV
#csv_file_path = 'C:\Users\carmi\Documents\Python Scripts\h'
df.to_csv("hypersonic_flow_simulation_data.csv", index=False)

#csv_file_path


# In[5]:


pd.read_csv ("hypersonic_flow_simulation_data.csv")


# In[ ]:




