
def convertToList(texto):
    for caracter in ".,;:¡!¿?()[]{}\"'":
        texto = texto.replace(caracter, "")
    return texto.split()

def standardWord(string):
    string = string.lower()
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for caracter in string:
        if caracter in reemplazos:
            string = string.replace(caracter, reemplazos[caracter])
    return string

def procesar_texto(string):
    # {numero total de palabras, lista de palabras unicas, la palabra mas larga, numero de veces que aparece cada palabra}
    lista = convertToList(string)
    diccionario ={"Total de palabras" : 0, "Lista palabras unicas" : [], "Palabra" : "", "contador de palabras" : {} }

    if len(lista) >0:
        diccionario["Palabra"] = lista[0]
        diccionario["Total de palabras"] = len(lista)

        for i in lista:
            palabra = standardWord(i)
            if diccionario["contador de palabras"].get(palabra) != None:
                diccionario["contador de palabras"][palabra]+=1
            else:
                diccionario["contador de palabras"][palabra] = 1 
            if i not in diccionario["Lista palabras unicas"]:
                diccionario["Lista palabras unicas"].append(i)
            if len(diccionario["Palabra"]) < len(i):
                diccionario["Palabra"] = i 
    return diccionario

def test():
    diccionario = procesar_texto("Somos una plataforma filantrópica de impacto social que apoya acciones y proyectos para generar oportunidades de calidad en educación.")
    palabras = diccionario["Total de palabras"]
    listaPalabras = diccionario["Lista palabras unicas"]
    palabraLarga = diccionario["Palabra"]
    contador = diccionario["contador de palabras"]
    assert palabras == 19
    assert listaPalabras == ['Somos', 'una', 'plataforma', 'filantrópica', 'de', 'impacto', 'social', 'que', 'apoya', 'acciones', 'y', 'proyectos', 'para', 'generar', 'oportunidades', 'calidad', 'en', 'educación']
    assert palabraLarga == "oportunidades"
    assert contador=={'somos': 1, 'una': 1, 'plataforma': 1, 'filantropica': 1, 'de': 2, 'impacto': 1, 'social': 1, 'que': 1, 'apoya': 1, 'acciones': 1, 'y': 1, 'proyectos': 1, 'para': 1, 'generar': 1, 'oportunidades': 1, 'calidad': 1, 'en': 1, 'educacion': 1}
test()


##mas pruebas
print()
print(procesar_texto("Estamos convencidos de que la mejor forma de contribuir a nuestro país es catalizando procesos de movilidad social a través de la educación."))
print()
print(procesar_texto("Transmiten emociones y sentimientos. En sus orígenes, tenían un carácter ritual y comunitario. Los primeros textos poéticos fueron creados para ser cantados Estan escritos en versos."))
