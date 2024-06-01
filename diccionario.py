while True:
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "ROFL": "Una respuesta a una broma",
                "SHEESH": "Ligera desaprobación",
                "CREEPY": "aterrador, siniestro",
                "AGGRO" : "ponerse agresivo/enojado",
                }

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print("El significado de la palabra es:" , meme_dict[word])
    else:
        print("La palabra no se encuentra en el diccionario")
    
    
