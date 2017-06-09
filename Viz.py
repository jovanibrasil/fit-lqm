'''

    Autor: Jovani Brasil
    Email: jovanibrasil@gmail.com

'''

import sys
import scipy.optimize as optimization
from PIL import Image


def readdata(filename):
    '''
        Faz leitura dos dados do arquivo de entrada.

        filename -- Nome arquivo de entrada.

    '''

    print "Lendo arquivo de coeficientes ..."

    global coefs_data, levels
    coefs_data = []
    
    with open(filename, "r") as f:
        content = f.read().splitlines()
    
        for i in range(0, len(content)):
            e = content[i]
             
            l = []
            s = e.replace(" end", "")
            l = [float(e) for e in s.split(" ")] 
            coefs_data.append(l)
    f.close()

    print filename, "lido com sucesso!"


def func(X, c):
    '''
        Funcao utilizada para construir a imagem.

        X -- Tupla com coordenadas x e y.
        c - Vetor de coeficientes.

    '''

    x, y = X
    x2 = x*x
    y2 = y*y
    r1 = c[0]*x2*y2 + c[1]*x*y2 + c[2]*y2 + c[3]*x2*y 
    return r1 + c[4]*x*y + c[5]*y + c[6]*x2 + c[7]*x + c[8] 


def gen_img():
    '''
        Gera imagem a partir dos coeficientes lidos no arquivo de dados.

    '''

    print "Gerando imagem aproximada ..."

    global gray_img, result_img, levels

    width, height = gray_img.size

    result_data = result_img.load()

    quads = pow(2, levels)   
    stepx = width/quads
    stepy = height/quads

    # Contador de quadrantes.
    count = 0;

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

            coefficients = coefs_data[count]
            count += 1

            # Gera valores a atribui a imagem.
            for yc in range(y, ystepy):
                for xc in range(x, xstepx): 
                    result_data[xc, yc] = int(func((xc, yc), coefficients))

            # Atualiza ponteiro horizontal.
            x = x + stepx
        # Retorna ponteiro horizontal ao inicio.
        x = 0
        # Atualiza ponteiro vertical.
        y = y+stepy

    print "Geracao concluida!"


def main(args):
    '''
        args[0]             -- Nome do arquivo com extensao.
        args[1] (opcional)  -- Salvar resultado no formato PGM.                        

    '''

    global gray_img
    global result_img
    global coefs_data
    global img_name 
    global levels

    datafile_name = args[0]
    array = datafile_name.replace("_data.txt", "").replace("-", ".").split("_")
    gray_img_name = array[0]
    levels = int(array[1])

    # Faz leitura do arquivo com os coeficientes.
    readdata(datafile_name)

    # Carrega imagem original e inicializa a resultado. 
    gray_img = Image.open(gray_img_name)
    result_img = Image.new('L', gray_img.size)

    # Gera valores dos pixels da imagem resultado.
    gen_img()

    if(len(args) > 1):
        n = datafile_name.replace(".", "_") + ".pgm"
        result_img.save(n)
        print  n, "salvo com sucesso!"

    # Mostra as duas lado a lado.
    gray_img.show(title="0 Niveis")
    result_img.show(title=str(levels)+" Niveis")


if __name__ == "__main__":
    main(sys.argv[1:])


