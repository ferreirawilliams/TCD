import json
def atender():
    a = input("Qual produto você deseja comprar: ")
    b = input("Quantos "+ a +" deseja comprar: ")
    c = input("Deseja continua comprando? [s] ou [n]").lower()
    
    while c == "s":
        a = input("Qual produto você deseja comprar: ")
        b = input("Quantos " + a + " deseja comprar: ")
        d = input("deseja continuar comprando? [s] ou [n]").lower()
        if d == "s":
            continue
        else:
            print("Obrigado")
            break
    return atender

atender()
    
