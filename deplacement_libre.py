import asyncio
import keyboard
from bleak import BleakClient
import threading

# Fonction déplacement libre
# Fonctionnement :
#   Tant que espace n'est pas appuyé, le programme lancera le mode automatique de l'arduino
#   Le mode automatique avance jusqu'à un obstacle puis selon la place qu'il à sur ses cotés, choisi s'il tourne à gauche ou à droite avant de réavancer
#   'x' ou 'm' mettent en pause le programme tant qu'ils sont appuyés

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

delay = 0.1
derniere_commande = None

async def main_libre():
    print(f"Connexion a {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée")
            return
        print("Connecté au module HM-10")

        global derniere_commande

        arreter = False

        while not arreter:
            if keyboard.is_pressed('space'):
                print("Arrêt demandé (espace pressée)")
                print("Veuillez attendre 5 sec que la déconnexion se fasse")
                arreter = True
                await client.write_gatt_char(UART_CHAR_UUID, ('m\n').encode())
                await client.write_gatt_char(UART_CHAR_UUID, ('x\n').encode())
                return
            
            commande = 'o'

            if keyboard.is_pressed('m'):
                commande = 'm'
            elif keyboard.is_pressed('x'):
                commande = 'x'

            if commande != derniere_commande:
                try:
                    await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())

                    print(f"Envoyée : {commande}")

                    derniere_commande = commande
                except Exception as e:
                    print(f"Erreur BLE : {e}")

            await asyncio.sleep(delay)

def run_asyncio_loop():
    asyncio.run(main_libre())
    print("Programme stoppé !")

def cmd_deplacement_libre():
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
    return