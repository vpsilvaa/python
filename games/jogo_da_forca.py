import random
import string

aux = ['leega', 'academy', 'computador', 'remoto', 'treinamento', 'online', 'python', 'email@.', 'marron 5', '!@#$%', 'hello123', 'word!']
for _ in range(8):
    palavra = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(1, 15)))
    aux.append(palavra)

def mostrar_boneco(erros):
    if erros == 0:
        print("  _______")
        print("  |      |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|___")
    elif erros == 1:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|___")
    elif erros == 2:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print("         |")
        print("         |")
        print("_________|___")
    elif erros == 3:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print("  O      |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|___")
    elif erros == 4:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O      |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|___")
    elif erros == 5:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|___")
    elif erros == 6:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("  *      |")
        print("         |")
        print("         |")
        print("_________|___")
    elif erros == 7:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("  *      |")
        print(" /       |")
        print("         |")
        print("_________|___")
    elif erros == 8:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("  *      |")
        print(" /|      |")
        print("         |")
        print("_________|___")
    elif erros == 9:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("  *      |")
        print(" /|\\     |")
        print("         |")
        print("_________|___")
    elif erros == 10:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("  *      |")
        print(" /|\\     |")
        print("  -      |")
        print("_________|___")
    elif erros == 11:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("  *      |")
        print(" /|\\     |")
        print("  -      |")
        print(" /       |")
        print("_________|___")
    elif erros == 12:
        print("  _______")
        print("  |      |")
        print("  -      |")
        print("  -      |")
        print(" -O-     |")
        print("  *      |")
        print(" /|\\     |")
        print("  -      |")
        print(" / \\     |")
        print("_________|___")
    

jogar = True
while jogar == True:
    palavra = random.choice(aux)

    letras_corretas = []
    tentativas = 12
    palpites_dados = []

    print(f"A palavra secreta tem {len(palavra)} letras ou caracteres.")

    while tentativas > 0:
        aux2 = ''
        for letra in palavra:
            if letra in letras_corretas:
                aux2 += letra
            else:
                aux2 += '*'
        print("\nPalavra:", aux2)
        print("Palpites dados:", ', '.join(palpites_dados))

        mostrar_boneco(12 - tentativas)

        try:
            if tentativas == 1:
                palpite = input("Última tentativa! Digite a palavra completa: ").lower()
            else:
                palpite = input("Digite uma letra ou caractere: ").lower()
        except KeyboardInterrupt:
            print("\n\nPartida interrompida pelo usuário.")
            break

        if tentativas == 1 and len(palpite) > 1:
            if palpite == palavra:
                print(f"\nVocê descobriu a palavra secreta: \"{palavra}\"")
            else:
                tentativas -= 1
                print(f"\nPalavra incorreta.")
            break

        if len(palpite) != 1 and tentativas != 1:
            tentativas -= 1
            print(f"Digite apenas uma letra ou caractere válido.\nVocê tem {tentativas} tentativas restantes.")
            continue

        if palpite in letras_corretas:
            tentativas -= 1
            print(f"Você já acertou esta letra ou caractere.\nVocê tem {tentativas} tentativas restantes.")
            continue

        if palpite in palpites_dados:
            tentativas -= 1
            print(f"Você já tentou esta letra ou caractere.\nVocê tem {tentativas} tentativas restantes.")
            continue

        palpites_dados.append(palpite)

        if palpite in palavra:
            letras_corretas.append(palpite)
            tentativas -= 1
            print(f"O palpite \"{palpite}\" está na palavra.\nVocê tem {tentativas} tentativas restantes.")
        else:
            tentativas -= 1
            print(f"O \"{palpite}\" não está na palavra.\nVocê tem {tentativas} tentativas restantes.")

        if set(letras_corretas) == set(palavra):
            print(f"\nVocê descobriu a palavra secreta: \"{palavra}\"")
            break

    if tentativas == 0:
        print(f"\nA palavra secreta era: \"{palavra}\"")
        mostrar_boneco(12)

    resposta = input("Deseja jogar novamente? (s/n): ").lower()
    if resposta != 's':
        print("\nFim de jogo")
        jogar = False