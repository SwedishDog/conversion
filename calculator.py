##Total Car count minus ARM washes = Drive Up Washes
##Divide plans sold by Drive Up Washes * 100 for Conversion Rate

#carCount = input("What was the carcount for the day? ")
#ARMWashes = input("How many of those cars were members? ")
#plansSold = input("How many plans did we sell today? ")

def ConversionRate(carCount,ARMWashes,plansSold):
    carCount = int(carCount)
    ARMWashes = int(ARMWashes)
    plansSold = int(plansSold)
    rate = (plansSold/(carCount-ARMWashes))
    #print("The Conversion Rate is {:.2%}".format(rate))
    return (rate * 100)

#ConversionRate(carCount,ARMWashes,plansSold)
