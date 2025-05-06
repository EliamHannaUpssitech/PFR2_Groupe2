import asyncio
import keyboard
from bleak import BleakClient

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

delay = 0.1  # Délai entre les vérifications clavier

async def main():
    print(f"🔌 Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not await client.is_connected():
            print("❌ Connexion échouée")
            return
        print("✅ Connecté au module HM-10")

        derniere_commande = None  # Suivi de la dernière commande envoyée

        try:
            while True:
                commande = 'x'  # Arrêt par défaut

                if keyboard.is_pressed('l'):
                    commande = 'l'

                if commande != derniere_commande:
                    try:
                        await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())
                        derniere_commande = commande
                    except Exception as e:
                        print(f"❌ Erreur BLE : {e}")

                await asyncio.sleep(delay)

        except KeyboardInterrupt:
            print("\n🛑 Arrêt par l'utilisateur.")

if __name__ == "__main__":
    asyncio.run(main())
