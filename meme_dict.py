meme_dict = {
    "LOL" - "una respuesta a algo gracioso"
    "CRINGE" - "algo raro o embarazoso"
    "ROFL" - "una respuesta a una broma"
    "SHEESH" - "ligera desaprobación"
    "CREEPY" - "aterrador, siniestro"
    "AGGRO" - "ponerse agresivo/enojado"
}
while True:
    word = input("Escribe una palabra moderna que no entiendas (Usa mayusculas)")
    if word in meme_dict:
        print(meme_dict[word])
    
    else:
        print(" aun no tenemos esa palabra")

    if word == "fin":
        break
