import random

resposta = "sim"

while resposta == "sim" : 
    numero = random.randint(1, 6)

    if numero == 1 :
        print("[_____]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[_____]")

    if numero == 2 :
        print("[_____]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[_____]")

    if numero == 3 :
        print("[_____]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[_____]")

    if numero == 4 :
        print("[_____]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[_____]")
    
    if numero == 5 :
        print("[_____]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[_____]")
    
    if numero == 6 :
        print("[_____]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[_____]")

    a = input("escreva sim para jogar novamente ou nao para sair: ")
    