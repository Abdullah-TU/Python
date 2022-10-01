Blood pressure calculations:

import sys


def pressure(par):
    while True:
        print('Enter {} pressure (or "quit" to stop):'.format(par), end=' ')
        pressure = input()
        if pressure == 'quit':
            print('Quit-command received. Stopping the program.')
            sys.exit()
        else:
            try:
                if int(pressure) > 0:
                    return pressure
                else:
                    print('Enter a positive integer!')

                    continue
            except ValueError or int(systolic) <= 0:
                print('Enter a positive integer!')
                continue

def condition(systolic, diastolic):
    if 180 < systolic or 120 < diastolic:
        print('Hypertensive crisis (consult your doctor immediately)')
    elif (140 <= systolic and systolic <= 180) or (90 <= diastolic and diastolic <= 120):
        print('High (hypertension) stage 2')
    elif (130 <= systolic and systolic <= 139) or (80 <= diastolic and diastolic <= 89):
        print('High (hypertension) stage 1')
    elif (120 <= systolic and systolic <= 129) and (60 <= diastolic and diastolic < 80):
        print('Elevated')
    elif (90 <= systolic and systolic < 120) and (60 <= diastolic and diastolic < 80):
        print('Normal')
    elif systolic < 90 or diastolic < 60:
        print('Low')


while True:
    sysVal = int(pressure('systolic'))
    diaVal = int(pressure('diastolic'))
    condition(sysVal, diaVal)
