
import numpy as np
import plotly.graph_objects as go

x_ = np.linspace(-2, 2, 50)
y_ = np.linspace(-2, 2, 50)

X, Y = np.meshgrid(x_, y_)

def f(x, y):
    return x**2 + np.sin(x + y)

x_vals = X.flatten()
y_vals = Y.flatten()
z_arr = f(x_vals, y_vals)

Z_original = f(X, Y)

# =====================================
# LINEAR FIT: z = a + bx + cy
# =====================================

sum_n = len(x_vals)
sum_x = np.sum(x_vals)
sum_y = np.sum(y_vals)
sum_x2 = np.sum(x_vals**2)
sum_y2 = np.sum(y_vals**2)
sum_xy = np.sum(x_vals*y_vals)

sum_z = np.sum(z_arr)
sum_xz = np.sum(x_vals*z_arr)
sum_yz = np.sum(y_vals*z_arr)

A1 = np.array([
    [sum_n, sum_x, sum_y],
    [sum_x, sum_x2, sum_xy],
    [sum_y, sum_xy, sum_y2]
])

B1 = np.array([sum_z, sum_xz, sum_yz])

a1, b1, c1 = np.linalg.solve(A1, B1)

Z_linear = a1 + b1*X + c1*Y

# =====================================
# QUADRATIC FIT
# z = a + bx + cy + dx² + exy + fy²
# =====================================

sum_x3 = np.sum(x_vals**3)
sum_y3 = np.sum(y_vals**3)
sum_x2y = np.sum(x_vals**2*y_vals)
sum_xy2 = np.sum(x_vals*y_vals**2)
sum_x4 = np.sum(x_vals**4)
sum_y4 = np.sum(y_vals**4)
sum_x3y = np.sum(x_vals**3*y_vals)
sum_x2y2 = np.sum(x_vals**2*y_vals**2)
sum_xy3 = np.sum(x_vals*y_vals**3)

sum_x2z = np.sum(x_vals**2*z_arr)
sum_xyz = np.sum(x_vals*y_vals*z_arr)
sum_y2z = np.sum(y_vals**2*z_arr)

A2 = np.array([
    [sum_n, sum_x, sum_y, sum_x2, sum_xy, sum_y2],
    [sum_x, sum_x2, sum_xy, sum_x3, sum_x2y, sum_xy2],
    [sum_y, sum_xy, sum_y2, sum_x2y, sum_xy2, sum_y3],
    [sum_x2, sum_x3, sum_x2y, sum_x4, sum_x3y, sum_x2y2],
    [sum_xy, sum_x2y, sum_xy2, sum_x3y, sum_x2y2, sum_xy3],
    [sum_y2, sum_xy2, sum_y3, sum_x2y2, sum_xy3, sum_y4]
])

B2 = np.array([
    sum_z, sum_xz, sum_yz,
    sum_x2z, sum_xyz, sum_y2z
])

a2, b2, c2, d2, e2, f2 = np.linalg.solve(A2, B2)

Z_quadratic = (
    a2 + b2*X + c2*Y
    + d2*X**2 + e2*X*Y + f2*Y**2
)

# =====================================
# CUBIC FIT
# =====================================

sum_x5 = np.sum(x_vals**5)
sum_y5 = np.sum(y_vals**5)
sum_x4y = np.sum(x_vals**4*y_vals)
sum_x3y2 = np.sum(x_vals**3*y_vals**2)
sum_x2y3 = np.sum(x_vals**2*y_vals**3)
sum_xy4 = np.sum(x_vals*y_vals**4)

sum_x6 = np.sum(x_vals**6)
sum_y6 = np.sum(y_vals**6)
sum_x5y = np.sum(x_vals**5*y_vals)
sum_x4y2 = np.sum(x_vals**4*y_vals**2)
sum_x3y3 = np.sum(x_vals**3*y_vals**3)
sum_x2y4 = np.sum(x_vals**2*y_vals**4)
sum_xy5 = np.sum(x_vals*y_vals**5)

sum_x3z = np.sum(x_vals**3*z_arr)
sum_x2yz = np.sum(x_vals**2*y_vals*z_arr)
sum_xy2z = np.sum(x_vals*y_vals**2*z_arr)
sum_y3z = np.sum(y_vals**3*z_arr)

A3 = np.array([
    [sum_n, sum_x, sum_y, sum_x2, sum_xy, sum_y2,
     sum_x3, sum_x2y, sum_xy2, sum_y3],

    [sum_x, sum_x2, sum_xy, sum_x3, sum_x2y, sum_xy2,
     sum_x4, sum_x3y, sum_x2y2, sum_xy3],

    [sum_y, sum_xy, sum_y2, sum_x2y, sum_xy2, sum_y3,
     sum_x3y, sum_x2y2, sum_xy3, sum_y4],

    [sum_x2, sum_x3, sum_x2y, sum_x4, sum_x3y, sum_x2y2,
     sum_x5, sum_x4y, sum_x3y2, sum_x2y3],

    [sum_xy, sum_x2y, sum_xy2, sum_x3y, sum_x2y2, sum_xy3,
     sum_x4y, sum_x3y2, sum_x2y3, sum_xy4],

    [sum_y2, sum_xy2, sum_y3, sum_x2y2, sum_xy3, sum_y4,
     sum_x3y2, sum_x2y3, sum_xy4, sum_y5],

    [sum_x3, sum_x4, sum_x3y, sum_x5, sum_x4y, sum_x3y2,
     sum_x6, sum_x5y, sum_x4y2, sum_x3y3],

    [sum_x2y, sum_x3y, sum_x2y2, sum_x4y, sum_x3y2, sum_x2y3,
     sum_x5y, sum_x4y2, sum_x3y3, sum_x2y4],

    [sum_xy2, sum_x2y2, sum_xy3, sum_x3y2, sum_x2y3, sum_xy4,
     sum_x4y2, sum_x3y3, sum_x2y4, sum_xy5],

    [sum_y3, sum_xy3, sum_y4, sum_x2y3, sum_xy4, sum_y5,
     sum_x3y3, sum_x2y4, sum_xy5, sum_y6]
])

B3 = np.array([
    sum_z, sum_xz, sum_yz, sum_x2z, sum_xyz,
    sum_y2z, sum_x3z, sum_x2yz, sum_xy2z, sum_y3z
])

a3, b3, c3, d3, e3, f3, g3, h3, i3, j3 = np.linalg.solve(A3, B3)

Z_cubic = (
    a3 + b3*X + c3*Y
    + d3*X**2 + e3*X*Y + f3*Y**2
    + g3*X**3 + h3*X**2*Y
    + i3*X*Y**2 + j3*Y**3
)

# =====================================
# INTERACTIVE 3D PLOT
# =====================================

surfaces = [
    ("Original", Z_original),
    ("Linear Fit", Z_linear),
    ("Quadratic Fit", Z_quadratic),
    ("Cubic Fit", Z_cubic)
]

fig = go.Figure()

for index, (name, Z) in enumerate(surfaces):
    fig.add_trace(go.Surface(
        x=X,
        y=Y,
        z=Z,
        name=name,
        colorscale="Viridis",
        showscale=False,
        visible=(index == 0),
        hovertemplate=(
            "x: %{x:.3f}<br>"
            "y: %{y:.3f}<br>"
            "z: %{z:.3f}<extra></extra>"
        )
    ))

buttons = []

for index, (name, Z) in enumerate(surfaces):
    visibility = [i == index for i in range(len(surfaces))]

    buttons.append(dict(
        label=name,
        method="update",
        args=[
            {"visible": visibility},
            {"title": name + " — 3D Surface"}
        ]
    ))

fig.update_layout(
    title="Original Function — 3D Surface",
    template="plotly_white",
    width=1000,
    height=750,
    scene=dict(
        xaxis=dict(title="X", range=[-2, 2]),
        yaxis=dict(title="Y", range=[-2, 2]),
        zaxis=dict(title="Z"),
        aspectmode="cube"
    ),
    updatemenus=[dict(
        buttons=buttons,
        direction="down",
        x=0.02,
        y=1.12,
        showactive=True
    )],
    margin=dict(l=0, r=0, t=100, b=0)
)

fig.show()

# Print fitted equations
print(
    f"Z_linear = {a1:.6f} + ({b1:.6f})*X + ({c1:.6f})*Y"
)

print(
    f"Z_quadratic = {a2:.6f} + ({b2:.6f})*X + ({c2:.6f})*Y "
    f"+ ({d2:.6f})*X**2 + ({e2:.6f})*X*Y + ({f2:.6f})*Y**2"
)

print(
    f"Z_cubic = {a3:.6f} + ({b3:.6f})*X + ({c3:.6f})*Y "
    f"+ ({d3:.6f})*X**2 + ({e3:.6f})*X*Y + ({f3:.6f})*Y**2 "
    f"+ ({g3:.6f})*X**3 + ({h3:.6f})*X**2*Y "
    f"+ ({i3:.6f})*X*Y**2 + ({j3:.6f})*Y**3"
)
