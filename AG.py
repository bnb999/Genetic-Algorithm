from random import shuffle,randint
import numpy as np

#Matrice 1
matrice1 = [[0,1,1,3,4,5,6,1,7],
           [1,0,5,4,3,6,1,9,2],
           [1,5,0,1,6,1,9,3,7], 
           [3,4,1,0,5,9,7,2,1],
           [4,3,6,5,0,9,1,2,1],
           [5,6,1,9,9,0,2,1,7],
           [6,1,9,7,1,2,0,4,5],
           [1,9,3,2,2,1,4,0,7],
           [7,2,7,1,1,7,5,7,0]]



#Matrice 2
matrice2 = [
    [0, 6, 6, 1, 4],
    [6, 0, 8, 3, 5],
    [6, 8, 0, 6, 4],
    [1, 3, 6, 0, 2],
    [4, 5, 4, 2, 0]
]

def evaluation(m,ind):
        c = 0
        for i in range(len(ind)-1):
            c+= m[ind[i]-1][ind[i+1]-1]
        return c 


def Genetique(Matrice,N):

    def cr(Y,Z):
        f,s = Y.copy(),Z.copy()
        m = int(len(f)/2)
        f[m::],s[m::] = s[m::],f[m::]
        fd,sd = [],[]
        for i in range(m,len(f)):
            if f[i] in f[:m]: fd.append(i)
            if s[i] in s[:m]: sd.append(i)
        for i in range(len(fd)) : 
            f[fd[i]],s[sd[i]] = s[sd[i]],f[fd[i]] 
        return f,s


    def mutation(Y):
        i = randint(0,len(Y)-1)
        j = randint(0,len(Y)-1)
        f = Y.copy()
        if i!=j :
            f[i],f[j] = f[j],f[i]
        return f

    pop = []
    t = [i for i in range(2,len(Matrice)+1)]
    for i in range(10):
        shuffle(t)
        pop.append(t.copy())
    for index in range(N):
        c = [evaluation(Matrice,[1]+i+[1]) for i in pop]
        best = [pop[i] for i in np.array(c).argsort()[:6]]
        for j in range(0,6,2):
            best[j],best[j+1] = cr(best[j],best[j+1])
        i,j = randint(0,5),randint(0,5)
        best[i] = mutation(best[i])
        best[j] = mutation(best[j])
        ng = pop + best
        ngc = [evaluation(Matrice,[1]+i+[1]) for i in ng]
        pop = [ng[i] for i in np.array(ngc).argsort()[:10]]
    return [1]+pop[0]+[1],c[0]


path,cost = Genetique(matrice1,10000)
print(f"Meilleur solution : {path}")
print(f"l'evaluation est {cost}")


