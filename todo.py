
# Mon gestionnaire de tâches complet
import json


def charger_taches() : 

    try: 
        with open("taches.json", "r" , encoding="utf-8") as f:
            contenu = json.load(f)
            return contenu if contenu is not None else []
    except (FileNotFoundError, json.JSONDecodeError):
        return  ["Apprendre Python", "Découvrir Github"]


def sauvegarder_taches(liste):
    with open("taches.json", "w" , encoding="utf-8") as f:
        return json.dump(liste, f)



def afficher_taches(liste): 
    print("\n=== Mon gestionnaire de tâches ===")
    if not liste:
        print("Aucune tache pour le moment")
    else:
        for i, tache in enumerate(liste, 1):
            print(f"{i}. {tache}")



def ajouter_tache(liste) : 
    nouvelle = input("Nouvelle tâche : ").strip()
    
    if  nouvelle : 
            liste.append(nouvelle)
            print("-> Tâche ajoutée !")
    else :
        print("Texte vide, aucune tâche ajoutée.")    


def modifier_tache(liste):
    # 1. Sécurité : si la liste est vide ([]), inutile d'aller plus loin
    if not liste:
        print("Aucune tâche à modifier.")
        return  # On quitte immédiatement la fonction

    # 2. On récupère le choix de l'utilisateur sous forme de texte ("1", "2", etc.)
    saisie = input("Numéro de la tâche à modifier : ").strip()

    # 3. .isdigit() vérifie si ce texte contient uniquement des chiffres
    # Exemple : "2".isdigit() -> True | "abc".isdigit() -> False
    if saisie.isdigit():
        num = int(saisie)  # On convertit le texte en vrai nombre entier
        
        # 4. On vérifie que le numéro existe dans la liste (entre 1 et le nombre total de tâches)
        if 1 <= num <= len(liste):
            nouveau_texte = input("Nouveau texte : ").strip()
            
            # 5. On vérifie que le nouveau texte n'est pas vide
            if nouveau_texte:
                # - 1 car les listes Python commencent à l'index 0, pas à 1
                liste[num - 1] = nouveau_texte
                print("-> Tâche modifiée !")
            else:
                print("Texte vide, modification annulée.")
        else:
            print("Numéro hors limites.")
    else:
        print("Entrée invalide, saisis un nombre entier.")




def supprimer_tache(liste):
    if not liste:
        print("Aucune tâche à supprimer.")
        return 

    saisie = input("Numéro de la tâche à supprimer : ").strip()
    if saisie.isdigit():
        num = int(saisie)
        if 1 <= num <= len(liste):
            supprimee = liste.pop(num - 1)
            print(f"-> Tâche « {supprimee} » supprimée !")
        else:
            print("Numéro hors limites.")
    else:
        print("Entrée invalide, saisis un nombre entier.")




def supprimer_toutes_taches(liste):
    if not liste:
            print("il n'y a rien à supprimer.")
            return
    confirmation = input("Es-tu sûr de vouloir TOUT supprimer ? (o/n) : ").strip().lower() 
    if confirmation == "o" :
            taches.clear()
            print("Toutes les taches sont supprimées")
    else :
        print("Action annulée")
                    


 

    





taches = charger_taches()






while True :

    afficher_taches(taches)

    print("\nQue veux-tu faire ?")
    print("1. Ajouter une tâche")
    print("2. Modifier une tâche")
    print("3. Supprimer une tâche")
    print("4. Supprimer toutes tâches")
    print("5. Quitter")

    choix = input("Entre ton choix (1-5) : ")

    if choix == "1":
        ajouter_tache(taches)

    elif choix == "2":
        modifier_tache(taches)
        

    elif choix == "3":
        supprimer_tache(taches)


    elif choix == "4":
        supprimer_toutes_taches(taches)
        
    
    elif choix == "5":
        sauvegarder_taches(taches)
        print("-> Tâches sauvegardées. Au revoir !")
        break



    else:
        print("Option non reconnue, réessaie.")
