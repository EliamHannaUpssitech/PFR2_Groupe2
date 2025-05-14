import asyncio
import keyboard
from bleak import BleakClient
import threading

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

delay = 0.1
derniere_commande = None
vitesse = 200  # suivi local pour affichage
arreter = False

async def main_manuel():
    global delay, derniere_commande, vitesse, arreter
    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée")
            return
        print("Connecté au module HM-10")

        global derniere_commande, vitesse

        while not arreter:
            if keyboard.is_pressed('space'):
                print("Arrêt demandé (espace pressée)")
                print("Veuillez attendre 5 sec que la déconnexion se fasse")
                arreter = True
                await client.write_gatt_char(UART_CHAR_UUID, ('m\n').encode())
                await client.write_gatt_char(UART_CHAR_UUID, ('x\n').encode())
                return

            commande = 'x'  # Commande par défaut

            if commande != derniere_commande:
                try:
                    await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())
                    derniere_commande = commande
                except Exception as e:
                    print(f"Erreur BLE : {e}")

            await asyncio.sleep(delay)

def reinitialiser_etat():
    global delay, derniere_commande, vitesse, arreter
    delay = 0.1
    derniere_commande = None
    vitesse = 200  # suivi local pour affichage
    arreter = False

def run_asyncio_loop():
    asyncio.run(main_manuel())
    print("Programme stoppé !")

def cmd_arrow():
    reinitialiser_etat()
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
    return
