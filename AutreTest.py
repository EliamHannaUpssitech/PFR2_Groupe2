import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Remplacez 'COM3' par le port approprié de votre Arduino

def digitalWrite(pin, state):
    board.digital[pin].write(state)

digitalWrite(2, 1)  # Met la broche D2 à l'état haut
time.sleep(1)
digitalWrite(2, 0)  # Met la broche D2 à l'état bas


import pyfirmata
import time

def digitalRead(pin):
    board.digital[pin].mode = pyfirmata.INPUT  # Assure que la broche est bien en mode entrée
    return board.digital[pin].read()  # Retourne l'état de la broche (0, 1 ou None si pas encore initialisé)

board = pyfirmata.Arduino('COM3')  # Connecte l’Arduino
capteurAv = board.get_pin('d:31:i')  # Broche  en input 
capteurD = board.get_pin('d:37:i')  # Broche  en input 
capteurG = board.get_pin('d:43:i')  # Broche  en input 

while presenceObjet():
    capteurAv.digitalRead(31)  # lit capteur avant
    time.sleep(1)
    capteurD.digitalRead(37)  # lit capteur droit 
    time.sleep(1)
    capteurG.digitalRead(43)  # lit capteur gauche






import pyfirmata
import time

# Connexion à l'Arduino sur le port COM3 (à adapter selon ton système)
port = 'COM3'  # Windows -> "COMx", Linux/Mac -> "/dev/ttyUSBx"
board = pyfirmata.Arduino(port)

# Mode itératif pour lire les valeurs en continu
it = pyfirmata.util.Iterator(board)
it.start()

# Définir une broche en entrée
pin = board.get_pin('d:7:i')  # d = digital, 7 = numéro de la broche, i = input

# Lire l'état de la broche 7 en boucle
while True:
    valeur = pin.read()
    if valeur is not None:
        print(f"État de la broche 7 : {valeur}")
    time.sleep(0.1)  # Petite pause pour éviter de saturer la boucle
