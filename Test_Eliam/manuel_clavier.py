import asyncio
import keyboard
from bleak import BleakClient
import threading

HM10_ADDRESS = "F7B2E471-0B6C-B447-B9A7-8890E71BFFDB"#"D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

delay = 0.1
derniere_commande = None
vitesse = 200  # suivi local pour affichage

async def main_manuel():
    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée")
            return
        print("Connecté au module HM-10")

        global derniere_commande, vitesse

        while True:
            if keyboard.is_pressed('space'):
                print("Arrêt demandé (espace pressée)")
                await client.write_gatt_char(UART_CHAR_UUID, ('m\n').encode())
                await client.write_gatt_char(UART_CHAR_UUID, ('x\n').encode())
                break

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

def run_asyncio_loop():
    asyncio.run(main_manuel())

def commandeManuelClavier():
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
