
anner_en_jours = 365
chiffre = int(input("donne moi une date en jour:"))
jours = anner_en_jours - chiffre
heures = jours * 24
minutes = heures * 60
secondes = minutes * 60
print("il te reste")
print("Jours :", jours)
print("Heures :", heures)
print("Minutes :", minutes)
print("Secondes :", secondes)

