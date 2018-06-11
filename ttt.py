from random import choice

def reset():
    global count
    global mat
    global lt
    count=0
    mat=[['_','_','_'],['_','_','_'],['_','_','_']]
    lt=[1,2,3,4,5,6,7,8,9]

def get():
    inp=int(input('choose position[1-9]:'))
    while inp not in lt:
        print('choice is already taken')
        inp=int(input('choose position[1-9]:'))         
    else:
        return inp
    return inp

def put(inp,s):
    q=int(inp)-1
    mat[int(q/3)][int(q%3)]=s

def display(mat):
    for i in mat:
        print('',end='   ')
        for j in i:
            print(j,end=' ')
        print()
        

def cond(z,x):
    global count
    count+=1
    if mat[0][0]==z and mat[0][1]==z and mat[0][2]==z:
        win(x)
        return 'f'
    elif mat[1][0]==z and mat[1][1]==z and mat[1][2]==z:
        win(x)
        return 'f'
    elif mat[2][0]==z and mat[2][1]==z and mat[2][2]==z:
        win(x)
        return 'f'
    elif mat[0][0]==z and mat[1][0]==z and mat[2][0]==z:
        win(x)
        return 'f'
    elif mat[0][1]==z and mat[1][1]==z and mat[2][1]==z:
        win(x)
        return 'f'
    elif mat[0][2]==z and mat[1][2]==z and mat[2][2]==z:
        win(x)
        return 'f'
    elif mat[0][0]==z and mat[1][1]==z and mat[2][2]==z:
        win(x)
        return 'f'
    elif mat[0][2]==z and mat[1][1]==z and mat[2][0]==z:
        win(x)
        return 'f'
    elif count ==9:
        print('match draw')
        main()
        return 'f'

def win(x):
    if x=='player':
        print('you win!')
    else:
        print('computer wins!')
    main()

def choose():
    a=int(input('''enter 1 for 'O'
      2 for 'X':'''))
    print('\n')
    if a==1:
        player('O','X')
    elif a==2:
        comp('X','O')
    else:
        print('choose correct option:')

def comp(p,c):
    a=choice(lt)
    print('computer chooses',a)
    lt.remove(a)
    put(a,c)
    display(mat)
    m=cond(c,'comp')
    if m=='f':
        return 0
    else:
        player(p,c)

def player(p,c):
     inp=int(get())
     lt.remove(inp)
     put(inp,p)
     display(mat)
     n=cond(p,'player')
     if n=='f':
         return 0
     else:
         comp(p,c)

def main():
    x=input('play (y/n):')
    if x=='y':
        reset()
        print('\n\nTIC TAC TOE')
        display(mat)
        print('\n')
        choose()
    else:
        return 0

main()
