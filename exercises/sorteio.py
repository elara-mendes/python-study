import random

item = str(input("Digite o item a ser sorteado:"))
participantes = []
participante = ""

if item != "":
    while participante != "parar":
        participante = str(input("Escreva o nome dos participante, quando terminar digite 'parar':")).lower()
        if participante != "parar" and participante != "":
            participantes.append(participante)
    random.shuffle(participantes)
    if len(participantes) > 0:
        print(f"{participantes[0].capitalize()} é o vencedor(a)! e ganhou {item}!")
    else:
        print("Nenhum participante adicionado.")
