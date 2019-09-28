from functions import *
a=['1','2','3']
b=['4','X','6']
c=['7','8','9']
print a,'\n',b,'\n',c
j=1
p=0
#b[1]='X'
while j<9:
    if j%2==0:
        print "it is computer turn"
      
        if a[0]=='X' and b[1]=='X' and c[2]=='9':
            c[2]='X'
        elif a[0]=='X' and a[2]=='X' and a[1]=='2':
            a[1]='X'
        elif a[0]=='X' and c[0]=='X' and b[0]=='4':
            b[0]='X'
        elif a[2]=='X' and c[2]=='X' and b[2]=='6':
            b[2]='X'
        elif c[0]=='X' and c[2]=='X' and c[1]=='8':
            c[1]='X'
        elif c[2]=='X' and b[1]=='X' and a[0]=='1':
            a[0]='X'
        elif c[0]=='X' and b[1]=='X' and a[2]=='3':
            a[2]='X'
        elif a[0]=='X' and b[0]=='X' and c[0]=='7':
            c[0]='X'
        elif a[0]=='X' and a[1]=='X' and a[2]=='3':
            a[2]='X'
        elif a[1]=='X' and a[2]=='X' and a[0]=='1':
            a[0]='X'
        elif a[2]=='X' and b[2]=='X' and c[2]=='9':
            c[2]='X'
        elif b[1]=='X' and b[0]=='X' and b[2]=='6':
            b[2]='X'
        elif b[2]=='X' and b[1]=='X' and b[0]=='4':
            b[0]='X'
        elif c[0]=='X' and b[0]=='X' and a[0]=='1':
            a[0]='X'
        elif a[1]=='X' and b[1]=='X' and c[1]=='8':
            c[1]='X'
        elif c[1]=='X' and b[1]=='X' and a[1]=='2':
            a[1]='X'
        elif c[2]=='X' and b[2]=='X' and a[2]=='3':
            a[2]='X'
        elif c[0]=='X' and c[1]=='X' and c[2]=='9':
            c[2]='X'
        elif c[1]=='X' and c[2]=='X' and c[0]=='7':
            c[0]='X'
        elif a[0]=='O' and b[0]=='O' and c[0]=='7':
            c[0]='X'
        elif a[0]=='O' and a[1]=='O' and a[2]=='3':
            a[2]='X'
        elif a[0]=='O' and c[0]=='O' and b[0]=='4':
            b[0]='X'
        elif a[2]=='O' and c[2]=='O' and b[2]=='6':
            b[2]='X'
        elif a[0]=='O' and a[2]=='O' and a[1]=='2':
            a[1]='X'
        elif c[0]=='O' and c[2]=='O' and c[1]=='8':
            c[1]='X'
        elif a[1]=='O' and a[2]=='O' and a[0]=='1':
            a[0]='X'
        elif a[2]=='O' and b[2]=='O' and c[2]=='9':
            c[2]='X'
        elif c[0]=='O' and c[1]=='O' and c[2]=='9':
            c[2]='X'
        elif c[1]=='O' and c[2]=='O' and c[0]=='7':
            c[0]='X'
        elif c[2]=='O' and b[2]=='O' and a[2]=='3':
            a[2]='X'
        elif a[0]=='1':
            a[0]='X'
            
        elif a[2]=='3':
            a[2]='X'
            
        elif c[0]=='7':
            c[0]='X'
            
        elif c[2]=='9':
            c[2]='X'
              
            
        elif a[1]=='2':
            a[1]='X'
            
        elif b[0]=='4':
            b[0]='X'
            
        elif b[2]=='6':
            b[2]='X'
            
        elif c[1]=='8':
            c[1]='X'
            
        #j=j+1     
         
    elif j%2!=0:
         x=input('Player 1 Enter location :-')
         if x<=3:
             if a[x-1]=='X' or a[x-1]=='O':
                 print 'Not Valid Location'
                 j=j-1
             else:
                 a[x-1]='O'
         if x>3 and x<=6:
             if b[x-4]=='X' or b[x-4]=='O':
                 print 'Not Valid Location'
                 j=j-1
             else:
                 b[x-4]='O'
         if x>6 and x<=9:
             if c[x-7]=='X' or c[x-7]=='O':
                 print 'Not Valid Location'
                 j=j-1
             else:
                 c[x-7]='O'
         if x<=0 or x>9:
             print 'Enter valid location'
             j=j-1
    j=j+1
    print a,'\n',b,'\n',c
    if check_col(a,b,c) or check_row(a,b,c) or check_dia(a,b,c):
        p=1
        break

if p==0:
    print 'Match Draw'
 
