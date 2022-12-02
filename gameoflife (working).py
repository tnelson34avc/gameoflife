
"""
Created on Mon Oct 10 18:19:36

@author: tyler nelson
"""

import numpy as np
import random as ran
showdata = 0
loops = 0

dead = 0
alive = 1


size = 10#chnage to 20
maxe = size+1

GB = np.zeros((size,size)) #tuple array

def startmap():
    global GB
    if showdata==True: print("startbored active")
    for i in range(size-1):
        for j in range(size-1):
            r = ran.uniform(0, 1)
            if r<.5:
                GB[i,j]=1
startmap()##########################################################
                            #(i,j,GB,status):
def live_neighbors(i,j,status): #add the status perameter so that it can know which rules to use
    global GB
    if showdata==True:print("liveneighbors active")
    #neighborhood = GB[i-1:i+1,j-1:j+1]
    #print(GB[i-1:i+1,j-1:j+1])
    numberofneighbors = len(getneigbors(i, j,GB)) #count = np.count_nonzero(neighborhood==1)
    
    tempneighbors = getneigbors(i, j, GB)
    
    count = checkneighbors(tempneighbors, status)
    
    if liveordie(count,status)==0:
        GB[i,j]=0#tempGB[i,j]=0
    elif liveordie(count,status)==1:
        GB[i,j]=1#tempGB[i,j]=1
        

def getneigbors(i,j,GB):
    
    #corners = [[0,0],[0,maxe-1],[maxe-1,0],[maxe-1,maxe-1]]
    if showdata==True:print(i,j)
    neighbors = (())
    
    if  (i>0) and i<(maxe-1):
        if j> 0 and j<maxe-1:#(i>0 and i<maxe-1 and j> 0 and j<maxe-1):
            if showdata==True:print("n")#print("not on edge")
            ##              UR        UM       UL        BL       BM      MR      ML      BR
            neighbors = [GB[i+1,j+1],GB[i,j+1],GB[i-1,j+1],GB[i-1,j-1],GB[i,j-1],GB[i+1,j],GB[i-1,j],GB[i+1,j-1]]
            
    elif  (i==0 and j==0):
        print("UL corner")
        ##             BM      MR     BR
        neighbors = [GB[i,j-1],GB[i+1,j],GB[i+1,j-1]]
        
    elif (i==0 and j==maxe-1):
        print("BL corner")
        ##              UR        UM      MR  
        neighbors = [GB[i+1,j+1],GB[i,j+1],GB[i+1,j]]
        
    elif (i==maxe-1 and j==0):
        print("UR corner")
        ##               BL       BM      ML  
        neighbors = GB[[i-1,j-1],[i,j-1],[i-1,j]]
    
    elif (i==maxe-1 and j==maxe-1):
        print("BR corner")
        ##              UM       UL       ML   
        neighbors = GB[[i,j+1],[i-1,j+1],[i-1,j]]
        
    elif (i==0 ) and (j> 0 and j<maxe-1):
        print("left edge")
        ##              UR        UM      BM      MR     BR
        neighbors = [GB[i+1,j+1],GB[i,j+1],GB[i,j-1],GB[i+1,j],GB[i+1,j-1]]
        
    elif (i==maxe-1) and (j> 0 and j<maxe-1):
        print("right edge")
        ##             UM       UL        BL       BM     ML    
        neighbors = [GB[i,j+1],GB[i-1,j+1],GB[i-1,j-1],GB[i,j-1],GB[i-1,j]]
        
    elif (i>0 or i<maxe-1) and (j==maxe-1):
        print("bottom edge")\
        ##              UR        UM       UL       MR      ML    
        neighbors = GB[[i+1,j+1],[i,j+1],[i-1,j+1],[i+1,j],[i-1,j]]
        
    elif (i>0 or i<maxe-1) and (j==0):
        print("top edge")
        ##               BL       BM      MR      ML      BR
        neighbors = GB[[i-1,j-1],[i,j-1],[i+1,j],[i-1,j],[i+1,j-1]]
    
        
    return neighbors
        
def checkneighbors(neighbors,status):
    match =0
        #finds out how many of the neigbors have that status
    for x in range(len(neighbors)):
        if neighbors[x]==status: 
            match
        
    return match
        

def liveordie(count,status): #rules depend on wether its alive or dead so check and add that 
    if showdata==True:print("liveordie active")
    '''
    Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by overpopulation.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    Any live cell with two or three live neighbors survives.
    Any dead cell with three live neighbors becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    '''
    if status is alive:
        if count < 2:
            return 0
        if count == 3 or count == 2:
            return 1
        if count > 3:
            return 0
        
    if status is dead:
        if count < 3:#count == 3:
            return 1

print(GB)############################################################
tempGB =GB

def ghosttown(GB):# check if the entire board is dead
    if showdata==True:print("ghosttownactive")
    peeps = 0
    for i in range(1,size-1):
        for j in range (1,size-1):
            if GB[i][j]==alive:
                peeps+=1
    if peeps > 1:
        return 1
    else:
        return 0;
    
def rungame():
    global GB
    global tempGB
    if showdata==True:print("rungameactive")
    #while ghosttown(GB)==1:
    for i in range(0,size-1):
        for j in range (0,size-1):
            live_neighbors(i,j,GB[i,j])#live_neighbors(i,j,GB,GB[i,j])
    print("printing new board")
    tempGB = GB
    #print(GB)
    printboard(GB)

def printboard(GB):
    if showdata==True:print("printboard is active")
    for i in range(1,size-1):
        #print("\n")
        for j in range (1,size-1):
            # if GB[i][j]==alive:
            #     print("X")
            # else:
            #     print(" ")
            #print('#' if GB[i,j] ==alive else '_' ,end = ' ')
            """fuck"""
    print("")
# rungame()

while ghosttown(GB) != 0:
    print(loops)
    rungame()
    loops =0#1+loops
    print(loops)
    if loops > 10:
        break
    
    print(GB)

        
#add a fuction for those on the edge and corners since they have specific rules




