
import random


def check_col(a,b,c):

    for i in range(3):
        if a[i] == b[i] == c[i]:
            return 1
        

def check_row(a,b,c):
 
    for i in range(1):
        if a[i] == a[i+1] == a[i+2]:
            return 1
        if b[i] == b[i+1] == b[i+2]:
            return 1
        if c[i] == c[i+1] == c[i+2]:
            return 1


def check_dig(a,b,c):
   
    for i in range(1):
        if a[i] == b[i+1] == c[i+2]:
            return 1
        if a[i+2] == b[i+1] == c[i]:
            return 1


def row(a,b,c,inp):

    z = len(inp)
    for i in range(1):
        if a[i] == a[i+1]:
            if 3 not in inp:
                return 3
        elif a[i+1] == a[i+2]:
            if 1 not in inp:
                return 1
        elif a[i] == a[i+2]:
            if 2 not in inp:
                return 2
        elif b[i] == b[i+1]:
            if 6 not in inp:
                return 6
        elif b[i+1] == b[i+2]:
            if 4 not in inp:
                return 4
        elif b[i] == b[i+2]:
            if 5 not in inp:
                return 5
        elif c[i] == c[i+1]:
            if 9 not in inp:
                return 9
        elif c[i+1] == c[i+2]:
            if 7 not in inp:
                return 7
        elif c[i] == c[i+2]:
            if 8 not in inp:
                return 8


def col(a,b,c,inp):

    for i in range(3):
        if a[i] == b[i]:
            if i+7 not in inp:
                return i+7
        elif b[i] == c[i]:
            if i+1 not in inp:
                return i+1
        elif a[i] == c[i]:
            if i+4 not in inp:
                return i+4


def dig(a,b,c,inp):

    for i in range(1):
        if a[i] == b[i+1]:
            if 9 not in inp:
                return 9
        elif b[i+1] == c[i+2]:
            if 1 not in inp:
                return 1
        elif c[i+2] == a[1]:
            if 5 not in inp:
                return 5
        elif a[i+2] == b[i+1]:
            if 7 not in inp:
                return 7
        elif b[i+1] == c[i]:
            if 3 not in inp:
                return 3
        elif a[i+2] == c[i]:
            if 5 not in inp:
                return 5


def trick(a,b,c,inp):
  
    l,m,n=[],[],[]
    for i in a:
        l.append(i)
    for i in b:
        m.append(i)
    for i in c:
        n.append(i)
        
    M = [1,2,3,4,5,6,7,8,9]
    for i in inp:
            M.remove(i)

    for k in M:
        if k<=3:
            l[k-1]='O'
        elif k<=6:
            m[k-4]='O'
        elif k<=9:
            n[k-7]='O'
        x=0
        x = check_col(l,m,n)
        if x == 1:
            if k<=3:
                l[k-1]=str(k)
            elif k<=6:
                m[k-4]=str(k)
            elif k<=9:
                n[k-7]=str(k)
            return k
        x = check_row(l,m,n)
        if x == 1:
            if k<=3:
                l[k-1]=str(k)
            elif k<=6:
                m[k-4]=str(k)
            elif k<=9:
                n[k-7]=str(k)
            return k
        x = check_dig(l,m,n)
        if x == 1:
            if k<=3:
                l[k-1]=str(k)
            elif k<=6:
                m[k-4]=str(k)
            elif k<=9:
                n[k-7]=str(k)
            return k


def comp_ch(a,b,c,usrin,inp):
    
    K = len(usrin)
    j = 0
    if K == 1:
        if 1 in usrin or 3 in usrin or 7 in usrin or 9 in usrin:
            return 5
        elif 5 in usrin:
            return random.choice([1,3,7,9])
        else:
            return 5;

    if K == 2:
        j =row(a,b,c,inp)
        if j >0:
            return j
        j =col(a,b,c,inp)
        if j >0:
            return j
        j =dig(a,b,c,inp)
        if j >0:
            return j
        k=0
        M = [1,3,7,9]
        for i in inp:
            if i in M:
                M.remove(i)
        if 2 in usrin or 4 in usrin or 6 in usrin or 8 in usrin:
            k = random.choice(M)
            return k

        M = [2,4,6,8]
        for i in inp:
            if i in M:
                M.remove(i)
        if (1 in usrin and 9 in usrin) or (3 in usrin and 7 in usrin):
            k = random.choice([2,4,6,8])
            return k
        M = [1,3,5,7,9]
        for i in inp:
            M.remove(i)
        return random.choice(M)

        

    else:
        j=0
        j =row(a,b,c,inp)
        if j >0:
            return j
        j =col(a,b,c,inp)
        if j >0:
            return j
        j =dig(a,b,c,inp)
        if j >0:
            return j
        j =trick(a,b,c,inp)
        if j >0:
            return j
        M = [1,2,3,4,5,6,7,8,9]
        for i in inp:
            M.remove(i)
        return random.choice(M)    


