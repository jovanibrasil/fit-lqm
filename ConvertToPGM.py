'''

    Autor: Jovani Brasil
    Email: jovanibrasil@gmail.com

'''

import sys
from PIL import Image

def main(args):
    '''
        args[0] Nome do arquivo a ser convertido
    '''
    name = args[0]
    print "Lendo arquivo a ser convertido ..."
    color_img = Image.open(args[0])
    name =  name[:name.index('.')]
    print "Convertendo para PGM ..."
    color_img.convert('L').save(name+'.pgm')
    print "Processo concluido!"

if __name__ == "__main__":
    main(sys.argv[1:])


