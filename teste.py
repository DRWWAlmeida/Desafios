

def resposta():
    res = int(input("Qual a temperatura da carne? "))
    return verify(res)

def verify(res):        
    if res < 48:
        print("A Carne ainda está crua!")
    elif res in range(48, 54):
        print("rare")
    elif res in range(54, 60):
        print("Medium Rare")
    elif res in range(60, 65):
        print("Medium")
    elif res in range(65, 72):
        print("Medium well")
    elif res > 71:
        print("Medium well")
    else:
        print("Well done!")
    resposta()
resposta()





