#The author's name is Julia Bub
class teaMug:
    """Represents a cup/mug of tea"""

myMug = teaMug()
myMug.capacity = 6
myMug.drank = 4
myMug.color = "purple"
#.capacity is the amount of tea the mug holds (in ounces)
#.drank is the amount of tea drank (in ounces)

def tea_drinking_simulation(t):
    tea_remaining = t.capacity - t.drank
    print(tea_remaining)
tea_drinking_simulation(myMug)
#this function should take the attributes, subtract them, and print 2 (the amount of tea remaining in the mug)
