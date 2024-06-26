
def match(goalState , startStae):
    h = 0 
    for i in range(len(startStae)):
        print ("first :" , i)
        for j in range(len(startStae[0])):
            print ("second :" , j)
            if startStae[i][j] != goalState[i][j]:
                h = h + 1
    return h

def moves(g , h , f, goalState, startState):

    state1,state2,state3,state4 = startState

    while True:
        if (goalState == startState):
            print("In Moves :  " , g)
            break
        else:
                g = g + 1

                possibility1 , state1 = upMove(goalState , startState )
                possibility2 , state2 = DownMove(goalState , startState )
                possibility3,state3 = leftMove(goalState , startState )
                possibility4 ,state4 = rightMove(goalState , startState )

                ans = min(possibility1 + g  ,possibility2 + g ,possibility3 + g ,possibility4 + g )
                if ans - g == possibility1:
                    moves (g , possibility1 , g + possibility1 , goalState , state1 )
                elif ans - g == possibility2:
                    moves (g , possibility2 , g + possibility2 , goalState , state2 )
                elif ans - g == possibility3:
                    moves (g , possibility3 , g + possibility3 , goalState , state3 ) 
                elif ans - g == possibility4:
                    moves (g , possibility4 , g + possibility4 , goalState , state4 )       

    return g




def upMove(   goalState,startState):
    h = 0 
    rLen = len(startState)
    cLen = len(startState[0])
    r,c = findEmptyPlace(startState)
    if r > 0:
        temp = startState[r - 1][c]
        startState[r - 1][c] = 0 
        startState[r][c] = temp


    h = match(goalState , startState)
    return h,startState


def DownMove(goalState,startState):
    h=0
    rLen = len(startState)
    cLen = len(startState[0])
    r,c = findEmptyPlace(startState)
    if r < rLen:
        temp = startState[r + 1][c]
        startState[r + 1][c] = 0 
        startState[r][c] = temp

    h = match(goalState , startState)
    return h,startState

def rightMove(goalState,startState):
    h=0
    rLen = len(startState) 
    cLen = len(startState[0]) 
    r,c = findEmptyPlace(startState)
    if c < cLen :
        temp = startState[r][c+1]
        startState[r][c+1] = 0 
        startState[r][c] = temp
    h = match(goalState , startState)
    return h ,startState

def leftMove(goalState,startState):
    h=0
    rLen = len(goalState)
    cLen = len(goalState[0])
    r,c = findEmptyPlace(startState)
    if c > 0:
        temp = startState[r][c-1]
        startState[r][c-1] = 0 
        startState[r][c] = temp
    h = match(goalState , startState)
    return h ,startState 

    

def findEmptyPlace(startState):
    for i in range(len(startState)):
        for j in range(len(startState[i])):
            if startState[i][j] ==  0:
                return i , j 
                break






goalState = [[1, 2, 3],[4, 5, 6], [7, 8, 0]]
startState = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]

print(moves(0,0,0,goalState, startState  ))





