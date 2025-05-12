import asyncio
import keyboard
from bleak import BleakClient
import threading

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"#"F7B2E471-0B6C-B447-B9A7-8890E71BFFDB"
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

            if keyboard.is_pressed('z'):
                commande = 'z'
            elif keyboard.is_pressed('q'):
                commande = 'q'
            elif keyboard.is_pressed('s'):
                commande = 's'
            elif keyboard.is_pressed('d'):
                commande = 'd'
            elif keyboard.is_pressed('a'):
                commande = 'a'
            elif keyboard.is_pressed('e'):
                commande = 'e'

            if commande != derniere_commande:
                try:
                    await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())

                    if commande == 'a':
                        vitesse = min(255, vitesse + 25)
                        print(f"Vitesse augmentée : {vitesse}")
                    elif commande == 'e':
                        vitesse = max(0, vitesse - 25)
                        print(f"Vitesse diminuée : {vitesse}")
                    else:
                        print(f"Envoyée : {commande}")

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

def commandeManuelClavier():
    reinitialiser_etat()
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
    return
