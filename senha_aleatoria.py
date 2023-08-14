import random as rd

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

if res1 == "Y" and res2 == "Y" and res3 == "Y" and res4 == "Y":
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

if res1 == "N" and res2 == "Y" and res3 == "Y" and res4 == "Y":
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

if res1 == "N" and res2 == "N" and res3 == "Y" and res4 == "Y":
    while(tam>0):
        senha.append(rd.choice(carac))
        aux=aux+1
        tam = tam-1
        if tam == 0: break
        senha.append(rd.choice(num))
        aux=aux+1
        tam = tam-1
        if tam == 0: break

if res1 == "N" and res2 == "N" and res3 == "N" and res4 == "Y":
    while(tam>0):
        senha.append(rd.choice(num))
        aux=aux+1
        tam = tam-1
        if tam == 0: break
    
if res1 == "Y" and res2 == "N" and res3 == "Y" and res4 == "Y":
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
    
if res1 == "Y" and res2 == "N" and res3 == "N" and res4 == "Y":
    while(tam>0):
        senha.append(rd.choice(maiu))
        tam = tam-1
        if tam == 0: break
        senha.append(rd.choice(num))
        tam = tam-1
        if tam == 0: break

if res1 == "Y" and res2 == "N" and res3 == "N" and res4 == "N":
    while(tam>0):
        senha.append(rd.choice(maiu))
        tam = tam-1
        if tam == 0: break

if res1 == "Y" and res2 == "Y" and res3 == "N" and res4 == "Y":
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

if res1 == "Y" and res2 == "Y" and res3 == "N" and res4 == "N":
    while(tam>0):
        senha.append(rd.choice(maiu))
        tam = tam-1
        if tam == 0: break
        senha.append(rd.choice(minu))
        tam = tam-1
        if tam == 0: break

if res1 == "N" and res2 == "N" and res3 == "Y" and res4 == "N":
    while(tam>0):
        senha.append(rd.choice(carac))
        tam = tam-1
        if tam == 0: break

if res1 == "N" and res2 == "Y" and res3 == "N" and res4 == "Y":
    while(tam>0):
        senha.append(rd.choice(minu))
        tam = tam-1
        if tam == 0: break
        senha.append(rd.choice(num))
        tam = tam-1
        if tam == 0: break

if res1 == "N" and res2 == "Y" and res3 == "N" and res4 == "N":
    while(tam>0):
        senha.append(rd.choice(minu))
        tam = tam-1
        if tam == 0: break

if res1 == "Y" and res2 == "N" and res3 == "Y" and res4 == "N":
    while(tam>0):
        senha.append(rd.choice(maiu))
        tam = tam-1
        if tam == 0: break
        senha.append(rd.choice(carac))
        tam = tam-1
        if tam == 0: break

if res1 == "N" and res2 == "Y" and res3 == "Y" and res4 == "N":
    while(tam>0):
        senha.append(rd.choice(minu))
        tam = tam-1
        if tam == 0: break
        senha.append(rd.choice(carac))
        tam = tam-1
        if tam == 0: break

if res1 == "Y" and res2 == "Y" and res3 == "Y" and res4 == "N":
    while(tam>0):
        senha.append(rd.choice(carac))
        tam = tam-1
        if tam == 0: break

if res1 == "N" and res2 == "N" and res3 == "N" and res4 == "N":
    print("Senha impossível de ser gerada")
elif (res1 == "Y" or res1 == "N") and (res2 == "Y" or res2 == "N") and (res3 == "Y" or res3 == "N") and (res4 == "Y" or res4 == "N"):
    for x in senha:
        print(x, end="")
else:
    print("Caracteres Y ou N digitados incorretamente")