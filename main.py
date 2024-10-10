#Variables Globales
mtext = " "
def run(text: str, target_word: str, replace_word: str) -> str:
    # TODO
    #Variables locales
    global mtext 
    posicion = text.find(target_word) #Buscamos la posicion de la palabra
    target_word = len(target_word)
    #Le sacamos la longitud con la funcion len
    mtext = text[0:posicion] + replace_word + text[posicion + target_word:]
    #Después cogemos la posicion 0 hasta la posición de la palabra, la concateno con la palabra que vamos a reemplazar, por ultimo cogemos la posicion + la longitud de la palabra y ya hasta el final de la cadena de texto
    return mtext

#Codigo principal

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(mtext)