def getThreeNumbers():
    bread = raw_input("How much bread do you have: ")
    peanut_butter = raw_input("How many scoops of peanut_butter do you have: ")
    jelly = raw_input("How many scoops of jelly do you have")
    return int(bread), int(peanut_butter), int(jelly)

print "So you have %s slices of bread, %s scoops of peanut butter and %s scoops of jelly" % (
		bread, peanut_butter, jelly)