import os
largura_tela = os.get_terminal_size().columns
rows = 30
for i in range(1,rows +1):
    linha = " " * (rows -1) + "*" * (2*i -1)
    espacos_extras = (largura_tela - len(linha))//2
    print(" " * espacos_extras + linha)
    

for i in range(rows-1,0,-1):
    linha = " " * (rows -1) + "*" * (2*i -1)
    espacos_extras = (largura_tela - len(linha))//2
    print(" " * espacos_extras + linha)
