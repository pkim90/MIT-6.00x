#Problem Set 2
#Name: Peter Kim
#Collaborators: ???
#Time:

#problem 3
# Write an iterative program that finds the largest number of McNuggets
# that cannot be bought in exact quantity. Your program should print the
# answer in the following format (where the correct number is provided in
# place of <n>):

#The following was in the lecture. It seems really close:

def solve1(numLegs, numHeads):
    for numSpiders in range(0, numHeads + 1):
        print ('numspiders is', numSpiders)
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs = 4 * numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                return (numPigs, numChicks, numSpiders)
    return (None, None, None)


def solve(numNuggets, maxSet):
    for twentyPack in range(0, maxSet + 1):
        print ('twentypack is') + str(twentypack)
        for sixPack in range(0, maxSet - twentyPack + 1):
            ninePack = maxSet - sixPack - twentyPack
            totNuggets = 9*ninePack + 6*sixPack + 20*twentyPack
            print (totNuggets)
            if totNuggets == numNuggets:
                return (ninePack, sixPack, twentyPack)
    return (None, None, None)

# After trying for about an hour I've decided to leave it for now and come back
# to it at a later time.
