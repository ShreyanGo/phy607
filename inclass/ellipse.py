import numpy as np
import matplotlib.pyplot as plt
# Part 1: Sampling methods
def exp_pdf(x, lam=2):
    Z = (1 - np.exp(-lam)) / lam
    return np.exp(-lam * x) / Z
def inverse_cdf(n):
    u = np.random.rand(n)
    lam = 2
    return -np.log(1 - u * (1 - np.exp(-lam))) / lam
def rejection(n):
    samples = []
    lam = 2
    M = exp_pdf(0, lam)
    
    while len(samples) < n:
        x = np.random.rand()
        u = np.random.rand() * M
        if u <= exp_pdf(x, lam):
            samples.append(x)
    return np.array(samples)
# test part 1
n = 5000
s1 = inverse_cdf(n)
s2 = rejection(n)
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.hist(s1, bins=40, density=True, alpha=0.7)
x = np.linspace(0, 1, 100)
plt.plot(x, exp_pdf(x), 'r-', lw=2)
plt.title('Inverse CDF')
plt.subplot(122)
plt.hist(s2, bins=40, density=True, alpha=0.7)
plt.plot(x, exp_pdf(x), 'r-', lw=2)
plt.title('Rejection Sampling')
plt.tight_layout()
plt.show()
print(f"Inverse CDF: mean={s1.mean():.3f}, std={s1.std():.3f}")
print(f"Rejection: mean={s2.mean():.3f}, std={s2.std():.3f}")
# Part 2: Ellipse integration
a, b = 5, 2
true_area = np.pi * a * b
def area_estimate(n):
    x = np.random.uniform(-a, a, n)
    y = np.random.uniform(-b, b, n)
    inside = (x**2/a**2 + y**2/b**2) <= 1
    return 4*a*b * inside.sum() / n
def circumference_estimate(n):
    theta = np.random.uniform(0, 2*np.pi, n)
    dl = np.sqrt((a*np.sin(theta))**2 + (b*np.cos(theta))**2)
    return 2*np.pi * dl.mean()
# check area
area = area_estimate(10000)
print(f"\nArea estimate: {area:.4f}, True: {true_area:.4f}")
# uncertainty scaling
N = np.logspace(2, 4.5, 8).astype(int)
trials = 30
uncertainties = []
for n in N:
    estimates = [area_estimate(n) for _ in range(trials)]
    uncertainties.append(np.std(estimates))
    print(f"N={n:5d}, uncertainty={uncertainties[-1]:.4f}")
# plot scaling
plt.figure(figsize=(8, 5))
plt.loglog(N, uncertainties, 'bo-', label='Data')
plt.loglog(N, uncertainties[0]*np.sqrt(N[0]/N), 'r--', label='N^(-1/2)')
plt.xlabel('N samples')
plt.ylabel('Uncertainty')
plt.title('Area Uncertainty Scaling')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
# circumference
circ_vals = [circumference_estimate(10000) for _ in range(20)]
print(f"\nCircumference: {np.mean(circ_vals):.4f} ± {np.std(circ_vals):.4f}")
# show sampling
n_vis = 1000
x = np.random.uniform(-a, a, n_vis)
y = np.random.uniform(-b, b, n_vis)
inside = (x**2/a**2 + y**2/b**2) <= 1
plt.figure(figsize=(6, 5))
plt.scatter(x[inside], y[inside], c='b', s=3, alpha=0.5)
plt.scatter(x[~inside], y[~inside], c='r', s=3, alpha=0.3)
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(a*np.cos(theta), b*np.sin(theta), 'k-', lw=2)
plt.axis('equal')
plt.title('Sampling for Area')
plt.show()