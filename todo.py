
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


taches = charger_taches()






while True:
    print("\n=== Mon gestionnaire de tâches ===")
    if not taches:
        print("(Aucune tâche pour le moment)")
    else:
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")

    print("\nQue veux-tu faire ?")
    print("1. Ajouter une tâche")
    print("2. Modifier une tâche")
    print("3. Supprimer une tâche")
    print("4. Supprimer toutes tâches")
    print("5. Quitter")

    choix = input("Entre ton choix (1-5) : ")

    if choix == "1":
        nouvelle = input("Nouvelle tâche : ")
        taches.append(nouvelle)
        print("-> Tâche ajoutée !")

    elif choix == "2":
        num = int(input("Numéro de la tâche à modifier : "))
        if 1 <= num <= len(taches):
            nouveau_texte = input("Nouveau texte : ")
            taches[num - 1] = nouveau_texte
            print("-> Tâche modifiée !")
        else:
            print("Numéro invalide.")

    elif choix == "3":
        num = int(input("Numéro de la tâche à supprimer : "))
        if 1 <= num <= len(taches):
            supprimee = taches.pop(num - 1)
            print(f"-> Tâche '{supprimee}' supprimée !")
        else:
            print("Numéro invalide.")


    elif choix == "4":
        taches.clear()
        print("Toutes les taches sont supprimées")
    
    elif choix == "5":
        sauvegarder_taches(taches)
        print("-> Tâches sauvegardées. Au revoir !")
        break



    else:
        print("Option non reconnue, réessaie.")
