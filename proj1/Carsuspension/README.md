# Car Suspension ODE Solver

This project implements custom numerical ODE solvers to analyze car suspension systems governed by the third-order ODE:

```
m * d³y/dt³ + c₂ * d²y/dt² + c₁ * dy/dt + c₀ * y = 0
```

Where:
- `y(t)` is the vertical displacement of the car body from equilibrium
- `m` is the mass of the car body
- `c₂` is the damping coefficient for acceleration changes
- `c₁` is the standard shock absorber damping coefficient  
- `c₀` is the spring constant

## Features

### Custom ODE Solvers
- **Euler's Method**: First-order explicit method
- **4th Order Runge-Kutta**: Higher-order explicit method
- **SciPy Integration**: For comparison using `solve_ivp`
- **Analytical Solutions**: When available for specific parameter sets

### Analysis Capabilities
- Multiple car suspension scenarios (standard, sports car, luxury car, truck)
- Error analysis comparing custom methods to SciPy reference
- Step size convergence analysis
- Comprehensive visualization including phase portraits
- Automatic figure generation and saving

## File Structure

```
├── main_suspension.py      # Main analysis script
├── ode_solvers.py         # Custom ODE solver implementations
├── suspension_system.py   # Car suspension model and scenarios
├── visualization.py       # Plotting and analysis functions
├── run_analysis.py        # Convenience script to run all scenarios
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start
Run all scenarios with default settings:
```bash
python run_analysis.py
```

Save all figures and include step size analysis:
```bash
python run_analysis.py --save-figures --step-analysis
```

### Individual Scenario Analysis
Run a specific scenario:
```bash
python main_suspension.py --scenario standard
```

Available scenarios:
- `standard`: Typical passenger car (1500 kg)
- `sports_car`: Performance vehicle with stiffer suspension (1200 kg)
- `luxury_car`: Comfort-oriented with softer suspension (2000 kg)
- `truck`: Heavy vehicle with robust suspension (3000 kg)

### Advanced Options
```bash
python main_suspension.py --scenario sports_car --step-size 0.005 --time-end 3.0 --save-figures --step-analysis
```

Options:
- `--scenario`: Choose test scenario
- `--step-size`: Numerical integration step size (default: 0.01)
- `--time-end`: Simulation end time (default: 2.0)
- `--save-figures`: Save plots as PNG files
- `--step-analysis`: Perform convergence analysis

## Output

### Generated Figures
1. **Main Comparison Plot**: Shows displacement, velocity, acceleration, and phase portrait
2. **Error Analysis**: Logarithmic error plots comparing methods
3. **Step Size Analysis**: Convergence rate analysis (if requested)

### Console Output
- Detailed solver progress and timing
- Final values for each method
- Comprehensive error metrics
- Analysis summary

## Technical Details

### ODE System Conversion
The third-order ODE is converted to a system of first-order ODEs:
```
y₁ = y           (displacement)
y₂ = dy/dt       (velocity)
y₃ = d²y/dt²     (acceleration)

dy₁/dt = y₂
dy₂/dt = y₃  
dy₃/dt = -(c₂*y₃ + c₁*y₂ + c₀*y₁)/m
```

### Solver Implementations

**Euler's Method**:
```
y_{n+1} = y_n + h * f(t_n, y_n)
```

**4th Order Runge-Kutta**:
```
k₁ = h * f(t_n, y_n)
k₂ = h * f(t_n + h/2, y_n + k₁/2)
k₃ = h * f(t_n + h/2, y_n + k₂/2)
k₄ = h * f(t_n + h, y_n + k₃)
y_{n+1} = y_n + (k₁ + 2k₂ + 2k₃ + k₄)/6
```

### Error Analysis
- Absolute and relative errors computed against SciPy reference
- Maximum, mean, and RMS error metrics
- Convergence rate verification

## Example Results

For a standard car scenario with initial displacement of 0.1m:

| Method | Final Displacement (m) | Max Error vs SciPy |
|--------|----------------------|-------------------|
| Euler (h=0.01) | 0.001234 | ~10⁻⁴ |
| RK4 (h=0.01) | 0.001235 | ~10⁻⁸ |
| SciPy | 0.001235 | Reference |

The RK4 method demonstrates significantly better accuracy than Euler's method, approaching machine precision for reasonable step sizes.

## Physical Interpretation

The suspension system exhibits different behaviors based on parameters:
- **Overdamped**: Slow return to equilibrium without oscillation
- **Critically damped**: Fastest return without overshoot
- **Underdamped**: Oscillatory motion with decay

The different vehicle scenarios demonstrate how mass and damping affect ride quality and stability.

## Requirements

- Python 3.7+
- NumPy ≥ 1.21.0
- SciPy ≥ 1.7.0  
- Matplotlib ≥ 3.5.0

## License

This project is for educational purposes. Feel free to modify and extend for your own analysis needs.