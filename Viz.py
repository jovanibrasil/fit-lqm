import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.optimize as optimization
from PIL import Image


def readdata(filename):
   
    '''
    '''
    
    global coefs_data, levels
    coefs_data = []
    
    with open(filename, "r") as f:
        content = f.read().splitlines()
    
        levels = int(content[0])
    
        for i in range(1, len(content)):
            e = content[i]
            l = []
            s = e.replace(" end", "")
            l = [float(e) for e in s.split(" ")] 
            coefs_data.append(l)
    f.close()


def func(X, c):

    x, y = X
    x2 = x*x
    y2 = y*y
    r1 = c[0]*x2*y2 + c[1]*x*y2 + c[2]*y2 + c[3]*x2*y 
    return r1 + c[4]*x*y + c[5]*y + c[6]*x2 + c[7]*x + c[8] 


def gen_img():
    '''
        Gera imagem a partir dos coeficientes lidos no arquivo de dados.

    '''

    global gray_img, result_img, levels
    
    width, height = gray_img.size
   
    result_data = result_img.load()

    quads = 1
    if levels == 0:
        quads = 1
    else:
        quads = 2 * levels
   
    stepx = width/quads
    stepy = height/quads 
   
    # ----- para cada quadro de x ate y ------
    x = y = 0
    for stepyc in range(0, quads):
        for stepxc in range(0, quads):
            #print "Processando quadrante =", stepxc, stepyc , "(x, y)"  

            ystepy = y+stepy
            xstepx = x+stepy

            # Testa se existe sobra
            if stepy * quads < height and stepyc == quads-1:
                ystepy = (height - ystepy) + ystepy
            if stepx * quads < width and stepxc == quads-1:
                xstepx = (width - xstepx) + xstepx

            coefficients = coefs_data[stepxc + (quads * stepyc)]

            # ------ aplica os resultados gerados ----
            for yc in range(y, ystepy):
                for xc in range(x, xstepx):
                    # prepara dados 
                    result_data[xc, yc] = int(func((xc, yc), coefficients))

            # Atualiza x
            x = x + stepx
        # Atualiza x e y
        x = 0
        y = y+stepy

def main(args):
    '''
        args[0] Nome do arquivo com extensao.
        
    '''

    global gray_img
    global result_img
    global coefs_data
    global img_name 
    global levels

    datafile_name = args[0]
    grey_img_name = datafile_name.replace("_data.txt", "").replace("_", ".")

    # Faz leitura do arquivo com os coeficientes.
    readdata(datafile_name)

    # Carrega imagem original e inicializa a resultado. 
    gray_img = Image.open(grey_img_name)
    result_img = Image.new('L', gray_img.size)

    # Gera valores dos pixels da imagem resultado.
    gen_img()

    # Mostra as duas lado a lado.
    gray_img.show(title = "0 Niveis")
    result_img.show(title =str(levels)+" Niveis")


if __name__ == "__main__":
    main(sys.argv[1:])


