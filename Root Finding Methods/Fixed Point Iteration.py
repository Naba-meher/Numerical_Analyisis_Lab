"""
Program: Fixed Point Iteration Method

Objective:
To find a root of the equation

    x^3 - 7x^2 + 14x - 6 = 0

using the Fixed Point Iteration Method.

Algorithm:
1. Rewrite the equation in the form x = g(x).
2. Take an initial guess.
3. Compute x_new = g(x_old).
4. Repeat until the error is less than the given tolerance.
5. Print the approximate root.
"""

# Function g(x)
def g(x):
    return (x**3 + 14*x - 6) / (7*x)


# User inputs
x0 = float(input("Enter initial guess: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Enter maximum iterations: "))

print("\nIteration\tApproximation")

for i in range(1, max_iter + 1):

    x1 = g(x0)

    print(i, "\t\t", x1)

    if abs(x1 - x0) < tol:
        print("\nRoot =", x1)
        print("Number of iterations =", i)
        break

    x0 = x1

else:
    print("\nMethod did not converge within the given iterations.")