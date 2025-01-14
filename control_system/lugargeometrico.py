import control
import matplotlib.pyplot as plt

k=200
num = [1]
den = [1, 4, 0]

G1 = control.tf(num,den)
GPD = control.tf(k,[1, 15])

#Como obter as raízes do denominador
control.rlocus(G1)

#Plotar a linha de \zeta
zeta = 0.5

#fator de amortecimento
px = 20     #ponto em x no terceiro quadrante onde finaliza a reta

#Rotina para plotar a reta do fator de amortecimento
M = px/zeta
w = (M**2-px**2)**0.5
plt.plot([0, -px],[0, w],linewidth=2)
plt.show()
