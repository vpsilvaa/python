import random as rd
import time

def gerar_senha():
    num = (0,1,2,3,4,5,6,7,8,9)
    carac = ("/","*","-","+",".",",","!","@"
            ,"#","$","%","&","(",")","\\")
    minu = ("a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z")
    maiu = ("A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

    senha = []
    aux = 0

    try:
        tam = input("Digite o tamanho da senha:\n")
        tam = int(tam)
    except ValueError as ve:
        print("Valor digitado eh invalido")
        print(f"Erro: {ve}")
        exit()
        
    res1 = input("Deseja a senha com letras maiuscula? (Y/N)\n")
    res2 = input("Deseja a senha com letras minuscula? (Y/N)\n")
    res3 = input("Deseja a senha com caracteres especiais? (Y/N)\n")
    res4 = input("Deseja a senha com numeros? (Y/N)\n")

    if res1.upper() == "Y" and res2.upper() == "Y" and res3.upper() == "Y" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(maiu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(minu))
            aux=aux+1
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(carac))
            aux=aux+1
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(num))
            aux=aux+1
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "Y" and res3.upper() == "Y" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(minu))
            aux=aux+1
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(carac))
            aux=aux+1
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(num))
            aux=aux+1
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "N" and res3.upper() == "Y" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(carac))
            aux=aux+1
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(num))
            aux=aux+1
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "N" and res3.upper() == "N" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(num))
            aux=aux+1
            tam = tam-1
            if tam == 0: break
        
    if res1.upper() == "Y" and res2.upper() == "N" and res3.upper() == "Y" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(maiu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(carac))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(num))
            tam = tam-1
            if tam == 0: break
        
    if res1.upper() == "Y" and res2.upper() == "N" and res3.upper() == "N" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(maiu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(num))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "Y" and res2.upper() == "N" and res3.upper() == "N" and res4.upper() == "N":
        while(tam>0):
            senha.append(rd.choice(maiu))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "Y" and res2.upper() == "Y" and res3.upper() == "N" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(maiu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(minu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(num))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "Y" and res2.upper() == "Y" and res3.upper() == "N" and res4.upper() == "N":
        while(tam>0):
            senha.append(rd.choice(maiu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(minu))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "N" and res3.upper() == "Y" and res4.upper() == "N":
        while(tam>0):
            senha.append(rd.choice(carac))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "Y" and res3.upper() == "N" and res4.upper() == "Y":
        while(tam>0):
            senha.append(rd.choice(minu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(num))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "Y" and res3.upper() == "N" and res4.upper() == "N":
        while(tam>0):
            senha.append(rd.choice(minu))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "Y" and res2.upper() == "N" and res3.upper() == "Y" and res4.upper() == "N":
        while(tam>0):
            senha.append(rd.choice(maiu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(carac))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "Y" and res3.upper() == "Y" and res4.upper() == "N":
        while(tam>0):
            senha.append(rd.choice(minu))
            tam = tam-1
            if tam == 0: break
            senha.append(rd.choice(carac))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "Y" and res2.upper() == "Y" and res3.upper() == "Y" and res4.upper() == "N":
        while(tam>0):
            senha.append(rd.choice(carac))
            tam = tam-1
            if tam == 0: break

    if res1.upper() == "N" and res2.upper() == "N" and res3.upper() == "N" and res4.upper() == "N":
        print("Senha impossível de ser gerada")
    elif (res1.upper() == "Y" or res1.upper() == "N") and (res2.upper() == "Y" or res2.upper() == "N") and (res3.upper() == "Y" or res3.upper() == "N") and (res4.upper() == "Y" or res4.upper() == "N"):
        print("\nSenha:  ")
        for x in senha:
            print(x, end="")
        print("")
        print("")
    else:
        print("Caracteres Y ou N digitados incorretamente")



while True:
    gerar_senha()
    novamente = input("Deseja gerar outra senha? (Y/N)\n")
    if novamente.upper() != "Y":
        break