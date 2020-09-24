import random
import os
words = 'sesamo apio perejil aceite arandano gelatina jengibre higo zapallo nispero ciruelo huevo pan yogurt perro almendra mango durazno granada pera repollo espinaca yuca guayaba melon ajo limon fresa mora brocoli lechuga palta cafe avena cocoa sal azucar vainilla mantequilla carne queso leche chocolate fideo arroz rabano chirimoya mandarina pomelo naranja platano coco sandia cebolla tomate pimenton zanahoria kiwi papaya uva manzana locoto papa frutilla'.split()
letrasIncorrectas = ''
letrasCorrectas = ''
indice = random.randint(0, len(words) - 1)
palabraSecreta = words[indice]
juegoTerminado = False
def mensajesIntentos():
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasCorrectas or intento in letrasIncorrectas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            break
    return intento

def mostrarLetras(palabras):
    for letra in palabras:
        print(letra, end=' ')
    print()
def sinIntentos():
    global letrasIncorrectas 
    letrasIncorrectas = letrasIncorrectas + intento
    if len(letrasIncorrectas) == 6:
        print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) +
              ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
        global juegoTerminado
        juegoTerminado= True

def reiniciar():
    global letrasIncorrectas
    letrasIncorrectas = ''
    global letrasCorrectas
    letrasCorrectas = ''
    global indice
    indice = random.randint(0, len(words) - 1)
    global palabraSecreta
    palabraSecreta = words[indice]
    global juegoTerminado
    juegoTerminado= False


while True:
    print('ADIVINA LA PALABRA')
    print("#####################################################################################################")
    print('Letras incorrectas:', end=' ')
    mostrarLetras(letrasIncorrectas)

    espacios = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:

            espacios = espacios[:i] + \
                palabraSecreta[i] + espacios[i+1:]

    mostrarLetras(espacios)

    intento = mensajesIntentos()

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        todas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                todas = False
                return True
            else:
                return False
       
        if todas:
            print('¡Sí! ¡La palabra secreta es "' +
                  palabraSecreta + '"! ¡Has ganado!')
            juegoTerminado = True
    else:
       sinIntentos()

    if juegoTerminado:
        print('¿Quieres jugar de nuevo? (sí o no)')
        if input().lower().startswith('s'):
          reiniciar()
          os.system("cls")
        else:
            break
