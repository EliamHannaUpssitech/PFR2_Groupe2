# controle_robot.py
from queue import Queue
import asyncio
import threading
from bleak import BleakClient

# Fonction manuel arrow 
# Fonctionnement :
#   Connexion au robot puis appuyer sur les flèches présentes dans le mode Manuel de l'IHM fera bouger le robot

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

commande_queue = Queue()
derniere_commande = None
arreter = False

def envoyer_commande(commande):
    commande_queue.put(commande)

def reinitialiser_etat():
    global derniere_commande, arreter
    derniere_commande = None
    arreter = False

async def main_manuel():
    global derniere_commande, arreter
    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée")
            return
        print("Connecté au module HM-10")

        while not arreter:
            if not commande_queue.empty():
                commande = commande_queue.get()
                if commande != derniere_commande:
                    try:
                        await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())
                        derniere_commande = commande
                    except Exception as e:
                        print(f"Erreur BLE : {e}")
            await asyncio.sleep(0.1)

def run_asyncio_loop():
    asyncio.run(main_manuel())
    print("Programme stoppé !")

def cmd_arrow():
    reinitialiser_etat()
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
