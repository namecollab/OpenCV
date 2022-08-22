import numpy as np
import cv2 as cv
ix,iy,sx,sy = -1,-1,-1,-1
drawing = False
pt1_x , pt1_y = None , None

def circulos(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 50, (255,0,0), -1)

def cuadrilateros(event, x, y, flags, param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img, (ix, iy), (x, y), (255,0,0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

def poligonos(event, x, y, flags, param):
    global ix,iy,sx,sy
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 3, (255,0,0), -1)
        if ix != -1:
            cv.line(img, (ix, iy), (x, y), (255,0,0), 2, cv.LINE_AA)
        else:
            sx, sy = x, y
        ix,iy = x, y
    elif event == cv.EVENT_LBUTTONDBLCLK:
        ix, iy = -1, -1
        if flags == 33:
            cv.line(img, (x, y), (sx, sy), (255,0,0), 2, cv.LINE_AA)

def dibujo_libre(event,x,y,flags,param):
    global pt1_x,pt1_y,drawing
    if event==cv.EVENT_LBUTTONDOWN:
        drawing=True
        pt1_x,pt1_y=x,y
    elif event==cv.EVENT_MOUSEMOVE:
        if drawing==True:
            cv.line(img,(pt1_x,pt1_y),(x,y),color=(255,0,0),thickness=3)
            pt1_x,pt1_y=x,y
    elif event==cv.EVENT_LBUTTONUP:
        drawing=False
        cv.line(img,(pt1_x,pt1_y),(x,y),color=(255,0,0),thickness=3)        
        
menu = {}
menu['1']="Dibujar circulos" 
menu['2']="Dibujar cuadrilateros"
menu['3']="Dibujar poligonos"
menu['4']="Dibujar libremente"
menu['5']="Salir"

while True: 
    options=menu.keys()
    sorted(options)
    for entry in options: 
        print (entry, menu[entry])

    selection=input("Please Select:") 
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('image')
    
    if selection =='1': 
        cv.setMouseCallback('image',circulos)
        while(1):
            cv.imshow('image',img)
            if cv.waitKey(20) & 0xFF == 27:
                break
        cv.destroyAllWindows() 

    elif selection == '2':
        cv.setMouseCallback('image',cuadrilateros)
        while(1):
            cv.imshow('image',img)
            if cv.waitKey(20) & 0xFF == 27:
                break
        cv.destroyAllWindows()

    elif selection == '3':
        cv.setMouseCallback('image',poligonos)
        while(1):
            cv.imshow('image',img)
            if cv.waitKey(20) & 0xFF == 27:
                break
        cv.destroyAllWindows()

    elif selection == '4':
        cv.setMouseCallback('image',dibujo_libre)
        while(1):
            cv.imshow('image',img)
            if cv.waitKey(1) & 0xFF == 27:
                break
        cv.destroyAllWindows()

    elif selection == '5':
        break 
    else: 
        print ("Opcion desconocida")