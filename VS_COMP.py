from functions import *
N=raw_input("Enter player Name :")
a = ['1','2','3']
b = ['4','5','6']
c = ['7','8','9']
print a,'\n',b,'\n',c
inp = []                
usrinp = []             
j = 0                    
k = 0                      
for i in range(9):
    if i%2 == 0:
        print N,'TURN'
        x = input('Location for X ')
        while x<0 or x>9:                   
            print "Invalid Enter Again"
            x = input('Location for X ')
        while x in inp:                     
            print "Invalid Enter Again"
            x = input('Location for X ')
            while x<0 or x>9:
                print "Invalid Enter Again"
                x = input('Location for X ')
        inp.append(x)
        usrinp.append(x)
        if x<=3:
            a[x-1]='X'
        elif x<=6:
            b[x-4]='X'
        elif x<=9:
            c[x-7]='X'
        print a,'\n',b,'\n',c
        j = check_col(a,b,c)
        if j == 1:
            break;
        j = check_row(a,b,c)
        if j == 1:
            break;
        j = check_dig(a,b,c)
        if j == 1:
            break;
    else:
        print "COMP TURN"
        x = comp_ch(a,b,c,usrinp,inp)
        inp.append(x)
        if x<=3:
            a[x-1]='O'
        elif x<=6:
            b[x-4]='O'
        elif x<=9:
            c[x-7]='O'
        print a,'\n',b,'\n',c
        k = check_col(a,b,c)
        if k == 1:
            break;
        k = check_row(a,b,c)
        if k == 1:
            break;
        k = check_dig(a,b,c)
        if k == 1:
            break;



if k== 1:
    print 'COMPUTER WINS....'
elif j== 1:
    print '----',N,'WINS----'
else:
    print 'GAME TIE....BETTER LUCK NEXT TIME'


try:
    a = input("PRESS ENTER TO EXIT")
except (SyntaxError):
    a=0
