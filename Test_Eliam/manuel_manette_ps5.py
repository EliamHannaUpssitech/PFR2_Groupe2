import pygame
import asyncio
from bleak import BleakClient
import threading
import time

# Adresse du module Bluetooth HM10
HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

commande_partagee = "x"
envoyer_commande = True
vitesse = 200
arreter = False

# Mappings des boutons manette PS5 (DualSense)
mappings = {
    10: 'a',  # A => augmenter vitesse
    6: 'x',   # X => arrêt
    9: 'e',   # L1 => diminuer vitesse
    11: 'z',  # R1 => augmenter vitesse
    12: 's'   # Y => reculer
}

# Remplacements spécifiques
START_BUTTON_INDEX = 6           # Start (Options)
GAUCHE_BUTTON_INDEX = 13         # Flèche gauche
DROITE_BUTTON_INDEX = 14         # Flèche droite
R1_AS_TRIGGER_INDEX = 10         # R2 ne marche pas → R1 (déjà dans mappings)

def boucle_manette():
    global commande_partagee, envoyer_commande, arreter

    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("Aucune manette détectée.")
        arreter = True
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Manette détectée : {joystick.get_name()}")

    while not arreter:
        pygame.event.pump()
        boutons_actuels = set()

        for btn_index, cmd in mappings.items():
            if joystick.get_button(btn_index):
                boutons_actuels.add(cmd)

        # Bouton "Options" pour arrêter
        if joystick.get_button(START_BUTTON_INDEX):
            print("Bouton Start détecté. Arrêt du programme.")
            print("Veuillez attendre 5 sec que la déconnexion se fasse")
            arreter = True
            return

        # Flèches directionnelles
        if joystick.get_button(DROITE_BUTTON_INDEX):
            boutons_actuels.add('d')
        if joystick.get_button(GAUCHE_BUTTON_INDEX):
            boutons_actuels.add('q')

        if boutons_actuels:
            commande_actuelle = list(boutons_actuels)[0]
            commande_partagee = commande_actuelle
            envoyer_commande = True
        else:
            if commande_partagee != 'x':
                commande_partagee = 'x'
                envoyer_commande = True

        time.sleep(0.05)

async def boucle_ble():
    global commande_partagee, envoyer_commande, vitesse, arreter

    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion BLE échouée")
            return
        print("Connecté au module HM-10")

        while not arreter:
            if envoyer_commande:
                try:
                    cmd = commande_partagee
                    await client.write_gatt_char(UART_CHAR_UUID, (cmd + "\n").encode())

                    if cmd == 'a':
                        vitesse = min(255, vitesse + 25)
                        print(f"[+ Vitesse] => {vitesse}")
                    elif cmd == 'e':
                        vitesse = max(0, vitesse - 25)
                        print(f"[- Vitesse] => {vitesse}")
                    elif cmd == 'x':
                        print(f"[Repos] => x")
                    else:
                        print(f"[Commande] => {cmd}")

                except Exception as e:
                    print(f"Erreur BLE : {e}")
                envoyer_commande = False

            await asyncio.sleep(0.1)

def reinitialiser_etat():
    global commande_partagee, envoyer_commande, vitesse, arreter
    commande_partagee = "x"
    envoyer_commande = True
    vitesse = 200
    arreter = False

def run_asyncio_loop():
    global arreter
    thread_manette = threading.Thread(target=boucle_manette)
    thread_manette.start()
    asyncio.run(boucle_ble())
    arreter = True
    thread_manette.join()
    pygame.quit()
    print("Programme stoppé !")

def main_manette_ps5():
    reinitialiser_etat()
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
    return
