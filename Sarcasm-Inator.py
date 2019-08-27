import random, time
class values:
    z = []
    x = input('Enter the string: ')
    y = 0
    b = []


def userInput():
    values.x
    sarcasm()

def sarcasm():
    for i in values.x:
        values.y = random.randint(1,2)
        if values.y == 1:
            values.z.append(i.upper())
        else:
            values.z.append(i.lower())
    print(''.join(values.z))
    values.z = []
    end()

def end():
    print('Run Again?')
    x = input('Y/N: ')
    if x.upper() == 'Y':
        sarcasm()
    else:
        print('Goodbye!')

    
sarcasm()
