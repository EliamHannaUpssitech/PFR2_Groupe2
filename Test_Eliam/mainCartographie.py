import serial
import serial.tools.list_ports
from rplidar import RPLidar
import time
import matplotlib.pyplot as plt
import math
import asyncio
from bleak import BleakClient
import keyboard
from enregistrer_dist import *

listDeplacement=[]
CarteGlobale=[]
distance_capteur_avant=300              # oublie pas de le supp
delay = 0.1  # Délai entre les vérifications clavier pour envoieDemande fonction

def action():
    global modeCarthographie
    modeCarthographie = False    
    print("fin carthographie")

keyboard.add_hotkey('space', action)

HM10_ADDRESS = "D8:A9:8B:C4:5F:EC"
UART_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
distance_capteur_lidar=200 #20 cm
marge_init_lidar=20
marge_angle_lidar=5                                                    #REMET MARGE DE 2 
distance_de_securite=200
vitesse_robot=667 #mm/s
vitesse_rotation=50
distance_Recule=50



keyboard.add_hotkey('a', action)
def initCartographie() :
    return True

def detect_lidar_port():
    """Détecte les ports série disponibles et tente de trouver un LiDAR."""
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if 'Silicon Labs CP210x USB to UART Bridge' in port.description :
            return port.device  # Retourne le port qui semble être celui du LiDAR
    return None

def getCoordonne(angle, distance,deplacement):
    #Convertit les coordonnées polaires en coordonnées cartésiennes. et prend en compte le déplacement précédent du robot
    x = distance * math.cos(math.radians(angle)+deplacement[0])
    y = distance * math.sin(math.radians(angle)+deplacement[1])
    return x, y

def read_rplidar(port,CarteGlobale):
    max_scans=10
    #Lit les données du LiDAR et retourne une liste d'angles et distances
    print("Utilisation du protocole RPLIDAR...")
    lidar = RPLidar(port)

    try:
        lidar.reset()
        time.sleep(2)
        for i, scan in enumerate(lidar.iter_scans()):
            if i >= max_scans:  # Stop après `max_scans`
                break
            for (_, angle, distance) in scan:
                if distance > 0:  # Vérifie si distance valide
                    CarteGlobale.append((angle, distance))
                
                    
                    

    except KeyboardInterrupt:
        print("Arrêt du LiDAR...")
    finally:
        lidar.stop()
        lidar.disconnect()

    return CarteGlobale

def init_lidar(distance_capteur_avant):
    port = detect_lidar_port()
    if not port:
            print("Aucun LiDAR détecté.")
            exit()
    lidar = RPLidar(port)
    try:
        lidar.reset()
        time.sleep(2)
        for i, scan in enumerate(lidar.iter_scans()):
            if i >= 10:  # ou une autre valeur de max_scans
                break
            for (_, angle, distance) in scan:
                cible = distance_capteur_avant + distance_capteur_lidar
                if abs(distance - cible) < marge_init_lidar:  # marge d’erreur
                    return angle  
        return None  
    finally:
        lidar.stop()
        lidar.disconnect()



def carthographie_Lidar(CarteGlobale,listDeplacement) :
    def carthographie(CarteGlobale):
        #Affiche la cartographie des points relevés.
        x_vals = []
        y_vals = []
        deplacement=somme_des_deplacements(listDeplacement)
        for angle, distance in CarteGlobale:
            x, y = getCoordonne(angle, distance,deplacement)
            x_vals.append(x)
            y_vals.append(y)

        plt.figure(figsize=(8, 8))
        plt.plot(x_vals, y_vals, marker='o', linestyle='', markersize=2, color='blue')  # pour imiter un scatter
        plt.title("Cartographie")
        plt.xlabel("X (mm)")
        plt.ylabel("Y (mm)")
        plt.grid()
        plt.savefig("Downloads/ma_Cartographie.png", dpi=300)  
        plt.show()  
      


    # === Programme principal ===
    port = detect_lidar_port()
    if not port:
        print("Aucun LiDAR détecté.")
        exit()

    print(f"LiDAR détecté sur {port}")
        
    CarteGlobale = read_rplidar(port,CarteGlobale)  # Récupérer les données
    carthographie(CarteGlobale)  # Afficher la carte
    return CarteGlobale  

def presence_objet(angle_face_robot,port, max_scans=10) :


    if not port:
        print("Aucun LiDAR détecté.")
        exit()
    lidar = RPLidar(port)
    angle_droite_robot=angle_face_robot+90
    angle_gauche_robot=angle_droite_robot+180 
    try:
        lidar.reset()
        time.sleep(2)
        presence_avant=False
        presence_droite=False
        presence_gauche=False
        distance_avant = None
        distance_droite = None
        distance_gauche = None

        for i, scan in enumerate(lidar.iter_scans()):
            if i >= max_scans:  # ou une autre valeur de max_scans
                break
             
            for (_  , angle, distance) in scan:
                print(angle)
                if abs(angle - angle_face_robot) < marge_angle_lidar:  # marge d’erreur
                    print("bon angle_face_robot trouvé !:",angle," La distance est de :",distance-distance_capteur_lidar)
                    distance_avant=distance
                    if distance-distance_capteur_lidar  <= distance_de_securite :

                        presence_avant=True
                        
                if abs(angle - angle_droite_robot) < marge_angle_lidar:  # marge d’erreur
                    print("bon angle_droite_robot trouvé !:",angle," La distance est de :",distance-distance_capteur_lidar)
                    distance_droite=distance
                    if distance-distance_capteur_lidar  <= distance_de_securite :
                        presence_droite=True
                        


                if abs(angle - angle_gauche_robot) < marge_angle_lidar:  # marge d’erreur
                    print("bon angle_gauche_robot trouvé !:",angle," La distance est de :",distance-distance_capteur_lidar)
                    distance_gauche=distance
                    if distance-distance_capteur_lidar  <= distance_de_securite :
                        presence_gauche=True
                        
               

            
           
    
        
    finally:
        lidar.stop()
        lidar.disconnect()
    distances=(presence_avant,presence_droite,presence_gauche,distance_avant,distance_droite,distance_gauche)
    return distances # tuple (presence_avant : bool ,presence_droite : bool ,presence_gauche : bool ,distance_avant : int ,distance_droite : int ,distance_gauche : int)
    #print("ERREUR : l'angle voulu n'as pas été trouver (devant le robot)")  



#le robot va forcément tourner quand il detecte un obstacle (il recule aussi un peu)
def calculDeplacement(angle_face_robot):
    tourner=False
    port = detect_lidar_port()
    while (True) :                                              # permet quand ona tourné de revenir à avancer pour faire une boucle tourner = quand on a detecter la distance de sécurté à l'angle en face du robot
        presenceObjet = presence_objet(angle_face_robot,port)        #tuple (0 presence_avant : bool ,1 presence_droite : bool ,2 presence_gauche : bool ,3 distance_avant : int ,4 distance_droite : int ,5 distance_gauche : int)
        print("il est passé")
        if (not presenceObjet[0]):                              #avancer
            print("pas d'objet")
            old_time=time.time()
            while (not presenceObjet[0]) :                      #permet d'attendre tant que il n'ya pas d'objet
                presenceObjet = presence_objet(angle_face_robot,port)
                print("presnce objet il avance : ",presenceObjet[0])
            temps_timer=time.time()-old_time
            print("le temps qu'il prend à avancer est : ", temps_timer)
            distance=vitesse_robot*temps_timer
            if(tourner):
                distance_x= math.cos (angle) *(distance+distance_Recule)
                distance_y= math.sin(angle)* (distance+distance_Recule)

            else: 
                distance_x=distance
                distance_y=0
            
            deplacement=(distance_x,distance_y)
            tourner = False
            break
        elif presenceObjet :
            #print("objet")
            old_time=time.time()
            sensDeRotation =1                                   #1 pour horraire -1 pour anti horaire car le robot va tourner dans la direction ou il y a le plus de distance
            if (presenceObjet[1] and presenceObjet[2]) :        # Si Quand tu as un obstacle devant et à droite et à gauche tu regarde sur les coté l'endroit ou tu as le plus de distance pour t'y diriger, permet de determiner dans quel sens va tourner le robot
                distanceObjetDroite=presenceObjet[4]
                distanceObjetGauche=presenceObjet[5]
                if distanceObjetDroite<=distanceObjetGauche :
                    sensDeRotation=-1
            elif (presenceObjet[1]) :
                sensDeRotation=-1
  
            while (presenceObjet[0]) :
                presenceObjet = presence_objet(angle_face_robot,port)
                print(" Pas presnce objet il tourne : ",presenceObjet[0])

            temps_timer=time.time()-old_time
            print("le temps qu'il prend à tourner à droite est : ", temps_timer)
            tourner=True
            angle = vitesse_rotation*temps_timer*sensDeRotation

    return deplacement 

def somme_des_deplacements(listDeplacement) :
    j=len(listDeplacement)
    deplacement_x=0
    deplacement_y=0
    print("Contenu de listDeplacement :", listDeplacement)
    print("Type de listDeplacement[0] :", type(listDeplacement[0]))
    print("Valeur de listDeplacement[0] :", listDeplacement[0])
    for i in range(j) :
        deplacement_x += listDeplacement[i][0]
        deplacement_y += listDeplacement[i][1]
    deplacement=(deplacement_x,deplacement_y)
    return deplacement

def envoi_demande(demande) :
    async def main():
        print(f"🔌 Connexion à {HM10_ADDRESS}...")
        async with BleakClient(HM10_ADDRESS) as client:
            if not await client.is_connected():
                print("❌ Connexion échouée")
                return
            print("✅ Connecté au module HM-10")

            derniere_commande = None  # Suivi de la dernière commande envoyée

            try:
                while True:
                    if ("distance"):
                            enregistrer_dist()
                    elif ("deplacement"):
                            commande = 'o' # lancer mode autom 
                    else :
                            commande = 'm' # fermer
                            commande = 'x' # fermer le mode autom

                    if commande != derniere_commande:
                        try:
                            await client.write_gatt_char(UART_CHAR_UUID, (commande + "\n").encode())
                            derniere_commande = commande
                        except Exception as e:
                            print(f"❌ Erreur BLE : {e}")

                    await asyncio.sleep(delay)

            except KeyboardInterrupt:
                print("\n🛑 Arrêt par l'utilisateur.")

    if __name__ == "__main__":
     asyncio.run(main())


# distance_capteur_avant=envoi_demande("distance") #demande lylian comment faire                                                          #pas tester (1) attendre comment faire lylian pour recevoir la valeur de distance du capteur de devant
#angle_face_robot=init_lidar(distance_capteur_avant)
angle_face_robot=0 
modeCarthographie=initCartographie()                                                                                    # tester (2) experimentalement (pas condition réel avec vrai donné (manque vrai distance capteur avant+distance_capteur_avant))
while(modeCarthographie):                                                                                                               
    envoi_demande("deplacement")            # lance le déplacement libre                                                                #pas tester (1)
    for i in range(1) :   # fait tous les 10 mouvement à reflechir si 10
        listDeplacement.append(calculDeplacement(angle_face_robot))                                                     # tester (2)  experimentalement (pas condition réel avec vrai donné (manque vrai vitesse de déplacement+vitesse de rotation+distance capteur avant+distance de sécurité)) 
    envoi_demande("fin_deplacement")          # fini le déplacement libre                                                               #pas tester (1)
    CarteGlobale=carthographie_Lidar(CarteGlobale,listDeplacement)  # analyse Lidar + Traitement donnees Lidar + Mise a jour Carte      #fonctionne mais pas tester depuis maj







### rajouter un verif qui ne rajoute à la carte que des points qui n'existe pas
### mettre la carte sous forme d'image en png


### crée un environment pour verifier que la carte s'actualise bien
