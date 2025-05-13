import asyncio
import re
import speech_recognition as sr
from bleak import BleakClient
import threading

# Adresse Bluetooth
HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

transcription = None

def normaliser_transcription(transcription):
    return transcription.lower().split()

def decouper_en_commandes(transcription):
    return re.split(r"\b(?:et|puis|ensuite|,|;|\.|\bet après\b)\b", transcription.lower())

def extraire_commandes(sous_phrase):
    tokens = normaliser_transcription(sous_phrase)
    commandes = []
    duree = 0.9  # durée par défaut en secondes

    for i, token in enumerate(tokens):
        if token in ["avance", "avancer", "forward"]:
            commandes.append("t")
            if i + 2 < len(tokens) and tokens[i + 1] == "de":
                try:
                    distance = float(tokens[i + 2].replace(",", "."))
                    duree = distance * 1.0
                except ValueError:
                    pass

        elif token in ["recule", "reculer", "back", "backward"]:
            commandes.append("g")
            if i + 2 < len(tokens) and tokens[i + 1] == "de":
                try:
                    distance = float(tokens[i + 2].replace(",", "."))
                    duree = distance * 1.0
                except ValueError:
                    pass

        elif token in ["tourne", "tourner", "turn"]:
            if i + 2 < len(tokens) and tokens[i + 1] in ["à", "de", "to"]:
                direction = tokens[i + 2]
                if direction in ["gauche", "left"]:
                    commandes.append("f")
                elif direction in ["droite", "right"]:
                    commandes.append("h")
            if i + 4 < len(tokens) and tokens[i + 3] == "de":
                try:
                    angle = float(tokens[i + 4].replace("°", "").replace(",", "."))
                    duree = angle / 90.0
                except ValueError:
                    pass

        elif token in ["stop", "arrête", "arrete", "arrêter", "pause", "stoppe"]:
            commandes.append("x")

        elif token in ["demi-tour", "demitour", "retourne", "retourner", "half turn"]:
            commandes.append("f")
            duree = 1.8

        elif token in ["augmente", "accélère", "accelere", "speed"]:
            commandes.append("a")

        elif token in ["ralentis", "diminue", "réduit", "reduit", "ralenti", "slow"]:
            commandes.append("e")

    return commandes, duree


async def boucle_vocale(client):
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("\nParlez maintenant (ou dites 'stop' pour arrêter)...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                print("Reconnaissance...")
                transcription = recognizer.recognize_google(audio, language="fr-FR")
                print(f"Vous avez dit : {transcription}")

                phrases = decouper_en_commandes(transcription)
                toutes_les_commandes = []

                for phrase in phrases:
                    commandes, duree = extraire_commandes(phrase)
                    if commandes:
                        toutes_les_commandes.append((commandes, duree))

                if not toutes_les_commandes:
                    print("Aucune commande reconnue.")
                    continue

                for commandes, duree in toutes_les_commandes:
                    if "x" in commandes:
                        print("Commande d'arrêt détectée. Fin du programme.")
                        await client.write_gatt_char(UART_CHAR_UUID, ("m\n").encode())
                        await client.write_gatt_char(UART_CHAR_UUID, ("x\n").encode())
                        return

                    for cmd in commandes:
                        await client.write_gatt_char(UART_CHAR_UUID, (cmd + "\n").encode())
                        print(f"Envoyé : {cmd}")
                        await asyncio.sleep(0.3)

                    await asyncio.sleep(duree)
                    await client.write_gatt_char(UART_CHAR_UUID, ("x\n").encode())
                    print("Arrêt automatique envoyé (x)")

            except sr.UnknownValueError:
                print("Je n'ai pas compris.")
            except sr.RequestError as e:
                print(f"Erreur API Google : {e}")
            except Exception as e:
                print(f"Erreur inattendue : {e}")

async def bclvocal():
    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée.")
            return
        print("Connecté au module HM-10.")
        await client.write_gatt_char(UART_CHAR_UUID, ("j\n").encode())  # mode vocal
        await boucle_vocale(client)

def run_asyncio_loop():
    asyncio.run(bclvocal())
    print("Programme stoppé !")

def main_vocal():
    thread = threading.Thread(target=run_asyncio_loop)
    thread.start()

def get_transcription():
    return transcription
