from tkinter import *
from tkinter import ttk

# Variables Globales Obligatoires
langue = 'FR'

def mainIHM():

    refresh()

    def on_language_change():
        if(selected_value.get() == 'Francais'):
            langue = 'FR'
        elif(selected_value.get() == 'English'):
            langue = 'EN'
        print(langue)

    selected_value = StringVar(value="Francais")
    Radiobutton(IHM, text="Français", variable=selected_value, value="Francais", command=on_language_change).place(x=750, y=40)
    Radiobutton(IHM, text="English", variable=selected_value, value="English", command=on_language_change).place(x=750, y=70)

    btn_power = Button(IHM, command=exit, bg=None)
    img_power = PhotoImage(file="images_IHM/power_button.png").subsample(7, 7)
    btn_power.config(image=img_power)
    btn_power.place(x=25, y=25)

    btn_manuel = Button(IHM, command=modeManuel, bg=None)
    img_manuel = PhotoImage(file="images_IHM/M_button.png").subsample(4, 4)
    btn_manuel.config(image=img_manuel)
    btn_manuel.place(x=233, y=183)

    btn_vocal = Button(IHM, command=modeVocal, bg=None)
    img_vocal = PhotoImage(file="images_IHM/V_button.png").subsample(4, 4)
    btn_vocal.config(image=img_vocal)
    btn_vocal.place(x=233, y=383)

    btn_autom = Button(IHM, command=modeAutom, bg=None)
    img_autom = PhotoImage(file="images_IHM/A_button.png").subsample(4, 4)
    btn_autom.config(image=img_autom)
    btn_autom.place(x=533, y=183)

    btn_image = Button(IHM, command=modeImage, bg=None)
    img_image = PhotoImage(file="images_IHM/I_button.png").subsample(4, 4)
    btn_image.config(image=img_image)
    btn_image.place(x=533, y=383)

    IHM.mainloop()

def modeManuel():

    xarrow = 100
    yarrow = 150
    
    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    btn_up = Button(IHM, command=cmd_test, bg=None)
    img_up = PhotoImage(file="images_IHM/Up_button.png").subsample(5, 5)
    btn_up.config(image=img_up)
    btn_up.place(x=100+xarrow, y=0+yarrow)

    btn_down = Button(IHM, command=cmd_test, bg=None)
    img_down = PhotoImage(file="images_IHM/Down_button.png").subsample(5, 5)
    btn_down.config(image=img_down)
    btn_down.place(x=100+xarrow, y=200+yarrow)

    btn_left = Button(IHM, command=cmd_test, bg=None)
    img_left = PhotoImage(file="images_IHM/Left_button.png").subsample(5, 5)
    btn_left.config(image=img_left)
    btn_left.place(x=0+xarrow, y=100+yarrow)

    btn_right = Button(IHM, command=cmd_test, bg=None)
    img_right = PhotoImage(file="images_IHM/Right_button.png").subsample(5, 5)
    btn_right.config(image=img_right)
    btn_right.place(x=200+xarrow, y=100+yarrow)

    btn_car = Button(IHM, command=cmd_test, bg=None)
    img_car = PhotoImage(file="images_IHM/car_button.png").subsample(7, 7)
    btn_car.config(image=img_car)
    btn_car.place(x=600, y=230)

    IHM.mainloop()

    """
    if langue == "FR":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixM = 0
            print("Bienvenue dans le mode manuel\n")
            print("Tout d'abord sachez que vous pouvez arreter le programme à tout moment avec la commande 'stop'\n")
            print("Dans ce menu vous pouvez faire:\n")
            print(" 1- Se deplacer manuellement\n 2- Retour au menu précédent\n")
            choixM = int(input("Entrez votre choix : "))

            if(choixM < 1 or choixM > 2):
                print("Veuillez choisir un nombre entre 1 et 2 pour accéder à ce que vous voulez faire.\n")
                print(" 1- Se deplacer manuellement\n 2- Retour au menu précédent\n")
                choixM = int(input("Entrez votre choix : ")) 

            if (choixM == 1):
                print("ModeManuel()")
            if(choixM == 2):
                return 0
        except Exception as e:
            print(f"Arrêt forcée de la fonction: {e}")
            return 0
    elif langue == "EN":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixM = 0
            print("Welcome to manual mode\n")
            print("First of all know that you can stop the program at any time with the 'stop' command\n")
            print("In this menu you can do:\n")
            print(" 1- Move manually\n 2- Return to previous menu\n")
            choixM = int(input("Enter your choice: "))

            if(choixM < 1 or choixM > 2):
                print("Please choose a number between 1 and 2 to access what you want to do.\n")
                print(" 1- Move manually\n 2- Return to previous menu\n")
                choixM = int(input("Enter your choice: "))  

            if (choixM == 1):
                print("ModeManuel()")
            if(choixM == 2):
                return 0
        except Exception as e:
            print(f"Forced shutdown of function: {e}")
            return 0
        """
        

def modeVocal():

    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    btn_micro = Button(IHM, command=cmd_test, bg=None)
    img_micro = PhotoImage(file="images_IHM/Micro_button.png").subsample(7, 7)
    btn_micro.config(image=img_micro)
    btn_micro.place(x=200, y=250)

    

    IHM.mainloop()

    """
    if langue == "FR":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixV = 0
            print("Bienvenue dans le mode vocale\n")
            print("Tout d'abord sachez que vous pouvez arreter le programme à tout moment avec la commande 'stop'\n")
            print("Dans ce menu vous pouvez faire:\n")
            print(" 1- Se deplacer vocalement\n 2- Retour au menu précédent\n")
            choixV = int(input("Entrez votre choix : "))

            if(choixV < 1 or choixV > 2):
                print("Veuillez choisir un nombre entre 1 et 2 pour accéder à ce que vous voulez faire.\n")
                print(" 1- Se deplacer vocalement\n 2- Retour au menu précédent\n")
                choixV = int(input("Entrez votre choix : "))

            if (choixV == 1):
                print("ModeVocal()")
            if(choixV == 2):
                return 0
        except Exception as e:
            print(f"Arrêt forcée de la fonction: {e}")
            return 0
    elif langue == "EN":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixV = 0
            print("Welcome to voice mode\n")
            print("First of all, you can stop the program at any time with the 'stop' command\n")
            print("In this menu you can do:\n")
            print(" 1- Move vocally\n 2- Return to previous menu\n")
            choixV = int(input("Enter your choice: "))

            if(choixV < 1 or choixV > 2):
                print("Please choose a number between 1 and 2 to access what you want to do.\n")
                print(" 1- Move vocally\n 2- Return to previous menu\n")
                choixV = int(input("Enter your choice: "))

            if (choixV == 1):
                print("ModeVocal()")
            if(choixV == 2):
                return 0
        except Exception as e:
            print(f"Forced shutdown of function: {e}")
            return 0
        """


def modeAutom():
    
    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    

    IHM.mainloop()

    """
    if langue == "FR":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixA = 0
            print("Bienvenue dans le mode automatique\n")
            print("Tout d'abord sachez que vous pouvez arreter le programme à tout moment avec la commande 'stop'\n")
            print("Dans ce menu vous pouvez faire:\n")
            print(" 1- Se deplacer automatiquement\n 2- Retour au menu précédent\n")
            choixA = int(input("Entrez votre choix : "))

            if(choixA < 1 or choixA > 2):
                print("Veuillez choisir un nombre entre 1 et 2 pour accéder à ce que vous voulez faire.\n")
                print(" 1- Se deplacer automatiquement\n 2- Retour au menu précédent\n")
                choixA = int(input("Entrez votre choix : "))

            if (choixA == 1):
                print("ModeAutomatique()")
            if(choixA == 2):
                return 0
        except Exception as e:
            print(f"Arrêt forcée de la fonction: {e}")
            return 0
    elif langue == "EN":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixA = 0
            print("Welcome to automatic mode\n")
            print("First of all, you can stop the program at any time with the 'stop' command\n")
            print("In this menu you can do:\n")
            print(" 1- Move automatically\n 2- Return to previous menu\n")
            choixA = int(input("Enter your choice: "))

            if(choixA < 1 or choixA > 2):
                print("Please choose a number between 1 and 2 to access what you want to do.\n")
                print(" 1- Move automatically\n 2- Return to previous menu\n")
                choixA = int(input("Enter your choice:"))

            if (choixA == 1):
                print("ModeAutomatique()")
            if(choixA == 2):
                return 0
        except Exception as e:
            print(f"Forced shutdown of function: {e}")
            return 0
        """


def modeImage():
    
    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    

    IHM.mainloop()

    """
    if langue == "FR":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixI = 0
            print("Bienvenue dans le mode image\n")
            print("Tout d'abord sachez que vous pouvez arreter le programme à tout moment avec la commande 'stop'\n")
            print("Dans ce menu vous pouvez faire:\n")
            print(" 1- Prendre une image\n 2- Retour au menu précédent\n")
            choixI = int(input("Entrez votre choix : "))

            if(choixI < 1 or choixI > 2):
                print("Veuillez choisir un nombre entre 1 et 2 pour accéder à ce que vous voulez faire.\n")
                print(" 1- Prendre une image\n 2- Retour au menu précédent\n")
                choixI = int(input("Entrez votre choix : "))

            if (choixI == 1):
                print("ModeImage()")
            if(choixI == 2):
                return 0
        except Exception as e:
            print(f"Arrêt forcée de la fonction: {e}")
            return 0
    elif langue == "EN":
        try:
            print("\n//////////////////////////////////////////////////////////\n")
            choixI = 0
            print("Welcome to image mode\n")
            print("First of all, you can stop the program at any time with the 'stop' command\n")
            print("In this menu you can do:\n")
            print("1- take an image\n 2- Return to previous menu\n")
            choixI = int(input("Enter your choice: "))

            if(choixI < 1 or choixI > 2):
                print("Please choose a number between 1 and 2 to access what you want to do.\n")
                print("1- Take a picture \n 2- Return to previous menu\n")
                choixI = int(input("Enter your choice:  "))

            if (choixI == 1):
                print("ModeImage()")
            if(choixI == 2):
                return 0
        except Exception as e:
            print(f"Forced shutdown of function: {e}")
            return 0
        """

"""
def choixLangue():
    print("Veuillez choisir la langue d'utilisation pour le robot\n")
    print("Veuillez entrer FR pour le français ou EN pour l'anglais\n")
    valLangue = str(input("Entrez votre choix : "))
    while(valLangue != "FR" and valLangue != "EN"):
        print("Veuillez entrer une valeur valide\n")
        valLangue = str(input("Entrez votre choix : "))
    if(valLangue == "FR"):
        print("L'utilisation du robot est maintenant en Francais\n")
        return "FR"
    elif(valLangue == "EN"):
        print("Using the robot is now in English\n")
        return "EN"
"""

def refresh():
    for widget in IHM.winfo_children():
        widget.destroy()

def cmd_test():
    print('commande test passée')

###########################

IHM = Tk()
IHM.geometry('900x600')
#IHM.configure(bg="gray",relief="raised")

mainIHM()

