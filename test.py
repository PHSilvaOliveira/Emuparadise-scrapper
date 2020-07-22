import regex
import webbrowser
from tkinter import *
import googlesearch

#pyinstaller --onefile test.py
def Baixar():
    jogo = googlesearch.lucky('emuparadise.me' + str(nome.get()),tld='me')
    print(jogo)
    emuParadise = regex.compile(r'(https://www.emuparadise.me/)' + '([\w-()]+)/' + '([\w-()\[\]]+/)' + '(\d+)')
    mb = emuParadise.search(str(jogo))
    numero = mb.group(4)
    output = 'https://www.emuparadise.me/roms/get-download.php?gid=' + numero + '&test=true'
    webbrowser.open(str(output))

interface = Tk()
interface.title('Interface')

# Colocar o título do jogo
TituloLabel = Label(interface, text = 'Insira o título do jogo' )
TituloLabel.grid(row = 50, column = 50)

#Colocar o nome
nomeLabel = Label(interface, text = 'Título')
nomeLabel.grid(row = 75, column = 50)
nome = Entry(interface)
nome.grid(row = 75, column= 100)

# Botão de Baixar (TODO) command=Baixar
Salvarlinha = Button(interface, text = 'Baixar', width = 10,command=Baixar)
Salvarlinha.grid(row = 250, column = 50)

#Propriedades da janela
interface.geometry('400x100+0+0')
interface.mainloop()