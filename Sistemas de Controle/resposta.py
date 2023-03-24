import control
import matplotlib.pyplot as plt

k=13.79
num=[28.37]
num2=[9.64]
num3=[16.11]
den= [1, 12, 44, 48]

tf=control.tf(num, den)
tf2=control.tf(num2, den)
tf3=control.tf(num3, den)
T, c = control.step_response(tf, 10)
T2, c2 = control.step_response(tf2, 10)
T3, c3 = control.step_response(tf3, 10)

plt.plot(T, c)
plt.plot(T2, c2)
plt.plot(T3, c3)
plt.legend(['G1', 'G2', 'G3'])
plt.grid()
plt.show()
