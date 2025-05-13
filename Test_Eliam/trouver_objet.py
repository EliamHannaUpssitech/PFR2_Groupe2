import asyncio
from bleak import BleakClient
import time
from object_details import *  # La fonction ne prend aucun argument

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

DELAI = 0.1
TOLERANCE_CENTRAGE = 100  # Valeur pour x dans [445, 645]
couleurs = None
positions = None

async def envoyer(client, commande):
    await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())
    print(f"Envoye : {commande}")
    await asyncio.sleep(DELAI)

async def recentrer_objet(client, couleur_cible):
    global couleurs, positions
    """Effectue un centrage de l'objet cible, retourne True si reussi"""
    for _ in range(6):
        infos = carac_obj()
        #formes, couleurs, positions, nb = infos
        couleurs = infos[1] 
        positions = infos[2]

        if couleur_cible not in couleurs:
            print("Objet non detecte pendant recentrage.")
            return False

        index = couleurs.index(couleur_cible)
        x = positions[index][0]
        print(f"Recentrage : x = {x}")

        if abs(x - 960) <= TOLERANCE_CENTRAGE:
            print("Objet centre.")
            return True

        direction = 'g' if x > 960 else 'h'
        await envoyer(client, direction)
        await envoyer(client, 'x')
        await asyncio.sleep(0.8)

    print("echec du recentrage.")
    return False

async def trouver_objet(couleur_cible):
    global couleurs, positions
    print(f"Connexion a {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion echouee.")
            return
        print("Connecte au module HM-10")

        await envoyer(client, 'm')
        await envoyer(client, 'x')

        for tentative in range(5):
            print(f"\nTentative {tentative+1}/5 - Analyse camera...")
            #formes, couleurs, positions, nb = carac_obj()
            infos = carac_obj()
            couleurs = infos[1] 
            positions = infos[2]

            if couleur_cible in couleurs:
                index = couleurs.index(couleur_cible)
                x = positions[index][0]
                print(f"Objet {couleur_cible} detecte a x = {x}")

                # Centrage initial
                centre = await recentrer_objet(client, couleur_cible)
                if not centre:
                    continue

                # Avance jusqu’a 50 cm
                await envoyer(client, 'v')
                await asyncio.sleep(2.5)
                await envoyer(client, 'm')
                await envoyer(client, 'x')

                # Recentrage a nouveau
                print("Recentrage après avancee...")
                centre = await recentrer_objet(client, couleur_cible)
                if not centre:
                    continue

                # Approche lente
                print("Approche finale lente...")
                await envoyer(client, 'w')
                await asyncio.sleep(2.5)
                await envoyer(client, 'm')
                await envoyer(client, 'x')

                print("Objet atteint avec succès.")
                return

            else:
                print(f"Objet {couleur_cible} non visible. Rotation droite.")
                await envoyer(client, 'd')
                await asyncio.sleep(0.6)
                await envoyer(client, 'x')

        print("echec : Objet non trouve après 5 tentatives. Mode libre.")
        await envoyer(client, 'o')
        await asyncio.sleep(20)
        await envoyer(client, 'm')
        await envoyer(client, 'x')

# Exemple d'execution
if __name__ == "__main__":
    couleur_cible = "Jaune"  # a ajuster
    asyncio.run(trouver_objet(couleur_cible))