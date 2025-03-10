import os

rows = 20
cols = 20
largura_tela = os.get_terminal_size().columns
largura_linha = cols *2

for i in range(rows):
    linha =" "
    for j in range(cols):
        if(i+j)%2==0:
            linha += "X "
        else:
            linha +="0 "
    largura_extra = (largura_tela - largura_linha)//2
    print(" " * largura_extra + linha)