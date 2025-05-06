import serial
import time

# Connexion au port série (ajuste COM4 si nécessaire)
try:
    ser = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2)  # Attendre la connexion
except serial.SerialException as e:
    print("Erreur de connexion série :", e)
    exit(1)

def send_serial(command):
    """Envoie une commande formatée au port série."""
    ser.write(f"{command}\n".encode())

def pulseIn(pin, timeout=1000000):
    """
    Fonction pour simuler pulseIn() en Arduino.
    Attend que l'état passe à HIGH, puis mesure la durée jusqu'à LOW.
    """
    send_serial(f"R{pin}")  # Demander une lecture sur la broche
    start_time = time.time()
    
    while (time.time() - start_time) < (timeout / 1_000_000):  # timeout en µs
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
    send_serial(f"W{trig},0")  # Mettre trig à LOW
    time.sleep(0.002)
    
    send_serial(f"W{trig},1")  # Impulsion HIGH
    time.sleep(0.002)
    send_serial(f"W{trig},0")  # Retour à LOW

    duree = pulseIn(echo)  # Mesurer le temps de réponse
    distance = duree * 0.034 / 2  # Convertir en cm
    
    return distance

# Définition des broches
trigCapteurAv, echoCapteurAv = 30, 31
trigCapteurD, echoCapteurD = 36, 37
trigCapteurG, echoCapteurG = 42, 43

# Boucle principale pour lire les distances
try:
    while True:
        dist_av = mesurer_distance(trigCapteurAv, echoCapteurAv)
        dist_d = mesurer_distance(trigCapteurD, echoCapteurD)
        dist_g = mesurer_distance(trigCapteurG, echoCapteurG)

        print(f"Avant: {dist_av:.1f} cm | Droite: {dist_d:.1f} cm | Gauche: {dist_g:.1f} cm")
        
        time.sleep(1)  # Pause avant la prochaine mesure

except KeyboardInterrupt:
    print("\nArrêt du programme.")
    ser.close()
