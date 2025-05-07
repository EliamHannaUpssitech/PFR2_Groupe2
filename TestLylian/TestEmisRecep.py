import asyncio
import keyboard
from bleak import BleakClient

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
delay = 0.1

# Liste pour stocker les distances : [Avant, Droite, Gauche]
distances = [None, None, None]

def notification_handler(sender, data):
    """
    Traite les messages de type 'AV:134.2', 'D:125.0', 'G:145.0'.
    """
    msg = data.decode().strip()
    print(f"📥 Reçu : {msg}")

    try:
        capteur, valeur = msg.split(":")
        val = float(valeur.strip())

        if capteur == "AV":
            distances[0] = val
        elif capteur == "D":
            distances[1] = val
        elif capteur == "G":
            distances[2] = val

    except:
        print("⚠️ Donnée mal formée ou invalide.")

async def main():
    print(f"🔌 Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not await client.is_connected():
            print("❌ Connexion échouée")
            return
        print("✅ Connecté")

        await client.start_notify(UART_CHAR_UUID, notification_handler)

        derniere_commande = None

        try:
            while True:
                commande = 'x'
                if keyboard.is_pressed('l'):
                    commande = 'l'

                if commande != derniere_commande:
                    await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())
                    derniere_commande = commande

                print(f"🧭 Avant: {distances[0]} | Droite: {distances[1]} | Gauche: {distances[2]}")
                await asyncio.sleep(1)

        except KeyboardInterrupt:
            print("\n🛑 Arrêté par l'utilisateur.")
        finally:
            await client.stop_notify(UART_CHAR_UUID)

if __name__ == "__main__":
    asyncio.run(main())
