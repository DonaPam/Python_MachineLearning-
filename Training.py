from operator import index
import numpy as np
# claseur
""" dictionnaire qui classe les nombres poistives et negatives """
classeur ={
    "positif": [],
    "negatif": []
}
def trier(classeur,nombre):

    if nombre < 0:
        classeur["negatif"].append(nombre)
    elif nombre > 0:
        classeur["positif"].append(nombre)
    return classeur
for i in range(5):
    n = int(input("Ton nombre:"))
    trier(classeur,n)

print(classeur)
print(classeur.values())
