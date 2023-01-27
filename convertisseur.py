
from tkinter import *

from PIL import Image, ImageTk

fenetre = Tk()
fenetre.title("Convertir ses monnaies")

#flag of countries / drapeau des pays 

#tools / outils titre et texte

label_titre_haut = Label(master=fenetre, text="Convertisseur",fg='powderblue')
label_titre_haut.configure(font=("Akira expanded", 20))
fenetre.configure( width=550, height=800 )
label_titre_haut.place( relx=0.5, rely=0.01,anchor=N )
sens = StringVar()

#texte De 

label_choix_monnaie1 = Label(master=fenetre, text= "De", fg='black')
label_choix_monnaie1.configure(font=("Akira expanded", 20))
label_choix_monnaie1.place( relx=0.5, rely=0.10,anchor=N )
sens = StringVar()

#texte A

label_choix_monnaie2 = Label(master=fenetre, text= "A", fg='black')
label_choix_monnaie2.configure(font=("Akira expanded", 20))
label_choix_monnaie2.place( relx=0.5, rely=0.35,anchor=N )
sens = StringVar()

#ajout éléments liste déroulante

devises = {"USD": {"nom_pays": "États-Unis", "nom_devise": "Dollar des États-Unis", "icone": PhotoImage(file="Ce PC/Documents/Python3/country-flags-main/png100px/us.png")}}
    


var_devise = StringVar(fenetre)
var_devise.set("USD")

menu_devise = OptionMenu(fenetre, var_devise, *devises)
menu_devise.config(width=20, font=("Arial", 12))
menu_devise.pack()

icone = ImageTk.PhotoImage(Image.open(devises[var_devise.get()]["icone"]))
label_icone = Label(fenetre, image=icone)
label_icone.pack()

fenetre.mainloop()