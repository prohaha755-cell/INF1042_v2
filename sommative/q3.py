
montant = float(input("Entrez le montant : "))

if montant < 50:
    rabais = 0
elif montant <= 100:
    rabais = 5
else:
    rabais = 10

economie = montant * rabais / 100
sous_total = montant - economie
taxe = sous_total * 0.13
total = sous_total + taxe

print("Rabais :", rabais, "%")
print("Economie :", economie)
print("Taxe :", taxe)
print("Total :", total)

