from planet import Solar_body

#List of bodies that will be used in main

black_hole = Solar_body(
    2.000e30 * 50,
    (0, 0),
    (0, 0),
    (50),
    "grey"
)

sun = Solar_body(
    1.9885e30,
    (0, 0),
    (0, 0),
    20,
    "orange"
)

sun2 = Solar_body(
    1.9885e30,
    (0, 0),
    (0, 0),
    20,
    "orange"
)

mercury = Solar_body(
    3.285e23,
    (0, 47870),
    (5.79e10, 0),
    4,
    "gray"
)

venus = Solar_body(
    4.867e24,
    (0, 35.02e3),
    (1.082e11, 0),
    4,
    "yellow"
)

earth = Solar_body(
    5.927e24,
    (0, 3.078e4),
    (1.496e11, 0),
    5,
    "blue"
)

mars = Solar_body(
    6.417e23,
    (0, 2.4077e4),
    (2.279e11, 0),
    6,
    "red"
)

jupiter = Solar_body(
    1.898e27,
    (0, 1.307e4),
    (7.785e11, 0),
    12,
    "orange"
)

saturn = Solar_body(
    5.683e26,
    (0, 9.69e3),
    (1.433e12, 0),
    10,
    "gold"
)

uranus = Solar_body(
    8.681e25,
    (0, 6.81e3),
    (2.877e12, 0),
    9,
    "lightblue"
)

neptune = Solar_body(
    1.024e26,
    (0, 5.43e3),
    (4.503e12, 0),
    9,
    "darkblue"
)

# 3 body problem
body1 = Solar_body(
    5.97e24,
    (0.466203685e4, 0.43236573e4),
    (-0.97000436e11,  0.24308753e11),
    8,
    "red"
)

body2 = Solar_body(
    5.97e24,
    (0.466203685e4, 0.43236573e4),
    ( 0.97000436e11, -0.24308753e11),
    8,
    "green"
)

body3 = Solar_body(
    5.97e24,
    (-0.93240737e4, -0.86473146e4),
    (0, 0),
    8,
    "blue"
)