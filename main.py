meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "FLEXEAR" : "Presumir o alardear algo",
            "FOMO": "Miedo de perderse de algo",
            "CHAMBA": "Trabajo",
            "SUS" : "Algo que pareciera sospechoso",
            "FIFAS" : "Persona fanática al Football"
            }
print(meme_dict.keys()) 
word=input("Escribe una palabra que no entiendas: ").upper()
if word in meme_dict.keys():
    print("Significado:", meme_dict[word])
else:
    print("Aún no hemos agregado esta palabra al diccionario")
