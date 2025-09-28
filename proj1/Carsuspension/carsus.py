
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Car suspension parameters
m = 1500.0    # mass (kg)
c2 = 100.0    # acceleration damping coefficient (kg*s)
c1 = 2000.0   # velocity damping coefficient (kg/s)
c0 = 15000.0  # spring constant (kg/s²)

# Initial conditions
y0 = 0.1      # initial displacement (m)
v0 = 0.0      # initial velocity (m/s)
a0 = 0.0      # initial acceleration (m/s²)

# Simulation parameters
t_max = 2.0   # simulation time (s)
dt = 0.01     # time step (s)

# Calculate number of steps
num_steps = int(t_max / dt)

def calculate_jerk(y, v, a):
    """
    Calculate the jerk (third derivative) from the ODE:
    m * d³y/dt³ + c2 * d²y/dt² + c1 * dy/dt + c0 * y = 0
    Solving for d³y/dt³: d³y/dt³ = -(c2 * d²y/dt² + c1 * dy/dt + c0 * y) / m
    """
    return -(c2 * a + c1 * v + c0 * y) / m

def ode_system(t, state):
    """
    ODE system for SciPy solve_ivp
    state = [y, v, a] = [displacement, velocity, acceleration]
    """
    y, v, a = state
    jerk = calculate_jerk(y, v, a)
    return [v, a, jerk]

def solve_suspension():
    """Main function to solve car suspension ODE"""
    
    # Arrays to store results
    time = np.zeros(num_steps)
    displacement_euler = np.zeros(num_steps)
    velocity_euler = np.zeros(num_steps)
    acceleration_euler = np.zeros(num_steps)

    displacement_rk4 = np.zeros(num_steps)
    velocity_rk4 = np.zeros(num_steps)
    acceleration_rk4 = np.zeros(num_steps)

    # Set initial conditions
    time[0] = 0.0
    displacement_euler[0] = y0
    velocity_euler[0] = v0
    acceleration_euler[0] = a0

    displacement_rk4[0] = y0
    velocity_rk4[0] = v0
    acceleration_rk4[0] = a0

    # Euler method simulation
    for i in range(1, num_steps):
        time[i] = time[i-1] + dt
        
        # Calculate jerk at current state
        jerk = calculate_jerk(displacement_euler[i-1], velocity_euler[i-1], acceleration_euler[i-1])
        
        # Update using Euler method
        displacement_euler[i] = displacement_euler[i-1] + velocity_euler[i-1] * dt
        velocity_euler[i] = velocity_euler[i-1] + acceleration_euler[i-1] * dt
        acceleration_euler[i] = acceleration_euler[i-1] + jerk * dt

    # Runge-Kutta method simulation  
    for i in range(1, num_steps):
        y = displacement_rk4[i-1]
        v = velocity_rk4[i-1]
        a = acceleration_rk4[i-1]
        
        # k1 values
        k1_y = v
        k1_v = a
        k1_a = calculate_jerk(y, v, a)
        
        # k2 values
        y_k2 = y + k1_y * dt/2
        v_k2 = v + k1_v * dt/2
        a_k2 = a + k1_a * dt/2
        k2_y = v_k2
        k2_v = a_k2
        k2_a = calculate_jerk(y_k2, v_k2, a_k2)
        
        # k3 values
        y_k3 = y + k2_y * dt/2
        v_k3 = v + k2_v * dt/2
        a_k3 = a + k2_a * dt/2
        k3_y = v_k3
        k3_v = a_k3
        k3_a = calculate_jerk(y_k3, v_k3, a_k3)
        
        # k4 values
        y_k4 = y + k3_y * dt
        v_k4 = v + k3_v * dt
        a_k4 = a + k3_a * dt
        k4_y = v_k4
        k4_v = a_k4
        k4_a = calculate_jerk(y_k4, v_k4, a_k4)
        
        # Final RK4 update
        displacement_rk4[i] = y + (k1_y + 2*k2_y + 2*k3_y + k4_y) * dt/6
        velocity_rk4[i] = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) * dt/6
        acceleration_rk4[i] = a + (k1_a + 2*k2_a + 2*k3_a + k4_a) * dt/6

    # SciPy solve_ivp for comparison
    initial_state = [y0, v0, a0]
    t_span = (0, t_max)
    t_eval = time

    sol = solve_ivp(ode_system, t_span, initial_state, t_eval=t_eval, 
                    method='RK45', rtol=1e-8, atol=1e-11)

    displacement_scipy = sol.y[0]
    velocity_scipy = sol.y[1]
    acceleration_scipy = sol.y[2]

    # Calculate errors
    error_euler_disp = np.abs(displacement_euler - displacement_scipy)
    error_rk4_disp = np.abs(displacement_rk4 - displacement_scipy)

    return (time, 
            displacement_euler, velocity_euler, acceleration_euler,
            displacement_rk4, velocity_rk4, acceleration_rk4,
            displacement_scipy, velocity_scipy, acceleration_scipy,
            error_euler_disp, error_rk4_disp)

def create_plots(time, disp_euler, vel_euler, acc_euler, 
                disp_rk4, vel_rk4, acc_rk4,
                disp_scipy, vel_scipy, acc_scipy,
                error_euler, error_rk4):
    """Create all plots"""
    
    # Main comparison plots
    plt.figure(figsize=(12, 8))

    # Plot 1: Displacement
    plt.subplot(2, 2, 1)
    plt.plot(time, disp_euler, 'r--', label='Euler Method', linewidth=2)
    plt.plot(time, disp_rk4, 'b-', label='4th Order RK', linewidth=2)
    plt.plot(time, disp_scipy, 'g-.', label='SciPy solve_ivp', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Displacement vs Time')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot 2: Velocity
    plt.subplot(2, 2, 2)
    plt.plot(time, vel_euler, 'r--', label='Euler Method', linewidth=2)
    plt.plot(time, vel_rk4, 'b-', label='4th Order RK', linewidth=2)
    plt.plot(time, vel_scipy, 'g-.', label='SciPy solve_ivp', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot 3: Acceleration
    plt.subplot(2, 2, 3)
    plt.plot(time, acc_euler, 'r--', label='Euler Method', linewidth=2)
    plt.plot(time, acc_rk4, 'b-', label='4th Order RK', linewidth=2)
    plt.plot(time, acc_scipy, 'g-.', label='SciPy solve_ivp', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.title('Acceleration vs Time')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Plot 4: Error comparison
    plt.subplot(2, 2, 4)
    plt.semilogy(time, error_euler, 'r-', label='Euler Error', linewidth=2)
    plt.semilogy(time, error_rk4, 'b-', label='RK4 Error', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Absolute Error (m)')
    plt.title('Error Analysis')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.suptitle('Car Suspension System Analysis\n',
                 fontsize=14)
    plt.tight_layout()
    plt.show()

def print_results(time, disp_euler, vel_euler, acc_euler, 
                 disp_rk4, vel_rk4, acc_rk4,
                 disp_scipy, vel_scipy, acc_scipy,
                 error_euler, error_rk4):
    """Print numerical results summary"""
    
    print("Final displacement:")
    print(f"  Euler method: {disp_euler[-1]:.6f} m")
    print(f"  RK4 method: {disp_rk4[-1]:.6f} m")
    print(f"  SciPy: {disp_scipy[-1]:.6f} m")

    print(f"\nError analysis:")
    print(f"  Euler - Max error: {np.max(error_euler):.2e} m")
    print(f"  Euler - Mean error: {np.mean(error_euler):.2e} m")
    print(f"  RK4 - Max error: {np.max(error_rk4):.2e} m")
    print(f"  RK4 - Mean error: {np.mean(error_rk4):.2e} m")

    accuracy_ratio = np.max(error_euler) / np.max(error_rk4)
    print(f"\nRK4 is {accuracy_ratio:.1f}x more accurate than Euler for this step size")