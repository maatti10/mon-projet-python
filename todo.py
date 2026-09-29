
# Mon gestionnaire de tâches complet
import json


def charger_taches() : 

    try: 
        with open("taches.json", "r" , encoding="utf-8") as f:
            contenu = json.load(f)
            return contenu if contenu is not None else []
    except (FileNotFoundError, json.JSONDecodeError):
        return [
            {"titre": "Apprendre Python", "fait": False},
            {"titre": "Découvrir Github", "fait": False}
        ]


#================== sauvegarder tâches #==============
def sauvegarder_taches(liste):
    with open("taches.json", "w" , encoding="utf-8") as f:
        return json.dump(liste, f)


#================== Affiche les tâches #==============
def afficher_taches(liste): 
    print("\n=== Mon gestionnaire de tâches ===")
    if not liste:
        print("Aucune tache pour le moment")
    else:
        for i, tache in enumerate(liste, 1):
            statut = "[X]" if tache["fait"] else "[ ]"
            
            print(f"{i}. {statut} {tache['titre']}")


#================== ajoute  tâches #==============
def ajouter_tache(liste) : 
    nouvelle = input("Nouvelle tâche : ").strip()
    
    if  nouvelle : 
            liste.append({"titre" : nouvelle, "fait": False})
            print("-> Tâche ajoutée !")
            sauvegarder_taches(liste)
    else :
        print("Texte vide, aucune tâche ajoutée.")    



#================== modifier les tâches #==============

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
                liste[num - 1]["titre"] = nouveau_texte
                print("-> Tâche modifiée !")
                sauvegarder_taches(liste)
            else:
                print("Texte vide, modification annulée.")
        else:
            print("Numéro hors limites.")
    else:
        print("Entrée invalide, saisis un nombre entier.")



#================== supprimer tâche ==================
def supprimer_tache(liste):
    if not liste:
        print("Aucune tâche à supprimer.")
        return

    saisie = input("Numéro de la tâche à supprimer : ").strip()
    if saisie.isdigit():
        num = int(saisie)
        if 1 <= num <= len(liste):
            supprimee = liste.pop(num - 1)
            print(f"-> Tâche '{supprimee['titre']}' supprimée !")
            sauvegarder_taches(liste)
        else:
            print("Numéro hors limites.")
    else:
        print("Entrée invalide, saisis un nombre entier.")



#================== supprimer toutes les tâches #==============
def supprimer_toutes_taches(liste):
    if not liste:
            print("il n'y a rien à supprimer.")
            return
    confirmation = input("Es-tu sûr de vouloir TOUT supprimer ? (o/n) : ").strip().lower() 
    if confirmation == "o" :
                liste.clear()
                print("Toutes les taches sont supprimées")
                sauvegarder_taches(liste)
    else :
            print("Action annulée")



#================== terminer tâche #==============

def terminer_tache(liste):
    if not liste:
        print("Aucune tâche à marquer.")
        return

    saisie = input("Numéro de la tâche à cocher/décocher : ").strip()
    if saisie.isdigit():
        num = int(saisie)
        if 1 <= num <= len(liste):
            index = num - 1
            liste[index]["fait"] = not liste[index]["fait"]
            etat = "terminée" if liste[index]["fait"] else "non terminée"
            print(f"-> Tâche marquée comme {etat} !")
            sauvegarder_taches(liste)
        else:
            print("Numéro hors limites.")
    else:
        print("Entrée invalide, saisis un nombre entier.")                  


 

#================== afficher_taches en cours =====================
def afficher_taches_en_cours(liste) :
    if not liste:
        print("aucune tache !!!")
        return

    for i, tache in enumerate(liste, 1) :
         
         if not tache["fait"]  :
            print(f"{i}.[ ] {tache['titre']}") 
        


taches = charger_taches()


while True :

    afficher_taches(taches)

    print("\nQue veux-tu faire ?")
    print("1. Ajouter une tâche")
    print("2. Modifier une tâche")
    print("3. Terminer une tâche")
    print("4. Supprimer tache")
    print("5. Supprimer toutes tâches")
    print("6. Afficher les taches non faites")
    print("7. Sauvegarder les taches")

    choix = input("Entre ton choix (1-7) : ")

    if choix == "1":
        ajouter_tache(taches)

    elif choix == "2":
        modifier_tache(taches)
        

    elif choix == "3":
        terminer_tache(taches)


    elif choix == "4":
        supprimer_tache(taches)
        
    
    elif choix == "5":
        supprimer_toutes_taches(taches)
        print("-> Tâches supprimées !")

    elif choix == "6" :
        afficher_taches_en_cours(taches)
        print("-> Tâches non faites !")


    elif choix == "7" :
        
        print("Au revoir !")

        break


    else:
        print("Option non reconnue, réessaie.")
