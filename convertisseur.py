from tkinter import *

from tkinter import ttk

fenetre = Tk()
fenetre.title("Convertir ses monnaies")
fenetre.geometry("500x700")


#flag of countries / drapeau des pays 

#tools / outils titre et texte

label_titre_haut = Label(master=fenetre, text="Convertisseur",fg='powderblue')
label_titre_haut.configure(font=("Akira expanded", 20))
fenetre.configure( width=550, height=800 , )
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
#premiere liste
def Combo_pays_onselect(evt):
    valeur = Combo_pays.get()
    index = Combo_pays.current()
    print("index: " + str(index) + "valeur: " + valeur )


Combo_pays = ttk.Combobox(fenetre)

Combo_pays["values"] = ("EUR->Europe","USD->USA","JPY->Japon","GBP->angleterre","CHF-> Suisse","INR->Inde","RUB->Russe","CNY->Chine","MXN->Mexique","AUD->Australie","CAD->Canada","ZAR->Afrique du sud",)
Combo_pays["state"] = "readonly"
Combo_pays.pack()
Combo_pays.place( relx=0.5, rely=0.16,anchor=N)



L1 = Label(fenetre,font=("Arial",10),text="Nombre à convertir ->")
L1.pack( side = LEFT)
L1.place(  relx=0.22, rely=0.25,anchor=N)
E1 = Entry(fenetre, bd =3,)
E1.pack(side = LEFT)
E1.place( relx=0.5, rely=0.25,anchor=N)


#2e liste

def Combo_pays_onselect(evt):
    valeur = Combo_pays2.get()
    index = Combo_pays2.current()
    print("index: " + str(index) + "valeur: " + valeur )


Combo_pays2 = ttk.Combobox(fenetre)

Combo_pays2["values"] = ("EUR->Europe","USD->USA","JPY->Japon","GBP->angleterre","CHF-> Suisse","INR->Inde","RUB->Russe","CNY->Chine","MXN->Mexique","AUD->Australie","CAD->Canada","ZAR->Afrique du sud",)
Combo_pays2["state"] = "readonly"
Combo_pays2.pack()
Combo_pays2.place( relx=0.5, rely=0.412,anchor=N)


L1 = Label(fenetre,font=("Arial",10),text="Résultats ->")
L1.pack( side = LEFT)
L1.place(  relx=0.22, rely=0.50,anchor=N)
E1 = Entry(fenetre, bd =3)
E1.pack(side = LEFT)
E1.place( relx=0.5, rely=0.50,anchor=N)



#ajout des image

#gestion de l'evenement combobox

#premiere liste
Combo_pays.bind("<<ComboboxSelected>>", Combo_pays_onselect)

#2e liste
Combo_pays2.bind("<<ComboboxSelected>>", Combo_pays_onselect)


fenetre.mainloop()
