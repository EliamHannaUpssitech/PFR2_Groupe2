import pyfirmata
import serial
import time

board = pyfirmata.Arduino('COM4')  # Remplacez 'COM3' par le port approprié de votre Arduino
ser = serial.Serial('COM4', 9600)  # Remplacez 'COM3' par le bon port série

echoCapteurAv = board.get_pin('d:31:i')  # Broche en input 
echoCapteurD = board.get_pin('d:37:i')  # Broche en input
echoCapteurG = board.get_pin('d:43:i')  # Broche en input
trigCapteurAv = board.get_pin('d:30:o')  # Broche en output
trigCapteurD = board.get_pin('d:36:o')  # Broche en output
trigCapteurG = board.get_pin('d:42:o')  # Broche en output

def digitalWrite(pin, state):
    board.digital[pin].write(state)

def pulseIn(pin, value, timeout=20000):
    start_time = time.time()
    duration = 0
    
    while time.time() - start_time < timeout:
        data = ser.read()
        if data == b'H' and value == 'HIGH':
            start_time = time.time()
        elif data == b'L' and value == 'LOW':
            start_time = time.time()
        elif (data == b'L' and value == 'HIGH') or (data == b'H' and value == 'LOW'):
            duration = time.time() - start_time
            return duration * 1000000  # Convertir en microsecondes
    return 0

def mesurerDistance(trig , echo):
    digitalWrite(trig, 0)
    time.sleep(2)
    digitalWrite(trig, 1)
    time.sleep(2)
    digitalWrite(trig, 0)

    duree = pulseIn(echo, 1)
    distance = duree*(0.034/2)

    return distance


#def distanceObjet():
    #if presenceObjet() != 0:
        #mesurerDistance()