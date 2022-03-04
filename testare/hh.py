'''
Created on 31 ian. 2021

@author: user
'''
x = [1, 2, 3]
x1 = [1] + x[1:]
x2 = x[:2] + [x[-1]]
print(x,x1,x2)

def pare(l):
    if len(l)==1:
        return l[0]
    if len(l)==0: return 1
    return l[0]*pare(l[2:])

print(pare([1,2,3,4,5,6,0]))