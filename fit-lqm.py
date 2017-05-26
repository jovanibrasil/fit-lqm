import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.optimize as optimization
from PIL import Image


def func(X, a, b, c, d, e, f, g, h, i):
    #print '>',  X
    x, y = X
    x2 = x*x
    y2 = y*y
    return a*x2*y2 + b*x*y2 + c*y2 + d*x2*y + e*x*y + f*y + g*x2 + h*x + i 


def func2(X, c):
    #print '>',  X
    x, y = X
    x2 = x*x
    y2 = y*y
    r1 = c[0]*x2*y2 + c[1]*x*y2 + c[2]*y2 + c[3]*x2*y 
    return r1 + c[4]*x*y + c[5]*y + c[6]*x2 + c[7]*x + c[8] 


def solve(levels):

    global gray_image, result_img
    
    width, height = gray_img.size
    img = gray_img.load()

    d = result_img.load()
   
    quads = 1
    if levels == 0:
        quads = 1
    else:
        quads = 2 * levels
   
    stepx = width/quads
    stepy = height/quads

    
    print "Dimensoes da imagem =", gray_img.size
    print "Total de quadrantes = ", quads
    print "stepx =", stepx, " stepy =", stepy 

    
    # ----- para cada quadro de x ate y ------
    x = y = 0
    for stepyc in range(0, quads):
        for stepxc in range(0, quads):
            #print "Processando quadrante =", stepxc, stepyc , "(x, y)"  
            
            # ------ percorre o quadro -------
            vl = []
            xl = []
            yl = []
            for yc in range(y, y+stepy):
                for xc in range(x, x+stepx):
                    # prepara dados 
                    
                    vl.append(img[xc, yc])
                    #d[xc, yc] = img[xc, yc]
                    xl.append(xc)
                    yl.append(yc)
        
            # ------ realiza operacao de ajuste -----
            x0 = numpy.array([0.0]*9)
            coefficients = optimization.curve_fit(func, (xl, yl), vl, x0)[0]

            # ------ aplica os resultados gerados ----
            for yc in range(y, y+stepy):
                for xc in range(x, x+stepx):
                    # prepara dados 
                    d[xc, yc] = int(func2((xc, yc), coefficients))

            # Atualiza x
            x = x + stepx
        # Atualiza x e y
        x = 0
        y = y+stepy


def main(args):

    global clr_img
    global gray_img
    global result_img

    # Carrega uma imagem.

    #img = Image.open("br.png")

    color_img = Image.open(args[0])
    gray_img = color_img.convert('L')

    result_img = Image.new('L', gray_img.size)

    solve(int(args[1]))

    # TODO Salvar o polinomio gerado.
    # TODO Desenha imagem ajustada e a original lado a lado.

    gray_img.show()
    result_img.show()

    #print "Image size: ", width, height
    #img.convert('L').save('br2.pgm')

if __name__ == "__main__":
    main(sys.argv[1:])



