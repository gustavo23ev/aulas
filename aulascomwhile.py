import string
frase = "o gato comeu a bota"
palavra_formada = ""
indice = 0 
alfabeto = string.ascii_lowercase
digite_letra = "a"
while indice < len(frase):
    letra = frase[indice]
    palavra_formada += letra 
    flag_verificacao = None
    try:
        digite_letra_repitida = str(digite_letra)
        flag_verificacao = True
    except:
        flag_verificacao = None
        print("você não pode usar outro tipo de tipagem")
        continue
    if digite_letra_repitida not in alfabeto or len(digite_letra_repitida) > 1 or digite_letra_repitida == "" :
        print("Erro, na digitacao, tente novamente...")
        break
    indice += 1

if digite_letra_repitida:
    print(f"A letra digitada '{digite_letra_repitida}' escolhida pelo usuario, da palavra/frase {palavra_formada} se repitiu {palavra_formada.count(digite_letra_repitida)}x")


