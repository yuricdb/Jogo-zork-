"""
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programão 1

Autor: Yuri Correia de Barros (ycb)
Email: ycb@cin.ufpe.br
Data: 2019-08-22

"""

#O JOGO FOI TESTADO E FUNCIONOU, FAVOR QUALQUER BUG ENVIAR A LINHA POR EMAIL.

up = 'cima'
down = 'baixo'
left = 'esquerda'
right = 'direita'
desc = 'onde estou'
obj3= 'chave'
obj4= 'banco'
obj5= 'dinheiro'
obj6= 'sachê'
hand=''
geladeira = True
gaveta= False
gato = True
pote=False
casaco = False
dinheiro = False
print('Hoje é sexta feira e você tem um encontro para assistir a um filme no cinema\nTente sair sem atraso, mas lembre-se de não esquecer nada\n')
print(f'os comandos possíveis são: {down}, {left}, {right}, {up}\npegar, sim, encher, fechar, abrir\n')
y = 3
x = 8
game=True
move=''
 
while (game):
    if ((x==8) and (y>=2 and y<=4)): #blocoG
        print('Você está na posição:', x,y, '\n')
        if (y==4) and (geladeira==True):
            print('A janela está fechada, mas parece que continua frio\n')
        move = input('digite um comando\n')
        if (move == left):
            x += -1
        elif (move == right):
            print('Melhor do que assistir filme repetido no sofá de casa,\né assistir a uma estreia sentado numa tela de cinema')     
        elif (move == up):
            y += 1
        elif (move == down):
            y += -1

    if ((x>=1 and x<=9) and (y==1)): #blocoF
        print('Você está na posição:',x,y, '\n')
        move = input('digite um comando\n')
        if (move == left) and (x==1):
            print('parede')
        elif (move == left):
            x += -1
        elif (move == right) and ((x==9) and (pote==False)):
            move=input('o pote de comida do bichano está vazio')       
            if ((hand==obj6) and (move.upper()=='ENCHER')):
                gato=False
                pote=True
            elif (move.upper()=='ENCHER'):
                print(f'Tem certeza que não quer procurar o {obj6}?')
        elif (move == right) and (x==9):
            print('Seu bichano está amando a refeição')
        elif (move == right):
            x += 1     
        elif (move == up) and (x==9):
            print('Você não pode passar pelo sofá')
        elif (move == up):
            y += 1
        elif (move == down) and (x>=4 and x<=6):
            print('O quadro é muito bonito,\nMas de longe parece um espelho refletindo a geladeira,\narmário e todas as outras coisas ao norte')
        elif (move == down) and (x==2): #portaFIM
            if (dinheiro == True) and (casaco == True):
                input('Parabéns você fez com que o personagem pudesse ir ao cinema\n\n\n=-=-=-=-=GAME OVER=-=-=-=-=\n\n\nYuri Barros\nycb@cin.ufpe.br\nycb')#IMPEDE QUE O JOGO FECHE ANTES DE MOSTRAR O GAME OVER
                game==False
            elif (dinheiro==True):
                print('Com certeza você não vai querer passar frio dentro do cinema')
            elif (casaco==True):
                print('A entrada do cinema não é de graça')
        elif (move == down):
            print('parede')



    if ((x>=8 and x<=10) and (y>=8 and y<=10)): #blocoE
        print('Você está na posição:',x,y, '\n')
        move = input('digite um comando\n')
        if (move == left) and (y==10 and x==8):
            print('Armário')
        elif (move == left):
            x += -1
        elif (move == right) and (y==10 and (x>=8 and x<=10)):
            print('geladeira')
        elif (move == right) and (x==10 and (y>=8 and y<=10)):
            print('parede')
        elif (move == right):
            x += 1  
        elif (move == up) and ((y==9) and (x>=9 and x<=10)):
            print('Há uma geladeira acima')
            if ((x==10) and (y==9)) and (geladeira==True):
                move=input('a porta da geladeira está aberta')
                if(move.upper()=='FECHAR'):
                    move = input(f'\nHá um banco empatando a porta de fechar, deseja pegar o {obj4}')
                    if (move.upper()=='SIM'):   
                        hand=obj4
                        geladeira=False
        elif (move == up) and (y==10):
            print('Alguém está usando o banheiro')
        elif (move == up):
            y += 1
        elif (move == down):
            y += -1   

    if ((x>=6 and x<=10) and (y>=5 and y<=7)): #blocoD
        print('Você está na posição:',x,y, '\n')
        move = input('digite um comando\n')
        if (move == left) and ((x==6) and (y>=5 and y<=7)):
            print('há vários talheres em cima da mesa')
            if (y==6) and (hand!=obj6):
                move=input('O sachê do gato está na mesa')
                if (move.upper()=="PEGAR"):
                    hand=obj6
        elif (move == left):
            x += -1
        elif (move == right) and ((x==10) and (y>=5 and y<=7)):
            if (y==7):
                print('"Vejo uma grade e um velho sinal..."') #nao significa nada só uma música =D ("paisagem da janela" Lô borges)
            elif (y==5):
                print('parede')
            else:
                print('Paisagem da janela')
        elif (move == right):
            x += 1     
        elif (move == up):
            y += 1
        elif (move == down) and ((y==5) and (x>=9 and x<=10)):
            print('Há um sofá abaixo')
        elif (move == down):
            y += -1
        if (x==8 and y==7):
            print('O sol da janela a leste batendo na mesa a oeste deixa o verniz da madeira ainda mais brilhante')
    
    if ((x>=1 and x<=7) and (y>=2 and y<=4)): #blocoC
        print('Você está na posição:',x,y, '\n')
        move=input('digite um comando\n')
        if (move==left) and (y==3 and x==1):
            if (gato==True):
                move==print('Há um gato em cima do criado mudo')
            elif (gato==False) and (gaveta==False):
                move = input('Essa deve ser a chave da gaveta')
                if (move.upper()=='PEGAR'):
                    hand=obj3
            elif(gato==False):
                print('Há um criado mudo aqui')
        elif (move == left) and (x==1):
            print('parede')
        elif (move==left):
            x += -1
        elif (move == right):
            x += 1     
        elif (move == up) and ((y==4) and (x>=3 and x<=5)):
            print('Você não pode subir na mesa acima')
        elif (move == up):
            y += 1
        elif (move == down):
            y += -1
        if (x==4 and y==3):
            print('um largo corredor, mesas e cadeiras ao norte, e um espelho ao sul')
        if (x==7 and y==3):
            print('a oeste, parece algo em cima do móvel a oeste')
            
    if ((x>=1 and x<=2) and (y>=5 and y<=7)): #blocoA concluido

        print('Você está na posição:',x,y, '\n')
        move = input('digite um comando\n')
        if (move == left) and (x == 1):
            print('parede')
        elif (move == left):
            x += -1
        elif (move == right)and (x == 2):
            print('essa mesa está uma bagunça, mas não dá tempo de arrumar')    
        elif (move == right):
            x += 1
        elif (move == up) and (x==1 and y==7):
            print('há uma gaveta acima')
        elif (move == up):
            y += 1
        elif (move == down):
            y += -1
   
    if ((x>=2 and x<=7) and (y>=8 and y<=9)): #blocoB
        print('Você está na posição:',x,y, '\n')
        move = input('digite um comando\n')
        if (move == left) and ((y>=8 and y<=9) and (x==2)):
            if (gaveta==False):   
                move=input('A gaveta está trancada')           
                if (move.upper()=='ABRIR') and (hand==obj3):
                    gaveta=True
                    move=input('A gaveta está aberta, há dinheiro suficiente para o ingresso')
                    if (move.upper()=='PEGAR'):
                        dinheiro=True
                elif (move.upper()=='abrir'):
                    print('procure a chave para tentar abrir a gaveta')
            elif (gaveta==True) and (dinheiro==True):
                print('Você já pegou o dinheiro que precisa')
            elif (gaveta==True):
                move=input('Pegue o dinheiro que precisa e não se esqueça do resto')
                if (move.upper()=='pegar'):
                    dinheiro=True        
        elif (move == left):
            x += -1  
        elif (move == right):
            x += 1     
        elif (move == up) and ((y==9) and (x>=2 and x<=3)):
            print('Há todo tipo de coisas aqui, de roupas a brinquedos')
        elif (move == up) and ((y==9) and (x>=4 and x<=5)):
            print('A porta do meio do guarda roupa está quebrada')
        elif (move == up) and ((y==9) and (x>=6 and x<=7)):
            if (casaco==False):
                move=input('parece que o casaco foi guardado na parte mais alta')
                if (hand==obj4) and (move.upper()=='PEGAR'):
                    casaco=True
                elif (move.upper()=='PEGAR'):
                    print('você precisa de algo para subir')
            elif (casaco==True):
                print('filme agasalhado é uma maravilha')
                
        elif (move == up):
            y += 1
        elif (move == down) and ((y==8) and (x>=3 and x<=5)):
            print('Não dá pra subir na mesa')
        elif (move == down):
            y += -1
           
