nombre_initial = int (input ("Veuillez entrez l'entier à traiter : "))

if nombre_initial != int :
    print ("Cette valeur n'est pas traitée par le programme, nous nous excusons pour la gêne occasionée.")
    

base_initiale = int (input ("Veuillez entrer la base du nombre (Les seules bases traitées sont 2, 10 et 16) : "))
base_finale = int (input ("Veuillez entrer la base souhaitée (Les seules bases traitées sont 2,10 et 16)  : "))



if base_initiale != 2 and base_initale != 10 and base_initiale != 16 :
    print  ("La base du nombre que vous avez entrée n'est pas traitée par ce programme ")



def base_10_2 (nombre_initial, base_initiale) :
    while r != 0 and q != 0 :
        nombre_initial = divmod (nombre_initial, 2)
        append (r)
    
        
        
                        
        
    





print ("Le nombre "\
       + str (nombre_initial)\
       + " en base "\
       + str (base_initiale)\
       + " vaut "\
       + str (nombre_final)\
       + " en base "\
       + str (base_finale)\
       + ".")
