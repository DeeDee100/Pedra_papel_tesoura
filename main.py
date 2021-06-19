"""

    random pra Pedra 0 / papel 1 / tesoura 2
    input do user
    comparar input / random
    printar resultado
    Jogar dnv ? y/n

"""


from random import randint

again = True
a = True
n = True

pc_count = 0
user_count = 0

while again:
    while a:
        user = input("Pedra papel ou tesoura ? ")
        if (user.lower()).find('pedra') != -1:
            user = 0
            a = False
        elif (user.lower()).find('papel') != -1:
            user = 1
            a = False
        elif (user.lower()).find("tesoura") != -1:
            user = 2
            a = False
        else:
            print("Argumento não válido")

    pc = randint(0,2)

    if pc == user:
        print("Empate!")

    elif pc == 0 and user == 1:
        print (f"PC: {pc} Vs User: {user}")
        print("Você ganhou!")
        user_count +=1

    elif pc == 0 and user == 2:
        print("PC: Pedra Vs User: Tesoura")
        print("Você perdeu!")
        pc_count += 1

    elif pc == 1 and user == 0:
        print("PC: Papel Vs User: Pedra")
        print("Você Perdeu")
        pc_count += 1

    elif pc == 1 and user == 2:
        print("PC: Papel Vs User: Tesoura")
        print("Você Ganhou")
        user_count += 1

    elif pc == 2 and user == 0:
        print("PC:  Tesoura Vs User: Pedra ")
        print("Você ganhou")
        user_count += 1

    elif pc == 2 and user == 1:
        print("PC: tesoura Vs User: papel")
        print("Você perdeu")
        pc_count += 1


    print ("\n ----- PLACAR ----- ")
    print(f" PC: {pc_count} X User: {user_count}")
    print (" ------------------ ")


    while n:
        res = input("Jogar dnv? y/n")
        if res.lower() == 'n':
            again = False
            n = False
        elif res.lower() == 'y':
            again = True
            a = True
            n = False
        else:
            print("Resposta não válida")


