from math import log, tan, pi
from scipy.integrate import quad


# function we want to integrate
def f(x):
    return log(1+tan(x))

res, err = quad(f, 0, pi/4)

print("The numerical result is {:f} (+-{:g})"
    .format(res, err))
