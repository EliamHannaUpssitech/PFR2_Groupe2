import serial

PORT = '/dev/ttyACM0' 
FICHIER = "/home/xxneonmain69xx/PFR/distance.txt"

def enregistrer_dist():
    try:
        arduino = serial.Serial(PORT, 9600, timeout=1)
    except Exception as e:
        print(f"Erreur de port série : {e}")
        exit(1)

    print("En attente d'une valeur...")

    try:
        while True:
            ligne = arduino.readline().decode().strip()
            if ligne.isdigit():
                contenu = f"{ligne}\n"
                with open(FICHIER, "w") as f:
                    f.write(contenu)
                print(f"Valeur enregistrée : {contenu.strip()}")
                break
    except KeyboardInterrupt:
        print("\nArrêté manuellement.")
    finally:
        arduino.close()

