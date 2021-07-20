import tkinter as tk
from tkinter import *



#---------------Janela Inicial---------------
janela = Tk()
janela.title("Cine IFPE")
janela.geometry('1080x720+150+10')
janela.config(bg=('#292c31'))
#---------------Frame Janela Inicial---------------
login = Frame(janela, borderwidth=4, bg='gray', relief='raised')
login.place(x=300,y=150,width=500,height=250)

#---------------Widgets Janela Inicial---------------

def username():
    un_nick['text'] = un_value.get()
    
un_text = Label(login, text='Usuário', font=('bold',19), relief='raised')
un_text.place(x=20,y=100)
un_value = Entry(login, font=('bold',20), relief='raised')
un_value.place(x=150,y=100)
confirmar = Button(login,text='Confirmar', font=('bold',12), relief='raised',command=username)
confirmar.place(x=372,y=180)


#---------------Widgets Avançar---------------
def next():
    un_value.place_forget()
    un_text.place_forget()
    confirmar.place_forget()
    avançar.place_forget()
   

    bt_Operador.place(x=50,y=180)
    bt_Cliente.place(x=280,y=180)
    un_nick.place(x=420,y=115)
    user_atual.place(x=300,y=115)
    opções.place(x=100,y=60)

avançar = Button(janela,text='Avançar', width=12, font=('bold',12), relief='raised',command=next)
avançar.place(x=500,y=450)
user_atual = Label(janela,text='Usuário atual:', width=12, font=('bold',13), relief='raised',bg='red', fg='white')
un_nick = Label(janela, text='Username', font=('bold',13), relief='raised',bg='green', fg='white')
opções = Label(login, text='O que você vai fazer hoje?', font=('bold',19), relief='raised')


#---------------Janela Operadores---------------

def operador():
    aviso  = tk.Toplevel()
    aviso.geometry('400x400+450+80')
    aviso.config(bg=('blue'))
    mensagem = Label(aviso,text='Ainda estamos programando essa parte!',font=('bold',15))
    mensagem.place(x=20,y=180)


bt_Operador = Button(login, width=18,  text='OPERAR SISTEMA', font=('bold',12), relief='raised', command=operador)

#---------------Janela Clientes---------------
def cliente():
    bt_Operador.place_forget()
    bt_Cliente.place_forget()
    login.place_forget()
    

    #---------------Frames Janela clientes---------------

    #Frame Superior
    fr_superior = Frame(janela,borderwidth=4, bg='#292c31')
    fr_superior.place(x=5,y=5,w=1070,h=150)

    #Método substitudo enquanto tento colocar a logo de volta
    w_ifpe = Label(fr_superior,text='Cine-IFPE',font=('bold',40),bg='gray',fg='white')
    w_ifpe.pack(anchor=CENTER)

    #Nesta parte o arquivo IFPE.png não foi mostrado no frame

    #logo = PhotoImage(file='Projeto_Cinema/Poster/IFPE.png')
    #w_ifpe = Label(fr_superior, image=logo)
    #w_ifpe.pack(anchor=CENTER)

    #Frame Lateral
    fr_lateral = Frame(janela, borderwidth=4, bg='#535760', relief='raised')
    fr_lateral.place(x=5,y=180,w=100,h=530)
    #Frame Central
    fr_central = Frame(janela, borderwidth=4, bg='#535760', relief='raised')
    fr_central.place(x=115,y=180,w=955,h=60)
    #Frame Sub-Central
    fr_sub = Frame(janela, borderwidth=4, bg='#535760', relief='raised')
    fr_sub.place(x=115,y=250,w=955,h=460)
    #Frame interno1 do Sub-Central
    fr_interno = Frame(fr_sub, borderwidth=4, bg='#75787f', relief='raised')
    #Frame interno2 do Sub-Central
    fr_interno2 = Frame(fr_sub, borderwidth=4, bg='#75787f', relief='raised')
    #Frame interno3 do Sub-Central
    fr_interno3 = Frame(fr_sub, borderwidth=4, bg='#75787f', relief='raised')

    #---------------Abas---------------

    #---------------Filmes---------------

    #Home do Cinema
    Cinema = ['Cine IFPE', PhotoImage(file='Projeto_Cinema/Poster/Banner_IF.png'),
    '''
    Ao longo de sua história, o IFPE se consolidou como um espaço 
    ofertante de uma educação pública,gratuita e de qualidade. 
    Uma casa de educação que contribui diretamente
    com o desenvolvimento econômico local, 
    mas sobretudo para a formação e inclusão de milhões de cidadãos
    '''
    ]
    indice = Label(fr_interno, text=Cinema[0], font=('bold', 15), bg= '#75787f', fg= '#fff')
    post_atual = Label(fr_interno, image=Cinema[1])
    sinopse = Label(fr_interno2, text=Cinema[2], font=('bold',13), bg= '#75787f', fg= '#fff')


    #Avengers: End Game
    Avengers = ['Avengers: Ultimato', PhotoImage(file='Projeto_Cinema/Poster/Ultimato.png'),
    '''
    Após Thanos eliminar metade das criaturas vivas, 
    os Vingadores têm de lidar com a perda de amigos e entes queridos. 
    Com Tony Stark vagando perdido no espaço sem água e comida, 
    Steve Rogers e Natasha Romanov lideram a resistência contra o titã louco.
    '''
    ]

    #O Hobbit
    Hobbit = ['O Hobbit', PhotoImage(file='Projeto_Cinema/Poster/O Hobbit 2.png'),
    '''
    Como a maioria dos hobbits, Bilbo Bolseiro leva uma vida tranquila 
    até o dia em que recebe uma missão do mago Gandalf.
    Acompanhado por um grupo de anões, 
    ele parte numa jornada até a Montanha Solitária 
    para libertar o Reino de Erebor do dragão Smaug.''']

    #Harry Potter
    Harry_Potter = ['Harry Potter', PhotoImage(file='Projeto_Cinema/Poster/Harry Potter.png'),
    '''
    Harry Potter é um garoto órfão que vive infeliz com seus tios, os Dursleys.
    Ele recebe uma carta contendo um convite para ingressar em Hogwarts,
    uma famosa escola especializada em formar jovens bruxos. 
    Inicialmente, Harry é impedido de ler a carta por seu tio, 
    mas logo recebe a visita de Hagrid, 
    o guarda-caça de Hogwarts, que chega para levá-lo até a escola. 
    Harry adentra um mundo mágico que jamais imaginara, 
    vivendo diversas aventuras com seus novos amigos,
    Rony Weasley e Hermione Granger.
    '''
    ]

    #Jogos Vorazes
    Jogos_Vorazes = ['Jogos Vorazes', PhotoImage(file='Projeto_Cinema/Poster/Jogos_Vorazes.png'),
    '''
    Após sobreviver à temível arena dos Jogos Vorazes,
    Katniss Everdeen está desanimada e destruída. 
    Depois que a Capital reduziu o Distrito 12 a destroços,
    ela se refugiou no Distrito 13.Peeta Mellark foi submetido a 
    uma lavagem cerebral ,e agora está sob o domínio de Snow.
    Então, a presidência quer que Katniss lidere uma "resistência" 
    e mobilize a população em uma empreitada que irá colocá-la 
    no centro da trama para desmascarar Snow.
    '''
    ]


    #---------------Widgets da aba Bilheteria---------------

    def bilheteria():
        #Posicionando nome,pôsters e sinopses
        indice.pack(anchor=CENTER)
        post_atual.pack(anchor=CENTER)
        sinopse.pack(anchor=CENTER)
        #Posicionando frames
        fr_interno.place(x=5,y=5,w=300,h=440)
        fr_interno2.place(x=325,y=5,w=600,h=250)
        fr_interno3.place(x=775,y=280)
        #Posicionando botões
        filme_ifpe.place(x=20,y=10)
        filme_1.place(x=160,y=10)
        filme_2.place(x=300,y=10)
        filme_3.place(x=440,y=10)
        filme_4.place(x=580,y=10)
        bt_buy.pack(anchor=CENTER)

    #---------------Ações internas da aba Bilheteria---------------
    def cine_ifpe():
        indice['text'] = Cinema[0]
        post_atual['image'] = Cinema[1]
        sinopse['text'] = Cinema[2]

    def movie1_click():
        indice['text'] = Avengers[0]
        post_atual['image'] = Avengers[1]
        sinopse['text'] = Avengers[2]

    def movie2_click():
        indice['text'] = Hobbit[0]
        post_atual['image'] = Hobbit[1]
        sinopse['text'] = Hobbit[2]

    def movie3_click():
        indice['text'] = Harry_Potter[0]
        post_atual['image'] = Harry_Potter[1]
        sinopse['text'] = Harry_Potter[2]

    def movie4_click():
        indice['text'] = Jogos_Vorazes[0]
        post_atual['image'] = Jogos_Vorazes[1]
        sinopse['text'] = Jogos_Vorazes[2]


    def buy():#Janela para comprar o ingresso
        comprar = tk.Toplevel(janela)
        comprar.geometry('300x300+700+250')
        comprar.config(bg=('#292c31'))
        compra_confirmada = Label(comprar,text='Compra efetuada com sucesso!',font=('bold',15))
        compra_confirmada.place(x=10,y=150)

    def hide():#Remoção dos widgets das abas

        #Widgets da aba Bilheteria
        filme_ifpe.place_forget()
        filme_1.place_forget()
        filme_2.place_forget()
        filme_3.place_forget()
        filme_4.place_forget()
        indice.pack_forget()
        sinopse.pack_forget()
        post_atual.pack_forget()
        fr_interno.place_forget()
        fr_interno2.place_forget()
        fr_interno3.place_forget()



    #---------------Widgets da aba Salas---------------

    #---------------Widgets do frame lateral---------------

    #Aba Bilheteria
    bt_bilhe = Button(fr_lateral,text='Bilheteria', font=('bold',12),command=bilheteria)
    bt_bilhe.place(x=5,y=10,width=80)

    #Aba Salas
    bt_sala = Button(fr_lateral,text='Salas', font=('bold',12),command=hide)
    bt_sala.place(x=5,y=60,width=80)

    #---------------Widgets da aba Bilheteria---------------

    filme_ifpe = Button(fr_central, width=12,  text='IFPE', font=('bold',12), command=cine_ifpe)
    filme_1 = Button(fr_central, width=12,  text='Ultimato', font=('bold',12), command=movie1_click)
    filme_2 = Button(fr_central, width=12,  text='O Hobbit', font=('bold',12), command=movie2_click)
    filme_3 = Button(fr_central, width=12,  text='Harry Potter', font=('bold',12), command=movie3_click)
    filme_4 = Button(fr_central, width=12,  text='Jogos Vorazes', font=('bold',12), command=movie4_click)
    bt_buy = Button(fr_interno3,  text='Comprar ingresso', font=('bold',12), command=buy)




    #---------------------------------------------------------------
        
bt_Cliente = Button(login, width=18,  text='USAR SISTEMA', font=('bold',12), relief='raised', command=cliente)



   












janela.mainloop()