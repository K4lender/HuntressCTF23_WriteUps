import base64

def pears(beets):
    return chr(int(beets) - 17)

def strawberries(grapes):
    return grapes[:3]

def almonds(jelly):
    return jelly[3:]

def nuts(milk):
    oat_milk = ""
    while len(milk) > 0:
        oat_milk += pears(strawberries(milk))
        milk = almonds(milk)
    return oat_milk

def bears(cows):
    return cows[::-1]

def tragedy():
    apples = "129128136118131132121118125125049062118127116049091088107132106104116074090126107132106104117072095123095124106067094069094126094139094085086070095139116067096088106065107085098066096088099121094101091126095123086069106126095074090120078078"
    water = nuts(apples)

tragedy()
