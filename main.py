import random 
import threading

# up to 256000 it can handle.
tableX = 100
tableY = 100

startRange = 4

table = []

def setup():
    for i in range(tableX):
        table.insert(i, ' ')
        
    for j in range(tableY):
        table.insert(j, ' ')
s = threading.Thread(target=setup())
s.start()
s.join()

def game():
    f = random.randint(0, tableX + tableY)
    table[f] = 'O'
    global att 
    att = False

        
    print('Attempting to go to the target.')
    att = True 
    randomizedIndex = 0
    fakeTarget = 0 

    def randomize():
        global randomizedIndex
        global att 
        global fakeTarget 
         
        fakeT = table.copy()
        for i in fakeT:
            if i == 'O':
                fakeTarget = fakeT.index(i)

        try:
            while att == True:
                try:
                    r = random.randint(0, tableX + tableY)
                    
                    fakeT[r] = 'X'

                    for i in fakeT:
                        if i == 'X':
                            randomizedIndex = fakeT.index(i)
                except IndexError as err:
                    print(err)

                if randomizedIndex - fakeTarget < 2 and randomizedIndex - fakeTarget > -2:
                    if randomizedIndex == fakeTarget:
                        print(f'Same place!')
                        randomize()
                        break
                    print(f'Found a close path! {randomizedIndex - fakeTarget}')
                    print(fakeT)

                    att = False
                    break 
                else:
                    print(f'Is not a close path! Re-trying')
                    randomize()
                break
        except:
            print('error')
            randomize()
    d = threading.Thread(target=randomize(), daemon= True)
    d.start()
    
    #print(f'Real Table:\n{table}\n')


setup()

g = threading.Thread(target=game(), daemon= True)
g.start()
