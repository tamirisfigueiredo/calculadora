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

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


janela.mainloop()
