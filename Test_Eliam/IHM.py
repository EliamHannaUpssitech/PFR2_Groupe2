from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from object_details import *
from CommandeManuelBT_int import *

def mainIHM():

    refresh()

    btn_flag = Button(IHM, command=language_change, bg=None)
    if(langue == 'FR'): img_flag = PhotoImage(file="Test_Eliam/images_IHM/fr_flag.png").subsample(4, 4)
    if(langue == 'EN'): img_flag = PhotoImage(file="Test_Eliam/images_IHM/us_flag.png").subsample(4, 4)
    btn_flag.config(image=img_flag)
    btn_flag.place(x=775, y=25)

    btn_power = Button(IHM, command=exit, bg=None)
    img_power = PhotoImage(file="Test_Eliam/images_IHM/power_button.png").subsample(7, 7)
    btn_power.config(image=img_power)
    btn_power.place(x=25, y=25)

    btn_manuel = Button(IHM, command=modeManuel, bg=None)
    img_manuel = PhotoImage(file="Test_Eliam/images_IHM/M_button.png").subsample(4, 4)
    btn_manuel.config(image=img_manuel)
    btn_manuel.place(x=233, y=183)

    btn_vocal = Button(IHM, command=modeVocal, bg=None)
    img_vocal = PhotoImage(file="Test_Eliam/images_IHM/V_button.png").subsample(4, 4)
    btn_vocal.config(image=img_vocal)
    btn_vocal.place(x=233, y=383)

    btn_autom = Button(IHM, command=modeAutom, bg=None)
    img_autom = PhotoImage(file="Test_Eliam/images_IHM/A_button.png").subsample(4, 4)
    btn_autom.config(image=img_autom)
    btn_autom.place(x=533, y=183)

    btn_image = Button(IHM, command=modeImage, bg=None)
    img_image = PhotoImage(file="Test_Eliam/images_IHM/I_button.png").subsample(4, 4)
    btn_image.config(image=img_image)
    btn_image.place(x=533, y=383)

    IHM.mainloop()

# MANUEL ------------------------------
def modeManuel():

    xarrow = 100
    yarrow = 150
    
    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="Test_Eliam/images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    btn_up = Button(IHM, command=cmd_test, bg=None)
    img_up = PhotoImage(file="Test_Eliam/images_IHM/Up_button.png").subsample(5, 5)
    btn_up.config(image=img_up)
    btn_up.place(x=100+xarrow, y=0+yarrow)

    btn_down = Button(IHM, command=cmd_test, bg=None)
    img_down = PhotoImage(file="Test_Eliam/images_IHM/Down_button.png").subsample(5, 5)
    btn_down.config(image=img_down)
    btn_down.place(x=100+xarrow, y=200+yarrow)

    btn_left = Button(IHM, command=cmd_test, bg=None)
    img_left = PhotoImage(file="Test_Eliam/images_IHM/Left_button.png").subsample(5, 5)
    btn_left.config(image=img_left)
    btn_left.place(x=0+xarrow, y=100+yarrow)

    btn_right = Button(IHM, command=cmd_test, bg=None)
    img_right = PhotoImage(file="Test_Eliam/images_IHM/Right_button.png").subsample(5, 5)
    btn_right.config(image=img_right)
    btn_right.place(x=200+xarrow, y=100+yarrow)

    btn_clavier = Button(IHM, command=commandeManuel, bg=None)
    img_clavier = PhotoImage(file="Test_Eliam/images_IHM/clavier_button.png").subsample(4, 4)
    btn_clavier.config(image=img_clavier)
    btn_clavier.place(x=600, y=130)

    btn_manette = Button(IHM, command=cmd_test, bg=None)
    img_manette = PhotoImage(file="Test_Eliam/images_IHM/manette_button.png").subsample(4, 4)
    btn_manette.config(image=img_manette)
    btn_manette.place(x=600, y=330)

    IHM.mainloop()
##########

# VOCAL ------------------------------
def modeVocal():

    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="Test_Eliam/images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    btn_micro = Button(IHM, command=cmd_test, bg=None)
    img_micro = PhotoImage(file="Test_Eliam/images_IHM/Micro_button.png").subsample(7, 7)
    btn_micro.config(image=img_micro)
    btn_micro.place(x=150, y=250)

    text_vocal = Text(IHM, bg=None, height=40, width=60)
    text_vocal.place(x=400, y=35)

    IHM.mainloop()
##########

# AUTOMATISME ------------------------------
def modeAutom():
    
    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="Test_Eliam/images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    btn_carto = Button(IHM, command=modeCarto, bg=None)
    img_carto = PhotoImage(file="Test_Eliam/images_IHM/carto_button.png").subsample(3, 3)
    btn_carto.config(image=img_carto)
    btn_carto.place(x=233, y=183)

    btn_trajet = Button(IHM, command=modeTrajet, bg=None)
    img_trajet = PhotoImage(file="Test_Eliam/images_IHM/trajet_button.png").subsample(2, 2)
    btn_trajet.config(image=img_trajet)
    btn_trajet.place(x=533, y=183)

    IHM.mainloop()

def modeCarto():

    refresh()

    btn_retour = Button(IHM, command=modeAutom, bg=None)
    img_return = PhotoImage(file="Test_Eliam/images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    IHM.mainloop()

def modeTrajet():

    refresh()

    btn_retour = Button(IHM, command=modeAutom, bg=None)
    img_return = PhotoImage(file="Test_Eliam/images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    IHM.mainloop()
##########

# IMAGE ------------------------------
def modeImage():
    
    refresh()

    btn_retour = Button(IHM, command=mainIHM, bg=None)
    img_return = PhotoImage(file="Test_Eliam/images_IHM/return_button.png").subsample(7, 7)
    btn_retour.config(image=img_return)
    btn_retour.place(x=25, y=25)

    # Images 16/9 1920x1080
    image = "Test_Eliam/images_tests/image_1102.png"
    img = Image.open(image).resize((747,420), Image.Resampling.LANCZOS)

    image_affichee = ImageTk.PhotoImage(img)
    image_analysee = Label(IHM,image=image_affichee)
    image_analysee.place(x=25, y=125)

    cac = carac_obj(image)

    text_image = Text(IHM, bg=None, height=5, width=100)
    text_image.place(x=150, y=25)
    for obj in range(cac[3]):
        text_image.insert(str(obj+1) + ".0", "Objet " + str(obj+1) + " : " + str(cac[0][obj]) + " " + str(cac[1][obj]) + "\n")

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
    mainIHM()

def cmd_test():
    print('commande test passée')

###########################

# Variables Globales Obligatoires
langue = "FR"

IHM = Tk()
IHM.geometry('900x600')
#IHM.configure(bg="gray",relief="raised")

mainIHM()

