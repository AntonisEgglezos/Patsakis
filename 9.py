def maxSequence(lista):
    maxnow=0
    fmax= 0
    sublist= []
    size=len(lista)
    for i in range(size):
        fmax+=lista[i]
        if fmax<0:
            fmax=0
            mv=i+1
        elif (maxnow<fmax):
            maxnow=fmax
            start=mv
            end=i
    for j in range(start,end+1):
        sublist.append(lista[j])
    print (maxnow,sublist)
