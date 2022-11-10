import cv2 as cv
import sys

'''Estoy asumiendo que las imagenes me llegan por algun motivo que tengo que descubrir
   en listas de enteros con valores grises de 0 a 255'''

def create_scale():
    scale = list()
    scale[10] = ' .:-=+*#%@'
    return scale

def transform(scale_length,x):
    '''Lo que tengo que hacer es mapear un valor de los pixeles rgb de la imagen a un valor de oscuridad
    en la escala ascii que tenemos'''
    d = 255//scale_length
    return x//d

def gray_scale_to_ascii(self, img):
    return list(map(lambda x: transform(len(create_scale()),x), img)


