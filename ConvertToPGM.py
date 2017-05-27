import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.optimize as optimization
from PIL import Image

def main(args):
    '''
        args[0] Nome do arquivo a ser convertido
    '''
    name = args[0]
    color_img = Image.open(args[0])
    name =  name[:name.index('.')]
    color_img.convert('L').save(name+'.pgm')

if __name__ == "__main__":
    main(sys.argv[1:])


