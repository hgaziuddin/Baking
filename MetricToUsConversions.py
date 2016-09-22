def milli_to_teaspoon(milli):
    milli = float(milli)
    teas = milli / 5
    teas = str(teas)
    milli = str(milli)
    print(milli + " milliliter(s) equals " + teas + " teaspoon(s)")


def teaspoon_to_milli(teas):
    teas = int(teas)
    milli = teas * 5
    milli = str(milli)
    teas = str(teas)
    print(teas + " teaspoon(s) equals " + milli + " milliliter(s)")


print("Do you want to calculate from Milliliters to Teaspoons or vice versa?/n")
print("Type: 'tsp to ml' or 'ml to tsp'")
nextinput = raw_input()


if nextinput == "tsp to ml":
    print("Please enter the amount of Teaspoons you want to convert into Milliliters")
    nextTspInt = raw_input()
    teaspoon_to_milli(nextTspInt)

if nextinput == "ml to tsp":
    print("Please enter the amount of Milliliters you want to convert into Teaspoons")
    nextMlInt = raw_input()
    milli_to_teaspoon(nextMlInt)
