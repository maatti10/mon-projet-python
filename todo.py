
# Mon gestionnaire de tâches complet
import json

#================ demande d'index =====================
def demander_index(liste, message) :
        
        saisie = input(message).strip()
        if saisie.isdigit():
            num = int(saisie)
            if 1<= num <= len(liste) :
                return  num - 1
            else:
                print("numero hors limites")

        else:
            print("Entrée invalise saisis un nombre entier")

        return None
        



     



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
        return  
    
    index = demander_index(liste, "Numéro de la tâche à modifier : ")

    if index is not None :
         nouveau_texte = input("Nouveau texte : ").strip()
            
         if nouveau_texte:
                    liste[index]["titre"] = nouveau_texte
                    print("-> Tâche modifiée !")
                    sauvegarder_taches(liste)
         else:
                    print("Texte vide, modification annulée.")
        
    


#================== supprimer tâche ==================
def supprimer_tache(liste):
    if not liste:
        print("Aucune tâche à supprimer.")
        return

    index = demander_index(liste, "Numero de la tache a supprimer !")
    if index is not None:
        supprimee = liste.pop(index)
        print(f"-> Tâche '{supprimee['titre']} supprimée !")
        sauvegarder_taches(liste)


    



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

    index = demander_index(liste, "Numéro de la tâche à cocher/décocher : ")

    if index is not None:

            
            liste[index]["fait"] = not liste[index]["fait"]

            etat = "terminée" if liste[index]["fait"] else "non terminée"

            print(f"-> Tâche marquée comme {etat} !")
            sauvegarder_taches(liste)
         

        
    
                    


 

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
