import requests
import time

# Adresse IP de la Raspberry Pi et port du serveur
rasp_ip = "http://192.168.1.42:5000/distance"  # Changez l'IP si nécessaire

while True:
    try:
        response = requests.get(rasp_ip)
        data = response.json()
        print(f"Donnée reçue : {data}")
    except Exception as e:
        print(f"Erreur lors de la récupération des données : {e}")
    
    time.sleep(1)  # Demander toutes les secondes