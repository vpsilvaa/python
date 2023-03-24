import control
import matplotlib.pyplot as plt

num = [1]
den = [1, 12, 32]

G1 = control.tf(num,den)
GPD = control.tf([1, 3],[1])

#Como obter as raízes do denominador
control.rlocus(G1*GPD)

#Plotar a linha de \zeta
zeta = 0.707

#fator de amortecimento
px = 20     #ponto em x no terceiro quadrante onde finaliza a reta

#Rotina para plotar a reta do fator de amortecimento
M = px/zeta
w = (M**2-px**2)**0.5
plt.plot([0, -px],[0, w],linewidth=2)
plt.show()
