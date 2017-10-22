'''

    Autor: Jovani Brasil
    Email: jovanibrasil@gmail.com

    TODO

    - captura de erros.

'''

import sys
import scipy.optimize as optimization
from PIL import Image

def savedata(levels):
    '''
        Salva resultados gerados em um arquivo texto.
        Cada linha representa um conjunto de coeficientes para um quadrantes.

        levels - Numero de niveis executados.

    '''

    global coefs_data

    f_name = img_name.replace('.', '-') + "_" + str(levels) + "_data.txt"

    print "Salvando arquivo com coeficientes ... "

    f = open(f_name, "w") 
    for e in coefs_data:
        for n in e:
            f.write(str(n) + " ")
        f.write("end\n")
    f.close()

    print "Arquivo", f_name, "salvo!"


def func(X, a, b, c, d, e, f, g, h, i):
    '''
        Funcao utilizada pelo metodo.
    '''

    x, y = X
    x2 = x*x
    y2 = y*y
    return a*x2*y2 + b*x*y2 + c*y2 + d*x2*y + e*x*y + f*y + g*x2 + h*x + i 


def solve(levels):

    '''
        Aplica o metodo de ajuste dos minimos quadrados em uma imagem.


        levels  --  Quantidade de divisoes que devem ser geradas na imagem.
                    
        Dependendo da quantidade niveis de subdivisao e do tamanho
        da imagem podem ser necessarios quadrantes extras na extremidades
        para manter a qualidade dos resultados. Isso devido ao arredondamento
        para inteiro das dimensoes dos quadrantes, necessario para para
        trabalharmos com os indices da matriz. 

    '''

    print "Aplicando metodo de ajuste ..."

    global gray_img, coefs_data
    
    width, height = gray_img.size
        
    img = gray_img.load()

    quads = pow(2, levels)
   
    stepx = width/quads
    stepy = height/quads
    
    # Inicializa ponteiros x (horizontal) e  y (vertical)
    x = y = 0

    stepyc = stepxc = True

    while stepyc:

        ystepy = y+stepy

        # Condicao de parada.
        if ystepy >= height: 
            ystepy = height
            stepyc = False

        stepxc = True

        while stepxc:
            
            vl = []
            xl = []
            yl = [] 

            # Atualiza posicao dentro da imagem.
            xstepx = x+stepx

            # Condicao de parada. 
            if xstepx >= width:
                xstepx = width
                stepxc = False

            # Percorre o quadro a partir dos ponteiros.
            for yc in range(y, ystepy):
                for xc in range(x, xstepx):
                    # Prepara dados para o metodo. 
                    vl.append(img[xc, yc])                    
                    xl.append(xc)
                    yl.append(yc)

            # Realiza opercao de ajuste dos minimos quadrados.
            coefficients = optimization.curve_fit(func, (xl, yl), vl, [0.0]*9)[0]

            # Armazena coeficientes.
            coefs_data.append(coefficients)

            # Atualiza ponteiro horizontal.
            x = x + stepx
        # Retorna ponteiro horizontal ao inicio.
        x = 0
        # Atualiza ponteiro vertical.
        y = y+stepy

    print "Processo de ajuste concluido!"

def main(args):
    '''
        args[0] Nome do arquivo com extensao.
        args[1] Quantidade de niveis.
    '''

    global gray_img
    global coefs_data
    global img_name

    coefs_data = []
    img_name = args[0]

    print "Lendo", img_name, "..."
    gray_img = Image.open(img_name)
    print "Leitura Realizada com sucesso!"
    solve(int(args[1]))

    savedata(int(args[1]))


if __name__ == "__main__":
    main(sys.argv[1:])



