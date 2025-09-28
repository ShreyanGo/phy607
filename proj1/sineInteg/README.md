# Numerical Integration Solver

## Installation
Install required packages:
```bash
pip install numpy scipy matplotlib
```

## Files
`main_integ.py` - Main script to run the integration analysis
`sininteg.py` - Integration methods and plotting functions

## Usage
```bash
python main_integration.py
```

## Output
3 plots showing function visualization, error comparison, and results table
Console output with final integration values and error statistics

## Description
The program numerically integrates sin²(x) from 0 to π using:

**Hand-implemented methods:**
Riemann sum (midpoint rule)
Trapezoidal rule
Simpson's 1/3 rule

**Library methods for comparison:**
NumPy `trapz`
SciPy `quad`

The analytical result is π/2 ≈ 1.5707963268 for comparison and error analysis.