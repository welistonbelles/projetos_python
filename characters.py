from tkinter import *
from PIL import Image, ImageTk


def next():
    tam = len(character.list_character)
    if character.current_character == tam:
        character.current_character = 1
        current_img['file'] = character.list_character[character.current_character]
        print("Resetou")
    else:
        character.current_character += 1
        current_img['file'] = character.list_character[character.current_character]
    prev_img['file'] = prev_image()
    next_img['file'] = next_image()

def prev():
    tam = len(character.list_character)
    if character.current_character == 1:
        character.current_character = tam
        current_img['file'] = character.list_character[character.current_character]
        print("Resetou")
    else:
        character.current_character -= 1
        current_img['file'] = character.list_character[character.current_character]
    prev_img['file'] = prev_image()
    next_img['file'] = next_image()


def select_character():
    print(f"Personagem escolhido: {character.list_character[character.current_character]}")


def prev_image():
    tam = len(character.list_character)
    if character.current_character == 1:
        character.prev_img = tam
        str = f'small_{character.list_character[character.prev_img]}'
        return str
    else:
        character.prev_img = character.current_character - 1
        str = f'small_{character.list_character[character.prev_img]}'
        return str

def next_image():
    tam = len(character.list_character)
    if character.current_character == tam:
        character.next_img = 1
        str = f'small_{character.list_character[character.next_img]}'
        return str
    else:
        character.next_img = character.current_character + 1
        str = f'small_{character.list_character[character.next_img]}'
        return str

class Character:

    def __init__(self):
        self.current_character = 1
        self.next_character = 0
        self.prev_character = 0
        self.prev_img = 0
        self.next_img = 0
        self.list_character = {1: 'ichigo.png', 2: 'inoue.png', 3: 'chad.png', 4: 'rukia.png'}


character = Character()
janela = Tk()
janela.title("Seleção de Personagens")

setadireita = ImageTk.PhotoImage(Image.open("setadireita.png"))
setaesquerda = ImageTk.PhotoImage(Image.open("setaesquerda.png"))
select_button = PhotoImage(file="select.png")
current_img = PhotoImage(file=character.list_character[character.current_character])
prev_img = PhotoImage(file=prev_image())
next_img = PhotoImage(file=next_image())
img_chad = ImageTk.PhotoImage(Image.open("chad.png"))



select_character = Button(janela, width=350, height=120, image=select_button, command=select_character).place(x=270, y=520)
leftImg = Label(janela, width=390, height=500, image=prev_img).place(x=50, y=0)
rightImg = Label(janela, width=390, height=500, image=next_img).place(x=450, y=0)
lbFunctions = Label(janela, width=390, height=500, image=current_img).place(x=250, y=0)
seta_esquerda = Button(janela, width=32, image=setaesquerda, command=prev).place(x=30, y=260)
seta_direita = Button(janela, width=32, image=setadireita, command=next).place(x=830, y=260)

for n in character.list_character:
    print(n, character.list_character[n])
else:
    print("Erro")





janela.resizable(width=False, height=False)
janela.geometry("900x650+300+20")
janela.mainloop()