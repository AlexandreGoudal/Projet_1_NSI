# -*- coding: cp1252 -*-
nombre_initial = int (input ("Veuillez entrez l'entier à traiter : "))

if type (nombre_initial) != int :
    print ("Cette valeur n'est pas traitée par le programme, nous nous excusons pour la gêne occasionée.")
    exit ()

base_initiale = int (input ("Veuillez entrer la base du nombre (Les seules bases traitées sont 2, 10 et 16) : "))

if base_initiale != 2 and base_initiale != 10 and base_initiale != 16 :
    print  ("La base du nombre que vous avez entrée n'est pas traitée par ce programme ")
    exit()

base_finale = int (input ("Veuillez entrer la base souhaitée (Les seules bases traitées sont 2, 10 et 16)  : "))

if base_finale != 2 and base_initiale != 10 and base_initiale != 16 :
    print  ("La base du nombre que vous avez entrée n'est pas traitée par ce programme ")
    exit()

def conversion (nombre_initial, base_initiale, base_finale):
    if base_initiale == 10 and base_finale == 2:
        nombre_final = bin (nombre_initial)
        return nombre_final
    elif base_initiale == 10 and base_finale == 16:
        nombre_final = hex (nombre_initial)
        return nombre_final

def base (nombre_initial, base_initiale) :
    r = 1
    q = 1
    while r != 0 and q != 0 :
        nombre_final = []
        nombre_initial = divmod (nombre_initial, base_initiale)
        nombre_final.append (r)
    return nombre_final
    pass





print ("Le nombre "\
       + str (nombre_initial)\
       + " en base "\
       + str (base_initiale)\
       + " vaut "\
       + str (conversion (nombre_initial, base_initiale, base_finale))\
       + " en base "\
       + str (base_finale)\
       + ".")

