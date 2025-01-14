import control
import matplotlib.pyplot as plt

k=13.79
num=[40]
num2=[9.64]
num3=[16.11]
den= [0.06, 5.5, 8, 40]

tf=control.tf(num, den)
tf2=control.tf(num2, den)
tf3=control.tf(num3, den)
T, c = control.step_response(tf, 10)

plt.plot(T, c)
plt.legend('G1')
plt.grid()
plt.show()
