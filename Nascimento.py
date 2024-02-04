print("Digite o seu nome: ")
nome = input()

iniciar = True

while(iniciar == True):
    print("Digie o ano de seu nascimento")
    try:
        ano = int(input())
        if (ano < 1922) or (ano > 2022):
            print("O ano precisa ser entre 1922 e 2022. Tente um ano válido.")
        else:
            idade = 2022 - ano
            print("En 2022, o usurário ", nome, " terá ", idade, " anos.")

            iniciar = False
    except:
        print("O ano precisar estar entre 1922 e 2022")
        
