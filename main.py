from tkinter import *
from tkinter import ttk

COR1 = '#1e1f1e'
COR2 = '#feffff'
COR3 = '#38576b'
COR4 = '#eceff1'
COR5 = '#ffab40'

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x305')
janela.config(bg=COR1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)
frame_tela = Frame(janela, width=235, height=50, bg=COR3, pady=0, padx=0, relief='flat',)
frame_tela.grid(row=0, column=0, sticky=NW)
frame_corpo = Frame(janela, width=235, height=268, bg=COR5, pady=0, padx=0, relief='flat',)
frame_corpo.grid(row=1, column=0, sticky=NW)

TODOS_VALORES = ""
valor_texto = StringVar()

def entrar_valor(event):
    global TODOS_VALORES
    TODOS_VALORES = TODOS_VALORES + str(event)
    valor_texto.set(TODOS_VALORES)

def calcular():
    try:
        global TODOS_VALORES
        TODOS_VALORES = TODOS_VALORES.replace('x', '*')
        TODOS_VALORES = TODOS_VALORES.replace('÷', '/')
        if '**' in TODOS_VALORES:
            valor_texto.set('Equação Inválida.')
        if '*-+' in TODOS_VALORES:
            valor_texto.set('Equação Inválida.')
        if '*+-' in TODOS_VALORES:
            valor_texto.set('Equação Inválida.')
        else:
            resultado = eval(TODOS_VALORES)
            valor_texto.set(resultado)
    except SyntaxError:
        valor_texto.set('Equação Inválida.')
    except ZeroDivisionError:
        valor_texto.set('Impos. dividir por 0.')

def limpar_tela():
    global TODOS_VALORES
    TODOS_VALORES = ""
    valor_texto.set("")

app_tela = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7,
 relief='flat', anchor='e', bd=0, justify=RIGHT, font=('Ivy 18 '), bg=COR3, fg=COR2)
app_tela.place(x=0, y=0)

b_1 = Button(frame_corpo, command=lambda: limpar_tela(), text='C', width=11,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrar_valor('%'), text='%', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command=lambda: entrar_valor('/'), text='/', width=5,
 height=2, bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)
b_4 = Button(frame_corpo, command=lambda: entrar_valor('7'), text='7', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command=lambda: entrar_valor('8'), text='8', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, command=lambda: entrar_valor('9'), text='9', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52)
b_7 = Button(frame_corpo, command=lambda: entrar_valor('*'), text='*', width=5,
 height=2, bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=52)
b_8 = Button(frame_corpo, command=lambda: entrar_valor('4'), text='4', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command=lambda: entrar_valor('5'), text='5', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=104)
b_10 = Button(frame_corpo, command=lambda: entrar_valor('6'), text='6', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=104)
b_11 = Button(frame_corpo, command=lambda: entrar_valor('-'), text='-', width=5,
 height=2, bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=104)
b_12 = Button(frame_corpo, command=lambda: entrar_valor('1'), text='1', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command=lambda: entrar_valor('2'), text='2', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=156)
b_14 = Button(frame_corpo, command=lambda: entrar_valor('3'), text='3', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=156)
b_15 = Button(frame_corpo, command=lambda: entrar_valor('+'), text='+', width=5,
 height=2, bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=156)
b_16 = Button(frame_corpo, command=lambda: entrar_valor('0'), text='0', width=11,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command=lambda: entrar_valor('.'), text='.', width=5,
 height=2, bg=COR4, fg=COR1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208)
b_18 = Button(frame_corpo, command=lambda: calcular(), text='=', width=5,
 height=2, bg=COR5, fg=COR2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=208)


janela.mainloop()
