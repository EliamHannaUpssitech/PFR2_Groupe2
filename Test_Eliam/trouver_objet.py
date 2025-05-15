import asyncio
from bleak import BleakClient
from object_details import *  # La fonction ne prend aucun argument
import threading

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

DELAI = 0.1
TOLERANCE_CENTRAGE = 200  # Valeur pour x de marge

formes = None
couleurs = None
positions = None
nb = None

async def envoyer(client, commande):
    await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())
    print(f"Envoye : {commande}")
    await asyncio.sleep(DELAI)

async def recentrer_objet(client, couleur_cible, tolerance, tentatives):
    global positions, couleurs, positions, nb
    """Effectue un centrage de l'objet cible, retourne True si reussi"""
    for _ in range(tentatives):

        if _ > 0: take_picture()
        await asyncio.sleep(3)

        if couleur_cible not in couleurs:
            print("Objet non detecte pendant recentrage.")
            return False

        index = couleurs.index(couleur_cible)
        x = positions[index][0]
        print(f"Recentrage : x = {x}")

        if abs(x - 960) <= TOLERANCE_CENTRAGE/tolerance:
            print("Objet centre.")
            return True

        direction = 'h' if x > 960 else 'g'
        await envoyer(client, direction)
        await envoyer(client, 'x')
        await asyncio.sleep(0.8)

    print("echec du recentrage.")
    return False

async def trouver_objet(couleur_cible):
    global formes, couleurs, positions, nb
    print(f"Connexion a {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion echouee.")
            return
        print("Connecte au module HM-10")

        await envoyer(client, 'm')
        await envoyer(client, 'x')
        trouve = False
        while not trouve:
            for tentative in range(5):
                print(f"\nTentative {tentative+1}/5 - Analyse camera...")
                take_picture()

                if couleur_cible in couleurs:
                    index = couleurs.index(couleur_cible)
                    x = positions[index][0]
                    print(f"Objet {couleur_cible} detecte a x = {x}")

                    # Centrage initial
                    centre = await recentrer_objet(client, couleur_cible, 1, 6)
                    if not centre:
                        continue

                    # Avance jusqu’a 50 cm
                    await envoyer(client, 'v')
                    await asyncio.sleep(2.5)
                    await envoyer(client, 'm')
                    await envoyer(client, 'x')

                    # Recentrage a nouveau
                    print("Recentrage après avancee...")
                    take_picture()
                    await asyncio.sleep(2)
                    centre = await recentrer_objet(client, couleur_cible, 2, 4)
                    if not centre:
                        continue

                    # Approche lente
                    print("Approche finale lente...")
                    await envoyer(client, 'w')
                    await asyncio.sleep(2.5)
                    await envoyer(client, 'm')
                    await envoyer(client, 'x')

                    print("Objet atteint avec succès.")
                    trouve = True
                    return

                else:
                    print(f"Objet {couleur_cible} non visible. Rotation droite.")
                    await envoyer(client, 'n')
                    await asyncio.sleep(0.6)
                    await envoyer(client, 'x')

            print("echec : Objet non trouve après 5 tentatives. Mode libre.")
            await envoyer(client, 'o')
            await asyncio.sleep(5)
            await envoyer(client, 'm')
            await envoyer(client, 'x')

def take_picture():
    global formes, couleurs, positions, nb
    infos = carac_obj()
    formes, couleurs, positions, nb = infos[0], infos[1], infos[2], infos[3]

# Couleurs ------------------------------

def TO_orange():
    thread = threading.Thread(target=run_asyncio_loop_orange)
    thread.start()
def run_asyncio_loop_orange():
    couleur_cible = "Orange"
    asyncio.run(trouver_objet(couleur_cible))
    print("Programme stoppé !")

def TO_jaune():
    thread = threading.Thread(target=run_asyncio_loop_jaune)
    thread.start()
def run_asyncio_loop_jaune():
    couleur_cible = "Jaune"
    asyncio.run(trouver_objet(couleur_cible))
    print("Programme stoppé !")

def TO_rouge():
    thread = threading.Thread(target=run_asyncio_loop_rouge)
    thread.start()
def run_asyncio_loop_rouge():
    couleur_cible = "Rouge"
    asyncio.run(trouver_objet(couleur_cible))
    print("Programme stoppé !")

def TO_vert():
    thread = threading.Thread(target=run_asyncio_loop_vert)
    thread.start()
def run_asyncio_loop_vert():
    couleur_cible = "Vert"
    asyncio.run(trouver_objet(couleur_cible))
    print("Programme stoppé !")

def TO_bleu():
    thread = threading.Thread(target=run_asyncio_loop_bleu)
    thread.start()
def run_asyncio_loop_bleu():
    couleur_cible = "Bleu"
    asyncio.run(trouver_objet(couleur_cible))
    print("Programme stoppé !")

def TO_violet():
    thread = threading.Thread(target=run_asyncio_loop_violet)
    thread.start()
def run_asyncio_loop_violet():
    couleur_cible = "Violet"
    asyncio.run(trouver_objet(couleur_cible))
    print("Programme stoppé !")

##
#
