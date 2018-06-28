import cv2
import numpy as np
import copy
import array
from matplotlib import pyplot as plt

def vizinhos(img, y, x):
    vizinhos = [];
    if (y + 1 < len(img)):
        vizinhos.append((y + 1, x));
    if (y - 1 >= 0):
        vizinhos.append((y - 1, x));
    if (x + 1 < len(img[y])):
        vizinhos.append((y, x + 1));
    if (x - 1 >= 0):
        vizinhos.append((y, x - 1));
    return vizinhos;

def bfs(img, ponto, rotulo):
    y, x = ponto
    img[y][x] = rotulo
    fila = [ponto];
    while fila:
        y, x = fila.pop()
        for vizinho in vizinhos(img, y, x):
            y_v, x_v = vizinho;
            rv = img[y_v][x_v];
            if (rv > 0 and rv != rotulo):
                img[y_v][x_v] = rotulo;
                fila.append(vizinho);

# conta quantidade de objetos em uma imagem binaria
def contar_objetos(img):
    rotulo = 5
    total = 0;
    for y in range(0, len(img)):
        for x in range(0, len(img[y])):
            rv = img[y][x];
            if rv == 255 and rv != rotulo:
                total += 1;
                bfs(img, (y, x), rotulo);
        	rotulo += 10  
    print 'Quantidade:', total - 1;

imgo = cv2.imread('img01-a.png')
img = cv2.cvtColor(imgo,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(5,5),0)
kernel = np.ones((2,2),np.uint8)
ret, thr = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
thrd = cv2.dilate(thr,kernel,None,None,3)
thre = cv2.erode(thrd,kernel)
opening = cv2.morphologyEx(thre,cv2.MORPH_OPEN,kernel, iterations = 1)
contar_objetos(opening)
cv2.imwrite('ativt.png',opening) 
cv2.imshow('original',img)
cv2.imshow('dilate',thrd)
cv2.imshow('erode',thre)
cv2.imshow('opening',opening)
k = cv2.waitKey(0)
if k == 27:
       cv2.destroyAllWindows()