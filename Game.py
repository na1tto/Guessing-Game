palavra_secreta = "caverna"
chute = ""
contador = 0
limite = 3
sem_tentativas = False

while chute != palavra_secreta and not(sem_tentativas):
    if contador < limite:
       chute = input("Tente advinhar a palavra secreta, você possui 3 tentativas: ")
       contador += 1
    else:
        sem_tentativas = True
if sem_tentativas:
    print("Você perdeu.")
else:
    print("Parabéns! Você acertou :)")
