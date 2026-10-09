"""
Program: Regula Falsi Method for Finding All Roots

Objective:
Find all roots of

    f(x) = x^3 - 7x^2 + 14x - 6

by first locating intervals using Incremental Search
and then applying the Regula Falsi Method.
"""

def f(x):
    return x**3 - 7*x**2 + 14*x - 6


def regula_falsi(a, b, tol, max_iter):

    for i in range(max_iter):

        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c


# User Inputs
start = float(input("Enter starting point: "))
end = float(input("Enter ending point: "))
step = float(input("Enter step size: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Enter maximum iterations: "))

# Find intervals containing roots
intervals = []

x = start

while x < end:

    x_next = x + step

    if x_next > end:
        x_next = end

    fx = f(x)
    fx_next = f(x_next)

    if fx == 0:
        intervals.append((x, x))

    elif fx_next == 0:
        intervals.append((x_next, x_next))

    elif fx * fx_next < 0:
        intervals.append((x, x_next))

    x = x_next


print("\nIntervals containing roots:")
for interval in intervals:
    print(interval)

# Find roots using Regula Falsi Method
roots = []

for a, b in intervals:

    if a == b:
        roots.append(a)
    else:
        root = regula_falsi(a, b, tol, max_iter)
        roots.append(root)

print("\nRoots:")
for i, root in enumerate(roots, start=1):
    print(f"Root {i} = {root}")