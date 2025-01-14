import matplotlib.pyplot as plt

# Dados das quatro linhas
x = [125, 500, 2000, 4000]
total = [0.839814861, 0.6284862935, 0.300891611, 0.3936860389]
meio = [0.9120318642, 0.6824027324, 0.3132805258, 0.4171467309]
vazio = [0.9978374817, 0.746437984, 0.3267334529, 0.4435807691]
ideal = [1.17, 0.78, 0.741, 0.741]

# Plotando o gráfico com legendas
plt.plot(x, total, marker='.', label='T60 para 100% de ocupação')
plt.plot(x, meio, marker='.', label='T60 para 50% de ocupação')
plt.plot(x, vazio, marker='.', label='T60 sem ocupação')
plt.plot(x, ideal, marker='.', label='T60 ideal')

# Configurando eixos e legenda
plt.xlabel('Frequência(Hz)')
plt.ylabel('T60')
plt.legend(loc='best')

# Exibindo o gráfico
plt.show()