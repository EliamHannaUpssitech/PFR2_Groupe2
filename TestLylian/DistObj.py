import serial
import time

# Ouvre le port série
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Laisser le temps à l'Arduino de redémarrer

def mesurer_distance(direction):
    """
    direction : 'A', 'D' ou 'G' pour Avant, Droite, Gauche
    """
    ser.write(direction.encode())  # Envoi commande
    ligne = ser.readline().decode().strip()
    
    try:
        duree = int(ligne)  # durée en µs
        distance = duree * 0.034 / 2  # conversion en cm
        return round(distance, 2)
    except ValueError:
        return -1  # Erreur ou timeout

def distObj():
    if presenceObjet("image") != 0 :
        dist_av = mesurer_distance('A')
    else:
        dist_av = 0
    return dist_av