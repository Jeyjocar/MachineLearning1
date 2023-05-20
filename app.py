"""15-05-2023
APP para verificar valores de acciones/ventas
Jeyfrey Calero"""

import pyttsx3


motor_voz = pyttsx3.init()
motor_voz.setProperty("rate", 150)
nombre_usuario = input("Cual es tu nombre: ")

while True:
    texto = input(f'{nombre_usuario} Introduce un texto: ')
    motor_voz.say(texto)
    if texto =='n': 
        motor_voz.say("Muchas gracias, hasta pronto")
        break
    else:
        with open("Mi_Archivo", "w")as archivo:
            archivo.write(texto)

    motor_voz.runAndWait()

