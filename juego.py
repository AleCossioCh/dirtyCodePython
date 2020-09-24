import random

words = 'sesamo apio perejil aceite arandano gelatina jengibre higo zapallo nispero ciruelo huevo pan yogurt perro almendra mango durazno granada pera repollo espinaca yuca guayaba melon ajo limon fresa mora brocoli lechuga palta cafe avena cocoa sal azucar vainilla mantequilla carne queso leche chocolate fideo arroz rabano chirimoya mandarina pomelo naranja platano coco sandia cebolla tomate pimenton zanahoria kiwi papaya uva manzana locoto papa frutilla'.split()
print('ADIVINA LA PALABRA')
incorrectas = ''
correctas = ''
indice = random.randint(0, len(words) - 1)
palabra = words[indice]
terminado = False

while True:
    print("#####################################################################################################")
    print('Letras incorrectas:', end=' ')
    for letra in incorrectas:
        print(letra, end=' ')
    print()

    espacios = '_' * len(palabra)
    for i in range(len(palabra)):
if palabra[i] in correctas:

    espacios = espacios[:i] + \
        palabra[i] + espacios[i+1:]

    for letra in espacios:
        print(letra, end=' ')
    print()

    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
                if len(intento) != 1:
                    print('Por favor, introduce una letra.')
        elif intento in correctas or intento in incorrectas:
            print('Ya has probado esa letra. Elige otra.')
                elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
                    print('Por favor ingresa una LETRA.')
        else:
            break

    if intento in palabra:
        correctas = correctas + intento
        todas = True
        for i in range(len(palabra)):
            if palabra[i] not in correctas:
                todas = False
                break

        if todas:
            print('¡Sí! ¡La palabra secreta es "' +
                  palabra + '"! ¡Has ganado!')
            terminado = True
    else:
        incorrectas = incorrectas + intento
        if len(incorrectas) == 6:
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(incorrectas)) +
                  ' intentos fallidos y ' + str(len(correctas)) + ' aciertos, la palabra era "' + palabra + '"')
            terminado = True

    if terminado:
        print('¿Quieres jugar de nuevo? (sí o no)')
if input().lower().startswith('s'):
    incorrectas = ''
    correctas = ''
    terminado = False
    indice = random.randint(0, len(words) - 1)
    palabra = words[indice]
else:
    break
