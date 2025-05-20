import random
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("______")
    print("|    |")
    print("|     ")
    print("|      ")
    print("|      ")

    arquivo = open("./palavras.txt")
    frutas = []
    chutes = []
    for linha in arquivo:
        linha=linha.strip()
        frutas.append(linha)
    fruta_secreta = frutas[random.randint(0, (len(frutas)-1))]
    fruta_espelho = []
    print(fruta_secreta)

    for letter in fruta_secreta:
        fruta_espelho.append("_")
    acertou = False
    vidas = 6
    while(vidas>0 and acertou == False):
        chute = input("Qual seu próximo CHUTE?")
        atualizou = False
        for x in range(len(fruta_secreta)):
            if(chute == fruta_secreta[x]):
                  fruta_espelho[x] = chute
                  atualizou = True
        if(not atualizou): vidas-=1
                  
        resultado = ''.join(fruta_espelho)
        
        if(vidas==5): 
            print("______")
            print("|    |")
            print("|    O")
            print("|      ")
            print("|      ")
        elif(vidas==4): 
            print("______")
            print("|    |")
            print("|    O")
            print("|    | ")
            print("|      ")
        elif(vidas==3): 
            print("______")
            print("|    |")
            print("|    O")
            print("|    |\\")
            print("|      ")
        elif(vidas==2): 
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|      ")
        elif(vidas==1): 
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|     \\")
        elif(vidas==0): 
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|   / \\")
        print(resultado)
        if(resultado == fruta_secreta): 
            acertou = True
            print("Parabéns, você acertou!")

if(__name__ == "__main__"):
    jogar()