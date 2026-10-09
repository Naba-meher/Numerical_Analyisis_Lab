"""
Program: Incremental Search Method

Objective:
To find intervals containing roots of the equation

    f(x) = x^3 - 7x^2 + 14x - 6

using the Incremental Search Method.

Algorithm:
1. Define the function f(x).
2. Take starting point, ending point, and step size as input.
3. Move through the interval using the given step size.
4. Check the sign of f(x) at consecutive points.
5. If the sign changes, a root exists in that interval.
6. Store and display all such intervals.
"""

# Function definition
def f(x):
    return x**3 - 7*x**2 + 14*x - 6


# User inputs
start = float(input("Enter starting point: "))
end = float(input("Enter ending point: "))
step = float(input("Enter step size: "))

# List to store intervals containing roots
root_intervals = []

# Initial point
x = start

print("\nIntervals containing roots:")

while x < end:
    x_next = x + step

    # Prevent exceeding the ending point
    if x_next > end:
        x_next = end

    # Function values at consecutive points
    fx = f(x)
    fx_next = f(x_next)

    # Check for exact root
    if fx == 0:
        print(f"Root found at x = {x}")
        root_intervals.append((x, x))

    # Check for sign change
    elif fx * fx_next < 0:
        print(f"Root lies between ({x:.4f}, {x_next:.4f})")
        root_intervals.append((x, x_next))

    x = x_next

# Display all intervals
print("\nSummary of Root Intervals:")
if len(root_intervals) == 0:
    print("No root intervals found in the given range.")
else:
    for i, interval in enumerate(root_intervals, start=1):
        print(f"Root {i}: {interval}")