import random
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    frutas = ["pera", "banana", "melancia", "laranja", "abacaxi"]
    fruta_secreta = frutas[random.randint(0, 3)]
    fruta_espelho = []

    for letter in fruta_secreta:
        fruta_espelho.append("_")
        
    enforcou = False
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
        print("______")
        print("|    |")
        print("|     ")
        print("|      ")
        print("|      ")
        if(vidas<=5): 
            print("______")
            print("|    |")
            print("|    O")
            print("|      ")
            print("|      ")

        if(vidas<=4): 
            print("______")
            print("|    |")
            print("|    O")
            print("|    | ")
            print("|      ")
        if(vidas<=3): 
            print("______")
            print("|    |")
            print("|    O")
            print("|    |\\")
            print("|      ")
        if(vidas<=2): 
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|      ")
        if(vidas<=1): 
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|     \\")
        if(vidas<=0): 
            print("______")
            print("|    |")
            print("|    O")
            print("|   /|\\")
            print("|   / \\")
        print(resultado)  # Saída: _a_a_a 
        if(resultado == fruta_secreta): 
            acertou = True
            print("Parabéns, você acertou!")

if(__name__ == "__main__"):
    jogar()