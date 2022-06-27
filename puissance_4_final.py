position=[
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "]]
t=0
score=-1

def affichage(p):
    print(" 1 2 3 4 5 6 7")
    print("┌─────────────┐")
    for row in p:
        m = "│" + ' '.join(str(e) for e in row) + "│"
        print(m)
    print("└─────────────┘")


def testvictoire(x,y):
    x=x-1
    #vertical
    if y<=2:
        if position[y][x]==position[y+1][x]==position[y+2][x]==position[y+3][x]:
            return True
    #horizontal
    elif x>=3:
        if position[y][x]==position[y][x-1]==position[y][x-2]==position[y][x-3]:
            return True
    if 5>=x>=2:
        if position[y][x]==position[y][x+1]==position[y][x-1]==position[y][x-2]:
            return True
    if 4>=x>=1:
        if position[y][x]==position[y][x+1]==position[y][x-1]==position[y][x+2]:
            return True
    if x<=3:
        if position[y][x]==position[y][x+1]==position[y][x+3]==position[y][x+2]:
            return True
    #diagonal droite
    if y<=2 and x<=3:
        if position[y][x]==position[y+1][x+1]==position[y+2][x+2]==position[y+3][x+3]:
            return True
    if 5>=x>=2 and 4>=y>=2:
        if position[y][x]==position[y+1][x+1]==position[y-1][x-1]==position[y-2][x-2]:
            return True
    if x>=3 and y>=3:
        if position[y][x]==position[y-1][x-1]==position[y-2][x-2]==position[y-3][x-3]:
            return True
    if 4>=x>=1 and 3>=y>=1:
        if position[y][x]==position[y-1][x+1]==position[y+1][x+1]==position[y+2][x+2]:
            return True
    #diagonal gauche
    if x>=3 and y<=2:
        if position[y][x]==position[y+1][x-1]==position[y+2][x-2]==position[y+3][x-3]:
            return True
    if 5>=x>=2 and 3>=y>=1:
        if position[y][x]==position[y+1][x-1]==position[y+2][x-2]==position[y-1][x+1]:
            return True
    if 1<=x<=4 and 2<=y<=4:
        if position[y][x]==position[y+1][x-1]==position[y-1][x+1]==position[y-2][x+2]:
            return True
    if x<=3 and y>=3:
        if position[y][x]==position[y-1][x+1]==position[y-2][x+2]==position[y-3][x+3]:
            return True
    else:
        return False


while score==-1:
    y1=0
    x1=int(input("Joeur X:"))
    if position[5][x1-1]=="O" or position[5][x1-1]=="X" :
        if position[4][x1-1]=="O" or position[4][x1-1]=="X" :
            if position[3][x1-1]=="O" or position[3][x1-1]=="X" :
                if position[2][x1-1]=="O" or position[2][x1-1]=="X" :
                    if position[1][x1-1]=="O" or position[1][x1-1]=="X" :
                        if position[0][x1-1]=="O" or position[0][x1-1]=="X" :
                            print("Coup illégal !")
                        else:
                            position[0][x1-1]="X"
                            y1=0
                    else:
                        position[1][x1-1]="X"
                        y1=1
                else:
                    position[2][x1-1]="X"
                    y1=2
            else:
                position[3][x1-1]="X"
                y1=3
        else:
            position[4][x1-1]="X"
            y1=4
    else:
        position[5][x1-1]="X"
        y1=5
    affichage(position)
    if testvictoire(x1,y1)==True:
        print("Le joueur X  a gagné")
        score=1
        break
    t+=1
    y2=0
    x2=int(input("Joueur O:"))
    if position[5][x2-1]=="O" or position[5][x2-1]=="X" :
        if position[4][x2-1]=="O" or position[4][x2-1]=="X" :
            if position[3][x2-1]=="O" or position[3][x2-1]=="X" :
                if position[2][x2-1]=="O" or position[2][x2-1]=="X" :
                    if position[1][x2-1]=="O" or position[1][x2-1]=="X" :
                        if position[0][x2-1]=="O" or position[0][x2-1]=="X" :
                            print("Coup illégal !")
                        else:
                            position[0][x2-1]="O"
                            y2=0
                    else:
                        position[1][x2-1]="O"
                        y2=1
                else:
                    position[2][x2-1]="O"
                    y2=2
            else:
                position[3][x2-1]="O"
                y2=3
        else:
            position[4][x2-1]="O"
            y2=4
    else:
        position[5][x2-1]="O"
        y2=5
    affichage(position)
    if testvictoire(x2,y2)==True:
        print("Le joueur O a gagné")
        score=0
    t+=1
    if t==42:
        print("Match nul !")
        score=1