from Quartz import CGEventCreateKeyboardEvent, CGEventPost
from Quartz import kCGHIDEventTap
import time

# Code de la touche 'z' selon le keycode macOS (QWERTY : 6, AZERTY : 6 aussi)
KEY_Z = 6

def press_key_z():
    # Appui sur 'z'
    key_down = CGEventCreateKeyboardEvent(None, KEY_Z, True)
    # Relâchement de 'z'
    key_up = CGEventCreateKeyboardEvent(None, KEY_Z, False)

    # Envoi des événements
    CGEventPost(kCGHIDEventTap, key_down)
    CGEventPost(kCGHIDEventTap, key_up)

# Test
press_key_z()