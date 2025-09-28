
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Integration parameters
a = 0.0                          # lower bound
b = np.pi                        # upper bound
n = 1000                         # number of intervals
analytical_result = np.pi / 2    # exact value of integrating [0,π] sin²(x) dx

def sin_squared(x):
    """Function to integrate: sin²(x)"""
    return np.sin(x)**2

def riemann_sum(func, a, b, n):
    """Riemann sum using midpoint rule"""
    h = (b - a) / n
    x_points = np.linspace(a + h/2, b - h/2, n)
    y_values = func(x_points)
    return h * np.sum(y_values)

def trapezoidal_rule(func, a, b, n):
    """Trapezoidal rule integration"""
    h = (b - a) / n
    x_points = np.linspace(a, b, n + 1)
    y_values = func(x_points)
    return h * (0.5 * y_values[0] + np.sum(y_values[1:-1]) + 0.5 * y_values[-1])

def simpsons_rule(func, a, b, n):
    """Simpson's 1/3 rule integration"""
    if n % 2 != 0:
        n += 1  # Make even for Simpson's rule
    
    h = (b - a) / n
    x_points = np.linspace(a, b, n + 1)
    y_values = func(x_points)
    
    odd_sum = np.sum(y_values[1:-1:2])
    even_sum = np.sum(y_values[2:-1:2])
    
    return (h / 3) * (y_values[0] + 4 * odd_sum + 2 * even_sum + y_values[-1])

def solve_integration():
    """Calculate integrals using all methods"""
    
    # Custom methods
    riemann_result = riemann_sum(sin_squared, a, b, n)
    trapezoidal_result = trapezoidal_rule(sin_squared, a, b, n)
    simpson_result = simpsons_rule(sin_squared, a, b, n)
    
    # SciPy/NumPy methods
    x_vals = np.linspace(a, b, n + 1)
    y_vals = sin_squared(x_vals)
    
    numpy_trapz = np.trapz(y_vals, x_vals)
    scipy_quad, _ = integrate.quad(sin_squared, a, b)
    
    # Calculate errors
    riemann_error = abs(riemann_result - analytical_result)
    trapezoidal_error = abs(trapezoidal_result - analytical_result)
    simpson_error = abs(simpson_result - analytical_result)
    numpy_error = abs(numpy_trapz - analytical_result)
    quad_error = abs(scipy_quad - analytical_result)
    
    return (riemann_result, trapezoidal_result, simpson_result, numpy_trapz, scipy_quad,
            riemann_error, trapezoidal_error, simpson_error, numpy_error, quad_error)

def create_plots(riemann_result, trapezoidal_result, simpson_result):
    """Create visualization plots"""
    
    plt.figure(figsize=(15, 6))
    
    # Plot 1: Function
    plt.subplot(1, 3, 1)
    x_plot = np.linspace(a, b, 1000)
    y_plot = sin_squared(x_plot)
    plt.plot(x_plot, y_plot, 'b-', linewidth=2)
    plt.fill_between(x_plot, 0, y_plot, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('sin²(x)')
    plt.title('Function: sin²(x)')
    plt.grid(True)
    
    # Plot 2: Method comparison
    plt.subplot(1, 3, 2)
    methods = ['Riemann', 'Trapezoidal', "Simpson's"]
    results = [riemann_result, trapezoidal_result, simpson_result]
    errors = [abs(r - analytical_result) for r in results]
    
    bars = plt.bar(methods, errors, color=['red', 'blue', 'green'])
    plt.yscale('log')
    plt.ylabel('Absolute Error')
    plt.title(f'Error Comparison (n={n})')
    plt.xticks(rotation=30)
    
    for bar, error in zip(bars, errors):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                f'{error:.1e}', ha='center', va='bottom', fontsize=8)
    
    # Plot 3: Results table
    plt.subplot(1, 3, 3)
    plt.axis('off')
    
    table_data = [
        ['Method', 'Result', 'Error'],
        ['Riemann', f'{riemann_result:.6f}', f'{abs(riemann_result - analytical_result):.2e}'],
        ['Trapezoidal', f'{trapezoidal_result:.6f}', f'{abs(trapezoidal_result - analytical_result):.2e}'],
        ["Simpson's", f'{simpson_result:.6f}', f'{abs(simpson_result - analytical_result):.2e}'],
        ['Analytical', f'{analytical_result:.6f}', '0.00e+00']
    ]
    
    table = plt.table(cellText=table_data[1:], colLabels=table_data[0],
                     cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.5)
    
    plt.suptitle(f'Numerical Integration: sin²(x) from 0 to π (Analytical = π/2 = {analytical_result:.6f})', 
                 fontsize=14, y=0.98)
    plt.subplots_adjust(top=0.85, bottom=0.1, left=0.08, right=0.95, wspace=0.3)
    plt.show()

def print_results(riemann_result, trapezoidal_result, simpson_result, numpy_trapz, scipy_quad,
                 riemann_error, trapezoidal_error, simpson_error, numpy_error, quad_error):
    """Print numerical results summary"""
    
    print(f"Final integration results:")
    print(f"  Riemann sum: {riemann_result:.6f}")
    print(f"  Trapezoidal rule: {trapezoidal_result:.6f}")
    print(f"  Simpson's rule: {simpson_result:.6f}")
    print(f"  NumPy trapz: {numpy_trapz:.6f}")
    print(f"  SciPy quad: {scipy_quad:.6f}")
    print(f"  Analytical: {analytical_result:.10f}")

    print(f"\nError analysis:")
    print(f"  Riemann - Error: {riemann_error:.2e}")
    print(f"  Trapezoidal - Error: {trapezoidal_error:.2e}")
    print(f"  Simpson's - Error: {simpson_error:.2e}")
    print(f"  NumPy trapz - Error: {numpy_error:.2e}")
    print(f"  SciPy quad - Error: {quad_error:.2e}")

    best_method = min([
        ("Riemann", riemann_error),
        ("Trapezoidal", trapezoidal_error),
        ("Simpson's", simpson_error),
        ("NumPy trapz", numpy_error),
        ("SciPy quad", quad_error)
    ], key=lambda x: x[1])

    print(f"\nMost accurate method: {best_method[0]} with error {best_method[1]:.2e}")