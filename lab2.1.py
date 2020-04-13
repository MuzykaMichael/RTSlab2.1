# Lab3(2.1)
# author: Muzyka Mikhaylo
# group: IO-72
# var: 19(1)

from algs import signal, get_F, get_F_optimized, make_table
import matplotlib.pyplot as plt

import numpy as np

import cmath


# option values
n = 12
omega = 1100
N = 64

range_min = 0
range_max = 1

x_gen = signal(n, omega, range_min, range_max)
x = [x_gen(i) for i in range(N)]
(FR, Fi) = get_F(x)
(FR1, Fi1) = get_F_optimized(x)
# print(get_F_optimized(x))

F = [FR[i] + Fi[i] for i in range(N)]

fig = plt.figure()

kef1 = fig.add_subplot(3, 2, 1)
kef2 = fig.add_subplot(3, 2, 2)
kef3 = fig.add_subplot(3, 2, 3)
kef4 = fig.add_subplot(3, 2, 4)
kef5 = fig.add_subplot(3, 2, 5)
kef6 = fig.add_subplot(3, 2, 6)


kef1.plot(range(N), FR)
kef2.plot(range(N), Fi)
kef3.plot(range(N), FR1)
kef4.plot(range(N), Fi1)
kef5.plot(range(N), x)
kef6.plot(range(N), F)

kef1.set(title='FR')
kef2.set(title='Fi')
kef3.set(title='FR_opt')
kef4.set(title='Fi_opt')
kef5.set(title='x')
kef6.set(title='F')

plt.show()

def draw(arr, x_label, y_label, title, legend, file_name=None):
    result, = plt.plot(range(len(arr)), arr, '-', label=legend)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    return result

spectr = make_table(x)
polar_spectr = np.array(list(map(lambda x: cmath.polar(x), spectr)))
ampl = draw(polar_spectr[:, 0], "p", "A(p)", "Polar Spectr", "Amplitude")
plt.legend(handles=[ampl], loc='upper right')
plt.grid()
plt.show()
phase = draw(polar_spectr[:, 1], "p", "Phi(p)", "Polar Spectr", "Phase")
plt.legend(handles=[phase], loc='upper right')
plt.grid()
plt.show()
