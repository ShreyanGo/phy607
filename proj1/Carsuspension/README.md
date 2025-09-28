# Car Suspension ODE Solver

## Installation
Install required packages:
```bash
pip install numpy scipy matplotlib
```

## Files
- `main.py` - Main script to run the analysis
- `suspension_solver.py` - ODE solver functions and plotting

## Usage
```bash
python main.py
```

## Output
- 4 plots showing displacement, velocity, acceleration vs time, plus error analysis
- Console output with final displacement values and error statistics

## Description
The program solves the 3rd order car suspension ODE:
```
m * d³y/dt³ + c₂ * d²y/dt² + c₁ * dy/dt + c₀ * y = 0
```

Using hand-implemented Euler and 4th order Runge-Kutta methods, compared against SciPy.