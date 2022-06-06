
import filecmp


# fichier1 = "comparaison1.txt"
# fichier2 = "comparaison2.txt"

# resultat = filecmp.cmp(fichier1, fichier2)
# if resultat == True:
#     print("Les deux fichiers ont le même contenu")

# else:
#     print("Les deux fichiers ont un contenu différent")
#     print(len(fichier1))

import difflib
  
with open('comparaison/comparaison1.txt') as fichier1:
    texte_fichier1 = fichier1.readlines()
  
with open('comparaison/comparaison2.txt') as fichier2:
    texte_fichier2 = fichier2.readlines()
  

for ligne in difflib.unified_diff(
        texte_fichier1, texte_fichier2, fromfile='comparaison1.txt', 
        tofile='comparaison2.txt', lineterm=''):
    print(ligne)