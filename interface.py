import PySimpleGUI as sg
from main import arte_jogo

termos = []

layout = [
    [sg.Text('Digite os nomes dos jogos no campo abaixo:')],
    [sg.Multiline('',size=(60,30),key='texto'),sg.T('Aguarde...',visible=False,key='aguarde')],
    [sg.Button('ok',pad=(170,1),size=(10,2),font='Arial 12')]
]

janela = sg.Window('Titulo', layout, size=(800,600), finalize=True)

while True:
    event, value = janela.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'ok':
        txt = open('texto.txt','w')
        txt.write(value['texto'])
        txt.close()
        janela['aguarde'].update(visible=True)
        janela.refresh()
        txt = open('texto.txt','r')
        for jogo in txt.readlines():
            if jogo.endswith('\n'):
                jogo = jogo[:-1]
            termos.append(jogo)
        arte_jogo(termos)
        janela['aguarde'].update(visible=False)
        janela.refresh()
janela.close()