import control
import matplotlib.pyplot as plt
import sys

K = 50
num=[1*K] #s+0.1
den=[1, 9, 18, 0] #s^3 + 9s^2 + 20s + 12

G = control.tf(num, den)

control.bode(G, initial_phase=0, dB=True, Hz=False, margins=True)

plt.show()

