import asyncio
import keyboard
from bleak import BleakClient

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

delay = 0.1
derniere_commande = None


async def main():
    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée")
            return
        print("Connecté au module HM-10")

        global derniere_commande, vitesse
        commande = 'o'  # Arrêt par défaut
        await client.write_gatt_char(UART_CHAR_UUID, ('o' + "\n").encode())
        while True:

            if keyboard.is_pressed('space'):
                print("Arrêt demandé (espace pressée)")
                await client.write_gatt_char(UART_CHAR_UUID, ('m' + "\n").encode())
                await client.write_gatt_char(UART_CHAR_UUID, ('x' + "\n").encode())  
                break

           
            elif keyboard.is_pressed('m'):
                commande = 'm'
            elif keyboard.is_pressed('s'):
                commande = 's'
            elif keyboard.is_pressed('o'):
                commande = 'o'
            else:
                commande = 'x'

            if commande != derniere_commande:
                try:
                    await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())

                   
                    print(f"Envoyée : {commande}")

                    derniere_commande = commande
                except Exception as e:
                    print(f"Erreur BLE : {e}")

            await asyncio.sleep(delay)

if __name__ == "__main__":
    asyncio.run(main())