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

# Seuils
TRIGGER_THRESHOLD = 0.5
JOYSTICK_THRESHOLD = 0.5

mappings = {
    0: 'a',  # A => augmenter vitesse
    2: 'x',  # X => arrêt
    4: 'e',  # LB => diminuer vitesse
    5: 'a',  # RB => augmenter vitesse
    3: 's'   # Y => reculer
}

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

    START_BUTTON_INDEX = 7

    while not arreter:
        pygame.event.pump()
        boutons_actuels = set()

        # Boutons classiques
        for btn_index, cmd in mappings.items():
            if joystick.get_button(btn_index):
                boutons_actuels.add(cmd)

        # Détection du bouton Start pour arrêter le programme
        if joystick.get_button(START_BUTTON_INDEX):
            print("Bouton Start détecté. Arrêt du programme.")
            print("Veuillez attendre 5 sec que la déconnexion se fasse")
            arreter = True
            break

        # Gâchette
        if joystick.get_axis(5) > TRIGGER_THRESHOLD:
            boutons_actuels.add('z')

        # Croix directionnelle (HAT)
        hat = joystick.get_hat(0)
        if hat == (1, 0):
            boutons_actuels.add('d')
        elif hat == (-1, 0):
            boutons_actuels.add('q')

        # Joystick gauche
        axe_horizontal = joystick.get_axis(0)
        axe_vertical = joystick.get_axis(1)

        if axe_horizontal > JOYSTICK_THRESHOLD:
            boutons_actuels.add('d')
        elif axe_horizontal < -JOYSTICK_THRESHOLD:
            boutons_actuels.add('q')

        if axe_vertical < -JOYSTICK_THRESHOLD:
            boutons_actuels.add('z')
        elif axe_vertical > JOYSTICK_THRESHOLD:
            boutons_actuels.add('s')

        # Si une commande est détectée
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
                        vitesse = min(255, vitesse + 15)
                        print(f"[+ Vitesse] => {vitesse}")
                    elif cmd == 'e':
                        vitesse = max(0, vitesse - 15)
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

def main_manette_xbox():
    reinitialiser_etat()
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()
