import serial
import time

# Connexion au port série (ajuste COM4 si nécessaire)
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Attendre la connexion

def pulseIn(pin, timeout=1000000):
    """
    Fonction pour simuler pulseIn() en Arduino.
    Attend que l'état passe à HIGH, puis mesure la durée jusqu'à LOW.
    """
    ser.write(f"R{pin}\n".encode())  # Demander une lecture sur la broche
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        data = ser.readline().decode().strip()
        if data:
            try:
                return int(data)  # Retourner la durée en µs
            except ValueError:
                return 0
    return 0  # Timeout

def mesurer_distance(trig, echo):
    """
    Fonction qui envoie une impulsion sur 'trig' et mesure la réponse sur 'echo'.
    """
    ser.write(f"W{trig},0\n".encode())  # Mettre trig à LOW
    time.sleep(0.002)
    
    ser.write(f"W{trig},1\n".encode())  # Impulsion HIGH
    time.sleep(0.002)
    ser.write(f"W{trig},0\n".encode())  # Retour à LOW

    duree = pulseIn(echo)  # Mesurer le temps de réponse
    distance = duree * 0.034 / 2  # Convertir en cm
    
    return distance

# Définition des broches
trigCapteurAv, echoCapteurAv = 30, 31
trigCapteurD, echoCapteurD = 36, 37
trigCapteurG, echoCapteurG = 42, 43

# Boucle principale pour lire les distances
while True:
    dist_av = mesurer_distance(trigCapteurAv, echoCapteurAv)
    dist_d = mesurer_distance(trigCapteurD, echoCapteurD)
    dist_g = mesurer_distance(trigCapteurG, echoCapteurG)

    print(f"Avant: {dist_av} cm | Droite: {dist_d} cm | Gauche: {dist_g} cm")
    
    time.sleep(1)  # Pause avant la prochaine mesure
