from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from object_details import *
from manuel_clavier import *
from manuel_manette import *

def mainIHM():
    global last_menu, langue

    refresh()
    last_menu = "main"

    text_name = Label(IHM, text="--( MYNSSL )--", font=('broadway' , 25))
    text_name.place(x=350, y=45)

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_power = Button(IHM, command=exit, bg=None)
    img_power = PhotoImage(file=str(path_img) + "power_button.png").subsample(7, 7)
    btn_power.config(image=img_power)
    btn_power.place(x=25, y=25)
    if(langue=='FR'):   text_power = Label(IHM, text="Eteindre le\nprogramme")
    elif(langue=='EN'): text_power = Label(IHM, text="Switch off\nthe program")
    text_power.place(x=29, y=105)

    btn_qm = Button(IHM, command=modeHelp, bg=None)
    img_qm = PhotoImage(file=str(path_img) + "qm_button.png").subsample(19, 19)
    btn_qm.config(image=img_qm)
    btn_qm.place(x=845, y=525)
    if(langue=='FR'):   text_qm = Label(IHM, text="Aide ?")
    elif(langue=='EN'): text_qm = Label(IHM, text="Help ?")
    text_qm.place(x=848, y=505)

    btn_manuel = Button(IHM, command=modeManuel, bg=None)
    img_manuel = PhotoImage(file=str(path_img) + "M_button.png").subsample(4, 4)
    btn_manuel.config(image=img_manuel)
    btn_manuel.place(x=233, y=183)
    if(langue=='FR'):   text_manuel = Label(IHM, text="Mode Manuel")
    elif(langue=='EN'): text_manuel = Label(IHM, text="Manual mode")
    text_manuel.place(x=263, y=163)

    btn_vocal = Button(IHM, command=modeVocal, bg=None)
    img_vocal = PhotoImage(file=str(path_img) + "V_button.png").subsample(4, 4)
    btn_vocal.config(image=img_vocal)
    btn_vocal.place(x=233, y=383)
    if(langue=='FR'):   text_vocal = Label(IHM, text="Mode Vocal")
    elif(langue=='EN'): text_vocal = Label(IHM, text="Vocal mode")
    text_vocal.place(x=268, y=363)

    btn_autom = Button(IHM, command=modeAutom, bg=None)
    img_autom = PhotoImage(file=str(path_img) + "A_button.png").subsample(4, 4)
    btn_autom.config(image=img_autom)
    btn_autom.place(x=533, y=183)
    if(langue=='FR'):   text_vocal = Label(IHM, text="Mode Automatisme")
    elif(langue=='EN'): text_vocal = Label(IHM, text="Automation Mode")
    text_vocal.place(x=547, y=163)

    btn_image = Button(IHM, command=modeImage, bg=None)
    img_image = PhotoImage(file=str(path_img) + "I_button.png").subsample(4, 4)
    btn_image.config(image=img_image)
    btn_image.place(x=533, y=383)
    if(langue=='FR'):   text_vocal = Label(IHM, text="Mode Image")
    elif(langue=='EN'): text_vocal = Label(IHM, text="Picture Mode")
    text_vocal.place(x=562, y=363)

    IHM.mainloop()

# MANUEL ------------------------------
def modeManuel():
    global last_menu, langue

    xarrow = 100
    yarrow = 250
    
    refresh()
    last_menu = "manuel"

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file=str(path_img) + "return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)
    if(langue=='FR'):
        text_return = Label(IHM, text="Retour au\nmenu de base")
        text_return.place(x=26, y=105)
    elif(langue=='EN'):
        text_return = Label(IHM, text="Back to\nmain menu")
        text_return.place(x=30, y=105)

    btn_car = Button(IHM, command=cmd_test, bg=None)
    img_car = PhotoImage(file=str(path_img) + "car_button.png").subsample(8, 8)
    btn_car.config(image=img_car)
    btn_car.place(x=87+xarrow, y=-170+yarrow)
    if(langue=='FR'):
        text_car = Label(IHM, text="Connexion\npour flèches")
    elif(langue=='EN'):
        text_car = Label(IHM, text="Connection\nfor arrows")
    text_car.place(x=119+xarrow, y=-210+yarrow)

    btn_up = Button(IHM, command=cmd_test, bg=None)
    img_up = PhotoImage(file=str(path_img) + "Up_button.png").subsample(5, 5)
    btn_up.config(image=img_up)
    btn_up.place(x=100+xarrow, y=0+yarrow)

    btn_down = Button(IHM, command=cmd_test, bg=None)
    img_down = PhotoImage(file=str(path_img) + "Down_button.png").subsample(5, 5)
    btn_down.config(image=img_down)
    btn_down.place(x=100+xarrow, y=200+yarrow)

    btn_left = Button(IHM, command=cmd_test, bg=None)
    img_left = PhotoImage(file=str(path_img) + "Left_button.png").subsample(5, 5)
    btn_left.config(image=img_left)
    btn_left.place(x=0+xarrow, y=100+yarrow)

    btn_right = Button(IHM, command=cmd_test, bg=None)
    img_right = PhotoImage(file=str(path_img) + "Right_button.png").subsample(5, 5)
    btn_right.config(image=img_right)
    btn_right.place(x=200+xarrow, y=100+yarrow)

    btn_clavier = Button(IHM, command=commandeManuelClavier, bg=None)
    img_clavier = PhotoImage(file=str(path_img) + "clavier_button.png").subsample(4, 4)
    btn_clavier.config(image=img_clavier)
    btn_clavier.place(x=600, y=100)
    if(langue=='FR'):
        text_car = Label(IHM, text="Connexion\npour clavier")
    elif(langue=='EN'):
        text_car = Label(IHM, text="Connection\nfor keyboard")
    text_car.place(x=631, y=235)

    btn_manette = Button(IHM, command=commandeManuelManette, bg=None)
    img_manette = PhotoImage(file=str(path_img) + "manette_button.png").subsample(4, 4)
    btn_manette.config(image=img_manette)
    btn_manette.place(x=600, y=360)
    if(langue=='FR'):
        text_manette = Label(IHM, text="Connexion\npour manette")
    elif(langue=='EN'):
        text_manette = Label(IHM, text="Connection\nfor controller")
    text_manette.place(x=630, y=500)

    IHM.mainloop()
##########

# VOCAL ------------------------------
def modeVocal():
    global last_menu, langue

    refresh()
    last_menu = "vocal"

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file=str(path_img) + "return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)
    if(langue=='FR'):
        text_return = Label(IHM, text="Retour au\nmenu de base")
        text_return.place(x=26, y=105)
    elif(langue=='EN'):
        text_return = Label(IHM, text="Back to\nmain menu")
        text_return.place(x=30, y=105)

    btn_micro = Button(IHM, command=cmd_test, bg=None)
    img_micro = PhotoImage(file=str(path_img) + "Micro_button.png").subsample(7, 7)
    btn_micro.config(image=img_micro)
    btn_micro.place(x=100, y=250)

    text_vocal = Text(IHM, bg=None, height=33, width=55)
    text_vocal.place(x=300, y=35)
    text_vocal.config(state=DISABLED)

    IHM.mainloop()
##########

# AUTOMATISME ------------------------------
def modeAutom():
    global last_menu, langue
    
    refresh()
    last_menu = "autom"

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file=str(path_img) + "return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)
    if(langue=='FR'):
        text_return = Label(IHM, text="Retour au\nmenu de base")
        text_return.place(x=26, y=105)
    elif(langue=='EN'):
        text_return = Label(IHM, text="Back to\nmain menu")
        text_return.place(x=30, y=105)

    btn_carto = Button(IHM, command=modeCarto, bg=None)
    img_carto = PhotoImage(file=str(path_img) + "carto_button.png").subsample(3, 3)
    btn_carto.config(image=img_carto)
    btn_carto.place(x=183, y=186)

    btn_trajet = Button(IHM, command=modeTrajet, bg=None)
    img_trajet = PhotoImage(file=str(path_img) + "trajet_button.png").subsample(2, 2)
    btn_trajet.config(image=img_trajet)
    btn_trajet.place(x=533, y=180)

    IHM.mainloop()

def modeCarto():
    global last_menu, langue

    refresh()
    last_menu = "carto"

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_retour = Button(IHM, command=modeAutom, bg=None)
    img_return = PhotoImage(file=str(path_img) + "return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)
    if(langue=='FR'):
        text_return = Label(IHM, text="Retour au\nmenu de base")
        text_return.place(x=26, y=105)
    elif(langue=='EN'):
        text_return = Label(IHM, text="Back to\nmain menu")
        text_return.place(x=30, y=105)

    IHM.mainloop()

def modeTrajet():
    global last_menu, langue

    refresh()
    last_menu = "trajet"

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_retour = Button(IHM, command=modeAutom, bg=None)
    img_return = PhotoImage(file=str(path_img) + "return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)
    if(langue=='FR'):
        text_return = Label(IHM, text="Retour au\nmenu de base")
        text_return.place(x=26, y=105)
    elif(langue=='EN'):
        text_return = Label(IHM, text="Back to\nmain menu")
        text_return.place(x=30, y=105)

    IHM.mainloop()
##########

# IMAGE ------------------------------
def modeImage():
    global last_menu, langue
    
    refresh()
    last_menu = "image"

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file=str(path_img) + "return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)
    if(langue=='FR'):
        text_return = Label(IHM, text="Retour au\nmenu de base")
        text_return.place(x=26, y=105)
    elif(langue=='EN'):
        text_return = Label(IHM, text="Back to\nmain menu")
        text_return.place(x=30, y=105)

    # Images 16/9 1920x1080
    image = "Test_Eliam/images_tests/image_1102.png"
    img = Image.open(image).resize((747,420), Image.Resampling.LANCZOS)

    image_affichee = ImageTk.PhotoImage(img)
    image_analysee = Label(IHM,image=image_affichee)
    image_analysee.place(x=25, y=145)

    cac = carac_obj(image)

    text_image = Text(IHM, bg=None, height=6, width=70)
    text_image.place(x=150, y=25)
    for obj in range(cac[3]):
        text_image.insert(str(obj+1) + ".0", "Objet " + str(obj+1) + " : " + str(cac[0][obj]) + " " + str(cac[1][obj]) + "\n")
    text_image.config(state=DISABLED)

    IHM.mainloop()

# HELP ------------------------------
def modeHelp():
    global last_menu, langue

    refresh()
    last_menu = "help"

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file=str(path_img) + "fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file=str(path_img) + "us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)
    if(langue=='FR'):   text_langue = Label(IHM, text="Changer la\nlangue")
    elif(langue=='EN'): text_langue = Label(IHM, text="Change the\nlangage")
    text_langue.place(x=777, y=97)

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file=str(path_img) + "return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)
    if(langue=='FR'):
        text_return = Label(IHM, text="Retour au\nmenu de base")
        text_return.place(x=26, y=105)
    elif(langue=='EN'):
        text_return = Label(IHM, text="Back to\nmain menu")
        text_return.place(x=30, y=105)

    if(langue=='FR'):
        text_help = Label(IHM, text=
                          "--( Bienvenue sur l'IHM : )--\n"
                          "\nMode Manuel :\n"
                          "- Utiliser les flèches : commencez par appuyer sur le bouton connexion au-dessus de celles-ci, puis attendez, ensuite le robot bougera avec les flèches.\n"
                          "- Utiliser le clavier : commencez par appuyer sur le bouton de connexion clavier, puis attendez, ensuite le robot bougera à l'aide des touches" 
                          " \n(z, q, s, d) (avant, gauche, bas, droite).\n"
                          "- Utiliser une manette :  commencez par appuyer sur le bouton de connexion manette, puis attendez, ensuite le robot bougera à l'aide de la manette.\n"

                          "\nMode Automatisme :\n"
                          "- Faire une cartographie : commencez par appuyer sur le bouton Cartographie, puis attendez, ensuite le robot se déplacera dans l'espace afin de faire" 
                          " \nune carte de la pièce qui s'affichera à la fin du chemin.\n"
                          "- Trouver un objet : commencez par appuyer sur le bouton Trajet, puis attendez, ensuite spécifiez l'objet voulu et lancez le trajet, le robot se" 
                          " \nchargera d'aller vers l'objet voulu.\n"

                          "\nMode Vocal :\n"
                          "- Commander par vocal : commencez par appuyer sur le bouton vocal, puis attendez, ensuite parlez pour commander le robot."
                          " \nVos commandes apparaissent sur l'IHM.\n"

                          "\nMode Image :\n"
                          "- Analyser l'image actuelle : Lorsque le mode Image est lancé, le robot se charge de prendre en photo la scène en face de lui et analysera les objets" 
                          " \n(ici balles) et affichera l'ensemble de ceux-ci sur l'IHM.\n", justify=LEFT)
    elif(langue=='EN'):
        text_help = Label(IHM, text=
                          "--( Welcome to the HMI : )--\n"
                          "\nManual mode :\n"
                          "- Using the arrows: start by pressing the connect button above them, then wait, then the robot will move with the arrows.\n"
                          "- Using the keyboard: start by pressing the keyboard connection button, then wait, then the robot will move using the keys" 
                          " \n(forward, left, down, right).\n"
                          "- Using a joystick: first press the joystick connection button, then wait, then the robot will move using the joystick.\n"

                          "\nAutomation mode :\n"
                          "- Make a map: start by pressing the Map button, then wait, then the robot will move in space to make"
                          " \na map of the room, which will be displayed at the end of the path.\n" 
                          "- Find an object: start by pressing the Path button, then wait, then specify the desired object and launch the path"
                          " \nThe robot will then go to the desired object.\n"

                          "\nVocal mode :\n"
                          "- Command by voice: first press the voice button, then wait, then speak to command the robot"
                          " \nYour commands appear on the HMI.\n"

                          "\nPicture Mode :\n"
                          "- Analyze the current image: When Image mode is launched, the robot takes photos of the scene in front of it and analyzes the objects"
                          " \n(in this case, balls) and display them on the HMI.\n", justify=LEFT)
    text_help.place(x=55, y=180)

    IHM.mainloop()
##########

# OTHERS & ADDONS ------------------------------
def refresh():
    for widget in IHM.winfo_children():
        widget.destroy()

def language_change():
    global langue
    if(langue == "FR"):
        langue = "EN"
    elif(langue == "EN"):
        langue = "FR"
    menuBack()

def menuBack():
    global last_menu
    if last_menu == "manuel":
        modeManuel()
    elif last_menu == "vocal":
        modeVocal()
    elif last_menu == "autom":
        modeAutom()
    elif last_menu == "image":
        modeImage()
    elif last_menu == "carto":
        modeCarto()
    elif last_menu == "trajet":
        modeTrajet()
    elif last_menu == "help":
        modeHelp()
    else:
        mainIHM()

def cmd_test():
    print('commande test passée') 

###########################

# Variables Globales Obligatoires
langue = "FR"
last_menu = "main"
path_img = "Test_Eliam/images_IHM/"

# Début du programme
IHM = Tk()
IHM.geometry('900x600')
#IHM.configure(bg="gray",relief="raised")

mainIHM()

##
#

