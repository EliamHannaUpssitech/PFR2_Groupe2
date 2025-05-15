import cv2
import numpy as np
import os
import time

def detect_color_hsv(img_hsv):
    # Masques pour chaque couleur
    masks = {}

    # ----------- ROUGE -----------
    lower_orange_red = np.array([0, 100, 50])
    upper_orange_red = np.array([10, 255, 255])
    lower_red = np.array([160, 100, 50])
    upper_red = np.array([180, 255, 255])
    mask_red = cv2.inRange(img_hsv, lower_orange_red, upper_orange_red) | cv2.inRange(img_hsv, lower_red, upper_red)
    masks['Rouge'] = mask_red

    # ----------- ORANGE -----------
    lower_orange = np.array([10, 100, 50])
    upper_orange = np.array([25, 255, 255])
    mask_orange = cv2.inRange(img_hsv, lower_orange, upper_orange)
    masks['Orange'] = mask_orange

    # ----------- JAUNE -----------
    lower_yellow = np.array([25, 100, 50])
    upper_yellow = np.array([35, 255, 255])
    mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    masks['Jaune'] = mask_yellow

    # ----------- VERT -----------
    lower_light_green = np.array([36, 100, 50])
    upper_light_green = np.array([54, 255, 255])
    lower_dark_green = np.array([55, 100, 50])
    upper_dark_green = np.array([85, 255, 255])
    mask_green = cv2.inRange(img_hsv, lower_light_green, upper_light_green) | cv2.inRange(img_hsv, lower_dark_green, upper_dark_green)
    masks['Vert'] = mask_green

    # ----------- BLEU -----------
    lower_very_light_blue = np.array([80, 10, 180])
    upper_very_light_blue = np.array([100, 80, 255])
    lower_cyan = np.array([80, 100, 100])
    upper_cyan = np.array([95, 255, 255])
    lower_mid_blue = np.array([95, 100, 50])
    upper_mid_blue = np.array([115, 255, 255])
    lower_dark_blue = np.array([115, 100, 30])
    upper_dark_blue = np.array([130, 255, 180])
    mask_blue = (
        cv2.inRange(img_hsv, lower_very_light_blue, upper_very_light_blue) |
        cv2.inRange(img_hsv, lower_cyan, upper_cyan) |
        cv2.inRange(img_hsv, lower_mid_blue, upper_mid_blue) |
        cv2.inRange(img_hsv, lower_dark_blue, upper_dark_blue))
    masks['Bleu'] = mask_blue

    # ----------- VIOLET -----------
    lower_violet = np.array([130, 50, 50])
    upper_violet = np.array([160, 255, 255])
    mask_violet = cv2.inRange(img_hsv, lower_violet, upper_violet)
    masks['Violet'] = mask_violet

    detected = []

    for color, mask in masks.items():
        if cv2.countNonZero(mask) > 100:  # seuil à ajuster
            detected.append(color)
    
    if not detected:
        detected.append('Inconnue')

    return detected


def carac_obj():

    os.system('ssh xxneonmain69xx@172.20.10.3 "python3 /home/xxneonmain69xx/PFR/capture_images.py"')
    os.system('exit')

    time.sleep(3)

    image = "\\\\172.20.10.3\Partage\images\Image1.png"

    img_color = cv2.imread(image)
    width, height = 1920, 1080

    # Passage de l'image en HSV pour mieux séparer les couleurs
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

    # Applique un flou sur l'image pour lisser les bordures
    img_blur = cv2.GaussianBlur(img_hsv, (13, 13), 0)

    # Passage de l'image en niveau de gris à partir d'une info HSV afin de séparer les tons (background / objets)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    _,img_thresh = cv2.threshold(img_gray, 137, 255, cv2.THRESH_BINARY)

    # CONTOURS
    ## RETR_EXTERNAL : récupére que contours externes, évite de trouver plusieurs fois les contours internes ou superposés
    ## CHAIN_APPROX_NONE : prend tout les contours et non pas 4 points sur l'objet
    contours, _ = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    objet = False

    nbObjets = 0
    formeObjets = []
    positionObjets = []
    colorObjets = []

    for contour in contours:
        if(np.shape(contour)[0] >= height/15):                          # On évite les bordures parasites
            epsilon = 0.005 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            cv2.drawContours(img_color, [approx], -1, (0, 255, 0), 1)

            num_vertices = len(approx)
            shape_name = ""

            if num_vertices < 8:                                        # Détection carré
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = w / float(h)
                shape_name = "Carre" if 0.9 <= aspect_ratio <= 1.1 else "Rectangle"
                objet = True
            elif len(approx) >= 12:                                     # Détection cercle
                area = cv2.contourArea(contour)
                perimeter = cv2.arcLength(contour, True)
                circularity = (4 * np.pi * area) / (perimeter ** 2)
                if 0.55 <= circularity <= 1.45:
                    shape_name = "Balle"
                    objet = True
            else:
                objet = False

            if(objet == True):
                x, y = approx[0][0]
                cv2.putText(img_color, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

                # POSITION DANS L'IMAGE : détecte selon les bordures le centre de position des objets
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                else:
                    cx, cy = 0, 0
                positionObjets.append([cx, cy])
                ###
                # COULEUR : moyenne de la couleur (R,G,B) à partir du centre de l'objet
                colorKernel = 30
                y1 = positionObjets[nbObjets][1]-colorKernel
                if(y1 < 0):
                    y1 = 0
                y2 = positionObjets[nbObjets][1]+colorKernel
                if(y2 > height):
                    y2 = height
                x1 = positionObjets[nbObjets][0]-colorKernel
                if(x1 < 0):
                    x1 = 0
                x2 = positionObjets[nbObjets][0]+colorKernel
                if(x2 > width):
                    x2 = width
                roi = img_blur[y1:y2, x1:x2]
                if roi.size == 0: colors = ['Inconnue']
                else: 
                    colors = detect_color_hsv(roi)
                colorObjets.append(colors[0])
                ###
                # FORME
                formeObjets.append(shape_name)
                ###
                # NOMBRE OBJETS PRESENTS : Ajout puis reset la présence pour le prochain contour
                nbObjets += 1
                objet = False
                ###

    print("taille image : " + str(height) + ", " + str(width))
    print([formeObjets, colorObjets, positionObjets, nbObjets])
    """
    cv2.imshow("IMG_ + str(i)", img_color)
    cv2.waitKey(0)
    """
    # NOMBRE D'OBJETS : nbObjets
    # FORME : forme = [obj1, obj2, ...]
    # COULEUR : colorObjets = [obj1, obj2, ...] -> objX = [R, G, B]
    # POSITION : positionObjets = [obj1, obj2, ...] -> objX = [posX, posY]
    return([formeObjets, colorObjets, positionObjets, nbObjets])
#carac_obj()

