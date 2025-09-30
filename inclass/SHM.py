import numpy as np
import matplotlib.pyplot as plt
import rungekutta as rk

# Claire O'Connor, Amelia Abruscato & Shreyan Goswami
# Integral Methods: Simple Harmonic Motion

# Debugging
msg_lvl = 5
def msg(lvl, msg):
    if msg_lvl < lvl:
        print(msg)

m = 1.0  # mass 
k = 10.0 # spring constant 
omega = np.sqrt(k / m) # angular freq

# Define simulation parameters
x0 = 5.0  # initial position 
v0 = 0.0  # initial velocity
t_max = 10.0 # simulation time 
dt = 0.01 # time step

# Calculate number of steps
num_steps = int(t_max / dt)

#arrays to store results
time = np.zeros(num_steps)
position = np.zeros(num_steps)
velocity = np.zeros(num_steps)
total_energy = np.zeros(num_steps)

# Set initial conditions
position[0] = x0
velocity[0] = v0

# Function to calculate acceleration
def calculate_acceleration(x):
    return -omega**2 * x

# Function to calculate total energy
def calculate_total_energy(x, v, m, k):
    kinetic_energy = 0.5 * m * v**2
    potential_energy = 0.5 * k * x**2
    return kinetic_energy + potential_energy

# Euler method simulation
for i in range(1, num_steps):
    time[i] = time[i-1] + dt

    # Calculate acceleration at current state
    a = calculate_acceleration(position[i-1])

    # Updated  position and velocity using Euler method
    velocity[i] = velocity[i-1] + a * dt
    position[i] = position[i-1] + velocity[i] * dt # Note: Using v[i-1] for position update

    # Calculate total energy
    total_energy[i] = calculate_total_energy(position[i], velocity[i], m, k)

# Plotting the total energy
show_Euler = True
if show_Euler:
    plt.figure(figsize=(8, 6))
    plt.plot(time, total_energy, label='Euler')
    plt.xlabel('Time (s)')
    plt.ylabel('Total Energy (J)')
    plt.title('Total Energy of SHM System (Euler Method)')
    plt.grid(True)
    #plt.legend()
    #plt.show()
    
# Runge Kutta method
time, pos, vel, PE, KE, total_energy = rk.RungeKutta(x0, v0, dt, t_max, m, k)
total_energy = np.array(total_energy)

# Plotting the total energy
show_RK = True
if show_RK:
    #plt.figure(figsize=(8, 6))
    plt.plot(time, total_energy, label='Runge Kutta')
    #plt.xlabel('Time (s)')
    #plt.ylabel('Total Energy (J)')
    #plt.title('Total Energy of SHM System (Runge Kutta Method)')
    #plt.grid(True)
    plt.legend()
    plt.show()

