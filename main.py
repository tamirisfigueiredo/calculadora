from tkinter import *
from tkinter import ttk

cor1 = '#1e1f1e'
cor2 = '#feffff'
cor3 = '#38576b'
cor4 = '#eceff1'
cor5 = '#ffab40'

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=cor1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)
frame_tela = Frame(janela, width=300, height=56, bg=cor2, pady=0, padx=0, relief='flat',)
frame_tela.grid(row=1, column=0, sticky=NW)
frame_corpo = Frame(janela, width=300, height=340, bg=cor5, pady=0, padx=0, relief='flat',)
frame_corpo.grid(row=2, column=0, sticky=NW)

todos_valores = ""
valor_texto = StringVar()

def entrar_valor(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

app_tela = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief='flat', anchor='e', bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=cor1)
app_tela.place(x=0, y=0)

b_1 = Button(frame_corpo, command=lambda: limpar_tela(), text='C', width=11, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrar_valor('%'), text='%', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda: entrar_valor('/'), text='/', width=5, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
b_4 = Button(frame_corpo, command=lambda: entrar_valor('7'), text='7', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command=lambda: entrar_valor('8'), text='8', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command=lambda: entrar_valor('9'), text='9', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command=lambda: entrar_valor('*'), text='*', width=5, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)
b_8 = Button(frame_corpo, command=lambda: entrar_valor('4'), text='4', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command=lambda: entrar_valor('5'), text='5', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command=lambda: entrar_valor('6'), text='6', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command=lambda: entrar_valor('-'), text='-', width=5, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)
b_12 = Button(frame_corpo, command=lambda: entrar_valor('1'), text='1', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command=lambda: entrar_valor('2'), text='2', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command=lambda: entrar_valor('3'), text='3', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command=lambda: entrar_valor('+'), text='+', width=5, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)
b_16 = Button(frame_corpo, command=lambda: entrar_valor('0'), text='0', width=11, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command=lambda: entrar_valor('.'), text='.', width=5, height=2, bg=cor3, fg=cor5, relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command=lambda: calcular(), text='=', width=5, height=2, bg=cor4, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()
