import cv2
import numpy as np

def detect_color_hsv(img_hsv):
    # Masques pour chaque couleur
    masks = {}

    # Rouge = deux plages
    lower_red1 = np.array([0, 100, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 50])
    upper_red2 = np.array([180, 255, 255])
    mask_red = cv2.inRange(img_hsv, lower_red1, upper_red1) | cv2.inRange(img_hsv, lower_red2, upper_red2)

    # Jaune
    lower_yellow = np.array([20, 100, 50])
    upper_yellow = np.array([30, 255, 255])
    mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

    # Vert
    lower_green = np.array([40, 100, 50])
    upper_green = np.array([85, 255, 255])
    mask_green = cv2.inRange(img_hsv, lower_green, upper_green)

    # Bleu
    lower_blue = np.array([90, 100, 50])
    upper_blue = np.array([130, 255, 255])
    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)

    masks['Rouge'] = mask_red
    masks['Jaune'] = mask_yellow
    masks['Vert'] = mask_green
    masks['Bleu'] = mask_blue

    detected = []

    for color, mask in masks.items():
        if cv2.countNonZero(mask) > 100:  # seuil à ajuster
            detected.append(color)

    return detected

def carac_obj(image):
    img_color = cv2.imread(image)
    width, height, _ = img_color.shape

    # Passage de l'image en HSV pour mieux séparer les couleurs
    img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

    # Applique un flou sur l'image pour lisser les bordures
    img_blur = cv2.GaussianBlur(img_hsv, (13, 13), 0)

    # Passage de l'image en niveau de gris à partir d'une info HSV afin de séparer les tons (background / objets)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    _,img_thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

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
        epsilon = 0.005 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        cv2.drawContours(img_color, [approx], -1, (0, 255, 0), 1)

        num_vertices = len(approx)
        shape_name = ""

        if num_vertices == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)
            shape_name = "Carre" if 0.9 <= aspect_ratio <= 1.1 else "" #"Rectangle"
            objet = True
        elif len(approx) >= 12:
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            circularity = (4 * np.pi * area) / (perimeter ** 2)
            if 0.55 <= circularity <= 1.45:
                shape_name = "Cercle"
                objet = True
        else:
            objet = False

        if(objet == True):
            x, y = approx[0][0]
            cv2.putText(img_color, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            for c in contour[nbObjets]:
                positionObjets.append([int(np.mean(c[0])), int(np.mean(c[1]))])
            
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
            colors = detect_color_hsv(roi)
            colorObjets.append(colors)
            
            formeObjets.append(shape_name)

            nbObjets += 1

    print([formeObjets, colorObjets, positionObjets, nbObjets])
    print("\n\n\n\n")

    cv2.imshow("IMG_" + str(i), img_color)
    cv2.waitKey(0)

    # NOMBRE D'OBJETS : nbObjets
    # FORME : forme = [obj1, obj2, ...]
    # COULEUR : colorObjets = [obj1, obj2, ...] -> objX = [R, G, B]
    # POSITION : positionObjets = [obj1, obj2, ...] -> objX = [posX, posY]
    return([formeObjets, colorObjets, positionObjets, nbObjets])

images = list(range(5389, 5408 + 1))
for i in images:
    carac_obj("./IMG_300/IMG_"+ str(i) +".jpeg")
