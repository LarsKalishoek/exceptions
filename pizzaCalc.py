#Lars Kalishoek pizzacalc

print("Typ in hoeveel pizza u van elke soort wilt \n --------------------")

def _calc(groote):
    while True:
        try:
            pizza = input(f" {groote} Pizza's: ")
            pizza = int(pizza)
            return pizza
        except ValueError as error:
            print("gebruik hele getallen")

#pizza sizes
small = _calc("Kleine")
medium = _calc("Medium")
large = _calc("Grote")

#prijs berekenen
prijs1 = int(small) * 6
prijs2 = int(medium) * 12
prijs3 = int(large) * 16

prijs = prijs1 + prijs2 + prijs3

#eindzin

factuurtekst = 'U heeft ' + str(small) + ' small pizzas ' + str(medium) + ' medium pizzas ' + str(large) + ' large pizzas het totale bedrag dat u moet betalen is : $' + str(prijs)
print (factuurtekst)