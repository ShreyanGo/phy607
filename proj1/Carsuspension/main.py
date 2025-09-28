from carsus import solve_suspension, create_plots, print_results

def main():
    """Run car suspension ODE analysis"""
    
    # Solve the ODE using all methods
    results = solve_suspension()
    
    # Unpack results
    (time, 
     disp_euler, vel_euler, acc_euler,
     disp_rk4, vel_rk4, acc_rk4,
     disp_scipy, vel_scipy, acc_scipy,
     error_euler, error_rk4) = results
    
    # numerical results
    print_results(time, disp_euler, vel_euler, acc_euler, 
                 disp_rk4, vel_rk4, acc_rk4,
                 disp_scipy, vel_scipy, acc_scipy,
                 error_euler, error_rk4)
    
    # plots
    create_plots(time, disp_euler, vel_euler, acc_euler, 
                disp_rk4, vel_rk4, acc_rk4,
                disp_scipy, vel_scipy, acc_scipy,
                error_euler, error_rk4)

if __name__ == "__main__":
    main()