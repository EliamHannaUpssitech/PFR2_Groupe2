import asyncio
import re
import speech_recognition as sr
from bleak import BleakClient

# Adresse Bluetooth
HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

def normaliser_transcription(transcription):
    return transcription.lower().split()

def vocal_commande(transcription):
    tokens = normaliser_transcription(transcription)
    commandes = []

    for i, token in enumerate(tokens):
        if token in ["avance", "avancer"]:
            commandes.append("t")
        elif token in ["recule", "reculer"]:
            commandes.append("g")
        elif token in ["tourne", "tourner"]:
            if i + 2 < len(tokens) and tokens[i + 1] in ["à", "de"]:
                direction = tokens[i + 2]
                if direction == "gauche":
                    commandes.append("f")
                elif direction == "droite":
                    commandes.append("h")
        elif token in ["stop", "arrête", "arrete", "arrêter", "pause"]:
            commandes.append("x")
        elif token in ["demi-tour", "demitour", "retourne", "retourner"]:
            commandes.append("k")
    
    return commandes



# Boucle principale d'écoute + envoi BLE
async def boucle_vocale(client):
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("\nParlez maintenant (ou dites 'stop' pour arrêter)...")
            recognizer.adjust_for_ambient_noise(source)  # Ajuste le bruit ambiant
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)  # Écoute jusqu'à la fin de la phrase
                print("Reconnaissance...")
                transcription = recognizer.recognize_google(audio, language="fr-FR")  # Utilise l'API Google
                print(f"Vous avez dit : {transcription}")
                commandes = vocal_commande(transcription)

                if not commandes:
                    print("Aucune commande reconnue.")
                    continue

                if "x" in commandes:
                    print("Commande d'arrêt détectée. Fin du programme.")
                    await client.write_gatt_char(UART_CHAR_UUID, ("m\n").encode())
                    await client.write_gatt_char(UART_CHAR_UUID, ("x\n").encode())
                    break

                for cmd in commandes:
                    await client.write_gatt_char(UART_CHAR_UUID, (cmd + "\n").encode())
                    print(f"Envoyé : {cmd}")
                    await asyncio.sleep(0.3)

                # Envoi automatique du "x"
                await asyncio.sleep(1)
                await client.write_gatt_char(UART_CHAR_UUID, ("x\n").encode())
                print("Arrêt automatique envoyé (x)")

            except sr.UnknownValueError:
                print("Je n'ai pas compris.")
            except sr.RequestError as e:
                print(f"Erreur API Google : {e}")
            except Exception as e:
                print(f"Erreur inattendue : {e}")



async def main():
    print(f"Connexion à {HM10_ADDRESS}...")
    async with BleakClient(HM10_ADDRESS) as client:
        if not client.is_connected:
            print("Connexion échouée.")
            return
        print("Connecté au module HM-10.")
        await client.write_gatt_char(UART_CHAR_UUID, ("j\n").encode())#passe en mode vocal
        await boucle_vocale(client)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Arrêt manuel.")
