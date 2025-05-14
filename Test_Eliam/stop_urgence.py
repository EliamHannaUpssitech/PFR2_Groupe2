import asyncio
from bleak import BleakClient
import threading

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

async def main_urgence():
    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée")
            return
        print("Connecté au module HM-10")
    print("Arrêt d'urgence - STOP")
    print("Veuillez attendre 5 sec que la déconnexion se fasse")
    await client.write_gatt_char(UART_CHAR_UUID, ('m\n').encode())
    await client.write_gatt_char(UART_CHAR_UUID, ('x\n').encode())
    return

def run_asyncio_loop():
    asyncio.run(main_urgence())
    print("Programme stoppé !")

def stop_robot():
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
    return

stop_robot()