#groeten

from tokenize import Name


print('Goedemiddag, bedankt voor uw aanmelding, wij willen graag een paar vragen stellen om te weten of u geschikt bent door deze baan.')
geschikt = True

#naam

# if int(lengte) > 150 and int(gewicht) > 90:
#      print('U bent geschikt voor deze baan, neem graag contact met ons op via onze email!')
# else:
#     geschikt = False
#     print('U bent helaas niet geschikt voor deze baan, we wensen u nog een fijne dag!')


    

naam = input ('Wat is uw naam?  :')
if naam == "Jan":
    raise NameError("Jan is niet welkom bij deze zaak")
kleur = input('Wat is uw favoriete kleur on de 10, graag in weekdagen antwoorden?  : ')
if kleur == "Blauw":
    raise NameError("Blauw is lelijk")
ass = input('Bent u een sussy baka?  :')
if ass == "nee":
    raise NameError("Ew geen sussy baka niet welkom")
stoel = input('Wat is uw favoriete stoel?  : ')
if stoel == "gamer chair":
    raise NameError("Stop.")

#lengte
lengte = input('Wat is uw lengte in cm?  : ')
# if int(lengte) < 150:
#     print('U bent niet lang genoeg voor de baan.')
#     geschikt = False
# if int(lengte) > 150:
#     print('U bent lang genoeg voor de baan.')
 
# #gewicht

gewicht = input('Wat is uw gewicht in hele kg?  : ')
# if int(gewicht) > 90:
#     print('U bent zwaar genoeg voor de baan.')
# if int(gewicht) < 90:
#     print('U bent niet zwaar genoeg voor de baan.')
#     geschikt = False 



#ervaringen

ervaring = input('Waar heeft u ervaring in  Dierendressuur/Jongleren/Acrobatiek?  :')
jaar = input('Hoeveel jaar hoeft u hier ervaring in?  : ')
if (ervaring == 'Dierendressuur' and int(jaar) < 4) or (ervaring == 'Jongleren' and int(jaar) < 5) or (ervaring =='Acrobatiek' and int(jaar) < 3):
    print('U bent niet geschikt voor de baan.')
    geschikt = False 
else: 
    print('U bent geschikt voor deze baan.')

#diploma en rijbewijs 

diploma = input('Heeft u een MBO-4 ondernemen diploma?  J/N  :')
rijbewijs = input('Heeft u een geldig vrachtwagen rijbewijs?  J/N  :')
hoed = input('Bent u eigenaar van een hoge hoed?  J/N  : ')

#man of vrouw eisen

geslacht = input('Bent u een man of vrouw?  :')
if geslacht == 'man':
    snor = input('Hoe breed is uw snor in cm?  :')
else:
    haar = input('Hoe lang is uw rood krulhaar?  :')

#certicicaat

certificaat = input('Heeft u een certificaat voor "Overleven met gevaarlijk personeel"  : ')
# if geschikt == True:
#     print('U bent geschikt voor deze baan, neem graag contact met ons op via onze email!')
# else:
#     print('U bent helaas niet geschikt voor deze baan, we wensen u nog een fijne dag!')


if int(lengte) > 150 and int(gewicht) > 90 and diploma = "J" and rijbewijs = "J" and hoed = "J":
     print('U bent geschikt voor deze baan, neem graag contact met ons op via onze email!')
else:
    geschikt = False
    print('U bent helaas niet geschikt voor deze baan, we wensen u nog een fijne dag!')