

def canMakeSandwich(hasPeanutButter, hasJelly, slicesOfBread):
    if (hasPeanutButter == False):
        print "you can't make any sandwiches - no peanut butter"
    else:
        if (slicesOfBread >= 2):
            # have peanut butter and enough bread
            numSandwiches = slicesOfBread/2
            if (hasJelly):
                print "you can make {0} PB & J sandwiches".format(numSandwiches)
            else:
                print "you can make {0} peanut butter sandwiches without jelly".format(numSandwiches)
        elif (slicesOfBread == 1):
            if (hasJelly):
                print "you can make half a PB & J sandwich"
            else:
                print "you can make half a peanut butter sandwiche without jelly"        
        else:
            print "you can't make any sandwiches - no bread"



slicesOfBread = 5
hasPeanutButter = True
hasJelly = False
canMakeSandwich(slicesOfBread, hasPeanutButter, hasJelly)

