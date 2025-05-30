vitesse_iss=7.77777777
vitesse_iss="{:.4f}".format(vitesse_iss) 
#transforme le float en str et laisse 4 chiffre après la virgule

with open("result.txt","w") as fichier:#créer un fichier txt pour pouvoir le modifier
    fichier.write(vitesse_iss)# met la vitesse dans ce fichier
