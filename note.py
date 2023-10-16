#Programme permete de saisir trois notes (sur 20) d'un étudiant apres le programme calcule la moyenne et affiche cette moyenne avec la mention
n1=float(input("Entrer votre 1er note : "))
n2=float(input("Entrer votre 2eme note : "))
n3=float(input("Entrer votre 3eme note : "))
m=float
m=(n1+n2+n3)/3

if(m>=16):
     print("moyene est : ",m)
     print("Tres bien")
elif(m>=14 and m<16):
     print("moyene est : ",m)
     print("Bien")
elif(m<14 and m>=12):
     print("moyene est : ",m)
     print("Assez bien")
elif(m<12 and m>=10):
     print("moyene est : ",m)
     print("Passable")
else:
    print("Vous n'etes pas admis")

