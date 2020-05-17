
''' >>  Elite Dangerous' Hyperspace Fuel Equation << 

The effective fuel consumption of a ship travelling
in hyperspace  can be calculated.

The formula is experimental

Found at: 
            https://elite-dangerous.fandom.com/wiki/Frame_Shift_Drive


----------------- [FSD = Frame Shift Drive] ---------------------

f = fuel consumption per jumps in tons

l = linear constant: Depends upon the rating of the FSD
    (Rating             A   |   B   |   C   |   D   |   E   )
    (Linear Constant    12  |   10  |   8   |   10  |   11  )

d = jump distance in light years

mShip = the mass of the entire ship including
    its cargo in tons and before fuel is consumed
    in hyperspace jump itself

mOpt = optimal mass of the FSD in tons as indicated 
    by the outfitters. The total mass of the ship
                         can exceed this value

p = power constant. This constant depends on 
                    the class of the FSD

    (Class                2   |   3   |   4   |   5   |   6   )
    (Power Constant      2.00 |  2.15 |  2.30 |  2.45 |  2.60 )


FORMULA 

    f = l * 0.001 * ( ( d * mShip )**p / (mOpt) )

'''

import math as mt
import time as tm
import sys

def main():

    print('Place Holder')

    l, d, mShip, p, mOpt = inputVariables()

    HyperSpaceEquation(l, d, mShip, mOpt, p)

    f = HyperSpaceEquation(l, d, mShip, mOpt, p)
    tm.sleep(.1)
    # Hyperspace Fuel Consumption
    hFC(f)

def inputVariables():

    print('''\n\tConstant depends upon the rating of the FSD;
    (Rating             A   |   B   |   C   |   D   |   E   )
    (Linear Constant    12  |   10  |   8   |   10  |   11  )''')
    l = float(input('\tLinear Constant  : '))

    d = float(input('\tJump Distance LYRS   : '))

    mShip = float(input('\tShip Total Mass  : '))

    print('''\n\tConstant depends on the class of the FSD;
    (Class                2   |   3   |   4   |   5   |   6   )
    (Power Constant      2.00 |  2.15 |  2.30 |  2.45 |  2.60 )''')
    p = float(input('\tPower Constant   : '))

    mOpt = float(input('\tFSD Optimal Mass  : '))


    return l , d , mShip , p , mOpt


def HyperSpaceEquation(l,d, mShip, mOpt, p):

    f = l * 0.001 * ( ( d * mShip )**p / (mOpt) )

    return f


def hFC(f):

    print('\n\tHyperspace Effective Fuel Consumption: ', format(f ,'7.2f'))


    tm.sleep(1)
    print('\n\tAdditional Jumps?  ')
    tm.sleep(.3)
    nextJump = input('\t < y / N > ')
    if nextJump == 'y' or nextJump == 'Y' or nextJump =='Yes':
        main()
    else:
        sys.exit()

main()