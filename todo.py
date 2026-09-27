
# Mon gestionnaire de taches
taches = ["Apprendre Python", "Découvrir Github"]

# 1. Demander une nouvelle tache a l'utilisateur
nouvelle_tache = input("Entre une tache a ajouter : ")
taches.append(nouvelle_tache)

#2. Afficher la liste mise a jour
print("\n=== Liste des taches ===")
for index, tache in enumerate(taches, 1):
    print(f"{index}. {tache}")
