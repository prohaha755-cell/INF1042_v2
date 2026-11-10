import math
voiture=input("quel type de voiture as-tu. electric ou a gas:")
temps=float(input("combien de temps conte tu rester:"))
temps=math.ceil(temps)
if temps==1.0:
    prix=4
    prixtotal=prix
elif temps>1.0:
    prix=((temps-1.0)*2.5)+4
    prixtotal=prix
if voiture=="electric":
    print("20% de rabais")
    rabais=0.2*prix
    prixtotal=prix-(0.2*prix)
    print(prix,rabais)
print(prixtotal)