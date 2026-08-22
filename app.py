import numpy as np

def F(X):
    x, y, z = X
    return np.array([
        x**2 + y**2 + z**2 - 14,
        4*x - 3*y**2 + 2*z**3 - 46,
        3*y**3 - 2*z - 18
    ], dtype=float)

def J(X):
    x, y, z = X
    return np.array([
        [2*x,   2*y,    2*z],
        [4,    -6*y,   6*z**2],
        [0,     9*y**2, -2]
    ], dtype=float)

# Tebakan awal
X = np.array([1.0, 1.0, 1.0])

print("RAFIF")

tol = 1e-6
max_iter = 100

print("Iterasi |        x        y        z      |   error")
print("-"*60)

for k in range(max_iter):
    delta = np.linalg.solve(J(X), -F(X))
    X_new = X + delta
    
    error = np.linalg.norm(delta, np.inf)   # norma tak hingga
    
    print(f"{k+1:6d} | {X_new[0]:8.6f} {X_new[1]:8.6f} {X_new[2]:8.6f} | {error:.6e}")
    
    if error < tol:
        X = X_new
        break
    
    X = X_new

print("\nHasil akhir:")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])
print("Jumlah iterasi =", k+1)
print("F(X) =", F(X))
print("Hello")



