import asyncio
from bleak import BleakScanner

async def scan():
    print("🔍 Scan BLE en cours (5 secondes)...")
    devices = await BleakScanner.discover(timeout=5.0)
    if devices:
        print("📋 Appareils trouvés :")
        for d in devices:
            print(f" - {d.name or 'Inconnu'} : {d.address}")
    else:
        print("❌ Aucun appareil BLE détecté.")

if __name__ == "__main__":
    asyncio.run(scan())
