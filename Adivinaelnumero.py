import random

numero_random = random.randint(1,100)
contador = 0
print("\tAdivina el numero:")
print("Debes agregar un numero del 1 al 100")
while True:
    while True:
        try:
            Numero = int(input('Pon un numero: '))
        except ValueError as E:
            print("Debes agregar un numero, no una letra")
            print(f"La excepcion es: {E}")
        else:
            break
    contador += 1
    if Numero>numero_random:
        print('El numero es menor')
    elif Numero<numero_random:
        print('El numero es mayor')
    else:
        print(f'¡Fecilitaciones el numero es: {numero_random}!')
        break
print(f'Numero de intentos: {contador}')