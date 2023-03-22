import string
import hashlib 
import json

# Comparaison de mot de passe

with open("password.json", "r") as f:
 
    mot_de_passe = f.readlines()

nouveau_mot_de_passe = input("Nouveau mot de passe : ")

if nouveau_mot_de_passe + "\n" in mot_de_passe:
    print("Ce mot de passe est déjà enregistré.")
else:
  
    with open("password.json", "a") as f:
        f.write(nouveau_mot_de_passe + "\n")
    print("Le nouveau mot de passe a déjà été enregistré.")

# Json

def fichier (mot_de_passe, code):
    f = open('password.json', "r+")
    database = json.load(f)
    database[mot_de_passe] = code
    f.seek(0)
    json.dump(database, f, indent=4)
    f.close()

# Hashlib

def crypto(mdp):
    code = mdp.encode()
    code_haslib = hashlib.sha256(code).hexdigest()
    print(code_haslib)
    return code_haslib


def password():

    # les chaines de caractere a utiliser

    minuscule= list(string.ascii_lowercase)
    majuscule =  list(string.ascii_uppercase)
    nombre = list(string.digits)
    caractere_speciaux = list(string.punctuation)
    
    #  remettre le compteur des  chaines de caaractere

    nbr_min = 0
    nbr_maj = 0
    nbr_num = 0
    nbr_spec = 0 

    while True :

        mot_de_passe = input("Configurez votre mot de passe : ")
        
    # Vérification de mot de passe 

        for i in mot_de_passe:
            if i in minuscule:
                nbr_min +=1
            if i in majuscule:
                nbr_maj+=1
            if i in nombre:
                nbr_num +=1
            if i in caractere_speciaux:
                nbr_spec +=1

        #  mot de passe correct ou incorrect

        if len(mot_de_passe) < 8 or nbr_min == 0 or nbr_maj == 0 or nbr_num == 0 or nbr_spec == 0:

            print('Password pas assez sécurisé')

        else:

            print('Password enregistré avec succès')

            code = crypto(mot_de_passe)
            
            fichier(mot_de_passe, code)

            break
password()