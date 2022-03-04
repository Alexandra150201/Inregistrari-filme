def __return_key(element,key):
    return key(element)


def insertSort(l,key=lambda x:x,key2=0,cmp=lambda x,y:x>y,cmp2=lambda x,y:x==y,reverse=False):
    """
 sort the element of the list
 l - list of element
 return the ordered list (l[0]<l[1]<...)
    """
    if not key2:
        for i in range(1,len(l)):
            ind = i-1
            a = l[i]
 #insert a in the right position
            while (ind>=0 and cmp(__return_key(l[ind],key),__return_key(a,key)) and reverse==False) or (ind>=0 and cmp(__return_key(a,key),__return_key(l[ind],key)) and reverse==True):
                 l[ind+1] = l[ind]
                 ind = ind-1
            l[ind+1] = a
        return l
    else:
        for i in range(1,len(l)):
            ind = i-1
            a = l[i]
 #insert a in the right position
            while (ind>=0 and cmp(__return_key(l[ind],key),__return_key(a,key)) and reverse==False) or \
             (ind>=0 and cmp(__return_key(l[ind],key2),__return_key(a,key2)) and 
              cmp2(__return_key(l[ind],key),__return_key(a,key)) and reverse==False) or \
              (ind>=0 and cmp(__return_key(a,key),__return_key(l[ind],key)) and reverse==True) or \
              (ind>=0 and cmp(__return_key(a,key2),__return_key(l[ind],key2)) and 
               cmp2(__return_key(l[ind],key),__return_key(a,key)) and reverse==True):
                 l[ind+1] = l[ind]
                 ind = ind-1
            l[ind+1] = a
        return l
        

def bingoSort(lista,key=lambda x:x,cmp=lambda x,y:x>y,reverse=False):
    """
    This procedure sorts in ascending order.
    """
    max=len(lista)-1
    nextValue=lista[max]
    for i in range(max-1,0,-1):
        if cmp(__return_key(lista[i],key),__return_key(nextValue,key)):
            nextValue=lista[i]
    while max > 0 and lista[max] ==nextValue:
        max= max-1

    while max > 0:
        value=nextValue
        nextValue=lista[max]
        for i in range(max-1,0,-1):
             if __return_key(lista[i],key)==__return_key(value,key):
                 aux=lista[i]
                 lista[i]=lista[max] 
                 lista[max]=aux
                 max=max-1
             elif cmp(__return_key(lista[i],key),__return_key(nextValue,key)):
                 nextValue=lista[i]
        while max > 0 and __return_key(lista[max],key)==__return_key(nextValue,key):
            max=max-1
    return lista

def mergeSort(l,start,end):
    if len(l)<=1:
        return 
    m=(end+start)//2
    mergeSort(l,start,m)
    mergeSort(l,m,end)
   # merge(l,start,end,m)
