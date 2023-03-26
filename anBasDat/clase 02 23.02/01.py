import random


def adivinar_numero():
    numero_secreto = random.randint(1, 15)
    intentos = 0

    while True:
        intentos += 1
        respuesta = int(input("Adivina el número entre 1 y 15: "))
        if respuesta == numero_secreto:
            print(
                f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
            break
        elif respuesta < numero_secreto:
            print("El número es mayor =>. Intenta de nuevo.")
        else:
            print("El número es menor <=. Intenta de nuevo.")


adivinar_numero()
