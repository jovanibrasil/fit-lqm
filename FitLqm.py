import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.optimize as optimization
from PIL import Image

def savedata(levels):
    '''
        Salva resultados gerados em um arquivo texto.
        
        Ordem do arquivo:

        1. Nome da imagem.
        2. Quantidade de polinomios gerados (ou numero de quadrantes, pois
        cada polinomio representa um quadrante).
        3. Lista de coeficientes para cada polinomio. 

    '''
    
    global coefs_data
    
    f = open( img_name.replace('.', '_') + "_data.txt", "w") 
    f.write(str(levels)+"\n")
    for e in coefs_data:
        for n in e:
            f.write(str(n) + " ")
        f.write("end\n")
    f.close()


def func(X, a, b, c, d, e, f, g, h, i):
    
    x, y = X
    x2 = x*x
    y2 = y*y
    return a*x2*y2 + b*x*y2 + c*y2 + d*x2*y + e*x*y + f*y + g*x2 + h*x + i 


def solve(levels):

    '''
        
        Description ...

        levels  -   Quantidade de divisoes que devem ser geradas na imagem.
    '''

    global color_img, gray_img, coefs_data
    
    width, height = gray_img.size
        
    img = gray_img.load()
   
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

            # ------ percorre o quadro -------
            vl = []
            xl = []
            yl = []
            for yc in range(y, ystepy):
                for xc in range(x, xstepx):
                    # prepara dados 
                    vl.append(img[xc, yc])                    
                    xl.append(xc)
                    yl.append(yc)
            # ------ realiza operacao de ajuste -----
            x0 = numpy.array([0.0]*9)
            coefficients = optimization.curve_fit(func, (xl, yl), vl, x0)[0]
            
            # Save coefficients
            coefs_data.append(coefficients)

            # Atualiza x
            x = x + stepx
        # Atualiza x e y
        x = 0
        y = y+stepy


def main(args):
    '''
        args[0] Nome do arquivo com extensao.
        args[1] Quantidade de niveis.
    '''

    global color_img
    global gray_img
    global coefs_data
    global img_name

    # Carrega uma imagem.
    coefs_data = []
    #img = Image.open("br.png")

    img_name = args[0]

    color_img = Image.open(img_name)
    gray_img = color_img.convert('L')

    result_img = Image.new('L', gray_img.size)

    solve(int(args[1]))

    savedata(int(args[1]))


if __name__ == "__main__":
    main(sys.argv[1:])



