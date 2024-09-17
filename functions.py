
etudiants = []
def menu():
    while True:
        print("\nMenu:")
        print("1. Ajouter un étudiant")
        print("2. Afficher tous les étudiants")
        print("3. Trier et afficher par ordre décroissant de la moyenne")
        print("4. Rechercher un étudiant")
        print("5. Modifier les notes d'un étudiant")
        print("6. Sortir")

        choix = input("Choisissez une option: ")

        if choix == "1":
            demander_infos()
        elif choix == "2":
            if not etudiants:
                print("\n Aucun étudiant n'a été enregistré")
            else:
                lister_etudiants(etudiants)
        elif choix == "3":
            trier_par_moyenne(etudiants)
        elif choix == "4":
            rechercher_etudiant()
        elif choix == "5":
            modifier_notes()
            lister_etudiants(etudiants)
        elif choix == "6":
            print("Merci d'avoir utilisé l'application.")
            break
        else:
            print("Option invalide, veuillez réessayer.")


def demander_infos():
    telephone = input("Entrez le numéro de téléphone de l'étudiant: ")
    while not valider_telephone(telephone):
        telephone = input("Numéro de téléphone invalide ou déjà utilisé. Veuillez réessayer: ")
    
    prenom = input("Entrez le prénom de l'étudiant: ")
    nom = input("Entrez le nom de l'étudiant: ")
    classe = input("Entrez la classe de l'étudiant: ")
    
    note_devoir = note_valide('devoir')
    note_projet = note_valide('projet')
    note_examen = note_valide('examen')
    
    moyenne = round((note_devoir + note_projet + note_examen) / 3, 2)

    etudiant = {
        "telephone": telephone,
        "prenom": prenom,
        "nom": nom,
        "classe": classe,
        "note_devoir": note_devoir,
        "note_projet": note_projet,
        "note_examen": note_examen,
        "moyenne": moyenne
    }
    etudiants.append(etudiant)
    print(f"L'étudiant {prenom} {nom} a été ajouté avec succès.\n")
    lister_etudiants(etudiants)


def trier_par_moyenne(etudiants):
    etudiants_tries = sorted(etudiants, key=lambda x: x['moyenne'], reverse=True)
    print("Étudiants triés par moyenne décroissante :")
    lister_etudiants(etudiants_tries)
    

def rechercher_etudiant():
    telephone_etudiant = input("Entrez le telephone de l'étudiant que vous cherchez : ")
    for etudiant in etudiants:
        if etudiant['telephone'] == telephone_etudiant:
            show_etudiant(etudiant)
        else:
            print("\n Aucun étudiant trouvé avec ce nom.\n")


def modifier_notes():
    telephone = input("Le telephone de l'étudiant : ")
    for etudiant in etudiants:
        
        if etudiant['telephone'] == telephone:
            
            etudiant['note_devoir'] = note_valide('devoir')
            etudiant['note_projet'] = note_valide('projet')
            etudiant['note_examen'] = note_valide('examen')
            
            etudiant['moyenne'] = (etudiant['note_devoir'] + etudiant['note_projet'] + etudiant['note_examen']) / 3
            return etudiant
    return None
     
    

def valider_telephone(telephone):
    if telephone.isdigit() and telephone.startswith(('70','75', '76', '77', '78')) and len(telephone) == 9:
        for etudiant in etudiants:
            if etudiant['telephone'] == telephone:
                return False
        return True
    return False

    
def note_valide(type_note):
    while True:
        try:
            note = float(input(f"Entrez la note de {type_note} (entre 0 et 20): "))
            if 0 <= note <= 20:
                return round(note, 2)
            else:
                print("La note doit être comprise entre 0 et 20.")
        except ValueError :
            print("Veuillez entrer un nombre valide.")

# Cette fonction permet d'afficher tous les étudiants
def lister_etudiants(etudiants):
    print("-" * 117)
    print(f" | {'Prénom':<15} | {'Nom':<10} | {'Téléphone':<15} | {'Classe':<10} | {'Devoir':<10} | {'Projet':<10} | {'Examen':<10} | {'Moyenne':<10} |")
    print("-" * 117)

    for etudiant in etudiants:
        print(f" | {etudiant['prenom']:<15} | {etudiant['nom']:<10} | {etudiant['telephone']:<15} | {etudiant['classe']:<10} "
              f"| {etudiant['note_devoir']:<10} | {etudiant['note_projet']:<10} | {etudiant['note_examen']:<10} | {etudiant['moyenne']:<10} | ")
        print("-" * 117)

# Cette fonction permet d'afficher l'etudiant recherché
def show_etudiant(etudiant):
    print("-" * 117)
    print(f" | {'Prénom':<15} | {'Nom':<10} | {'Téléphone':<15} | {'Classe':<10} | {'Devoir':<10} | {'Projet':<10} | {'Examen':<10} | {'Moyenne':<10} |")
    print("-" * 117)

    print(f" | {etudiant['prenom']:<15} | {etudiant['nom']:<10} | {etudiant['telephone']:<15} | {etudiant['classe']:<10} "
            f"| {etudiant['note_devoir']:<10} | {etudiant['note_projet']:<10} | {etudiant['note_examen']:<10} | {etudiant['moyenne']:<10} | ")
    print("-" * 117)
    
