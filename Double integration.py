#Douuble integration
from sympy import symbols, sympify, lambdify
# --------------------------------------------------
# Numerical Integration Rules
# --------------------------------------------------
def integrate_1d(function, lower_limit, upper_limit, n, method):
    h = (upper_limit - lower_limit) / n
    total = 0
    for i in range(n + 1):
        x = lower_limit + i * h
        value = function(x)
        if method == 1:  # Trapezoidal Rule
            if i == 0 or i == n:
                weight = 1
            else:
                weight = 2
        elif method == 2:  # Simpson's 1/3 Rule
            if i == 0 or i == n:
                weight = 1
            elif i % 2 == 1:
                weight = 4
            else:
                weight = 2
        elif method == 3:  # Simpson's 3/8 Rule
            if i == 0 or i == n:
                weight = 1
            elif i % 3 == 0:
                weight = 2
            else:
                weight = 3
        total += weight * value
    if method == 1:
        return (h / 2) * total
    elif method == 2:
        return (h / 3) * total
    elif method == 3:
        return (3 * h / 8) * total

# --------------------------------------------------
# Double Integration
# --------------------------------------------------
def double_integration(f, a, b, c, d, nx, ny, method):
    # Integrate with respect to y first
    def integrate_over_y(x):
        return integrate_1d(
            lambda y: f(x, y), c, d, ny, method
        )
    # Then integrate with respect to x
    result = integrate_1d(
        integrate_over_y, a, b, nx, method
    )

    return result


# --------------------------------------------------
# Main Program
# --------------------------------------------------

def main():
    x, y = symbols("x y")

    expression = input("Enter function f(x,y): ")
    f = lambdify((x, y), sympify(expression), "math")

    print("\nEnter limits for integration:")
    a = float(input("Lower limit of x: "))
    b = float(input("Upper limit of x: "))
    c = float(input("Lower limit of y: "))
    d = float(input("Upper limit of y: "))

    print("\nChoose integration methods:")
    print("1. Trapezoidal Rule")
    print("2. Simpson's 1/3 Rule")
    print("3. Simpson's 3/8 Rule")
    print("Enter multiple choices separated by commas.")
    print("Example: 1,2,3")

    choices = input("Your choice: ")
    methods = list(dict.fromkeys(
        int(choice.strip()) for choice in choices.split(",")
    ))

    if not methods or any(m not in (1, 2, 3) for m in methods):
        print("Invalid method selection.")
        return

    for method in methods:
        print(f"\nMethod: {method}")

        nx = int(input("Number of subintervals along x: "))
        ny = int(input("Number of subintervals along y: "))

        if nx <= 0 or ny <= 0:
            print("Subinterval counts must be positive.")
            continue

        if method == 2 and (nx % 2 != 0 or ny % 2 != 0):
            print("Simpson's 1/3 Rule requires both counts to be even.")
            continue

        if method == 3 and (nx % 3 != 0 or ny % 3 != 0):
            print("Simpson's 3/8 Rule requires both counts "
                  "to be multiples of 3.")
            continue

        result = double_integration(
            f, a, b, c, d, nx, ny, method
        )

        names = {
            1: "Trapezoidal Rule",
            2: "Simpson's 1/3 Rule",
            3: "Simpson's 3/8 Rule"
        }

        print(f"{names[method]} result = {result}")


if __name__ == "__main__":
    main()
