
from sininteg import solve_integration, create_plots, print_results

def main():
    """Run numerical integration analysis"""
    
    # Solve integration using all methods
    results = solve_integration()
    
    # Unpack results
    (riemann_result, trapezoidal_result, simpson_result, numpy_trapz, scipy_quad,
     riemann_error, trapezoidal_error, simpson_error, numpy_error, quad_error) = results
    
    # Print numerical results first
    print_results(riemann_result, trapezoidal_result, simpson_result, numpy_trapz, scipy_quad,
                 riemann_error, trapezoidal_error, simpson_error, numpy_error, quad_error)
    
    # Then create plots
    create_plots(riemann_result, trapezoidal_result, simpson_result)

if __name__ == "__main__":
    main()