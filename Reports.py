import curses
import time
from ArbolAVL import arbolAVL
arbolito = arbolAVL()
r = None

def reportar(window,cadenaB = object,bloqueSeleccionado = object):
    titulo(window,'R e p o r t s')
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    window.addstr(7,19,'1.-  BlockChain Report',curses.color_pair(2))
    window.addstr(8,19,'2.-  Tree Reports',curses.color_pair(2))
    window.timeout(-1)
    opcion =-1
    while(opcion ==-1):
        opcion = window.getch()
        if(opcion==49):
            #blockchain Report
            cadenaB.graficarListaDoble()
            opcion = -1               
        elif(opcion==50):
            #tree Report
            cjson = str(bloqueSeleccionado.cabeza.data)
            reportarArbol(window,cjson)
            titulo(window,'R e p o r t s')
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
            window.addstr(7,19,'1.-  BlockChain Report',curses.color_pair(2))
            window.addstr(8,19,'2.-  Tree Reports',curses.color_pair(2))
            window.timeout(-1)
            opcion = -1
        elif(opcion==27):
            return     
        else:
            opcion = -1


def reportarArbol(window,cadJs):
    global r
    r = arbolito.leerJson(cadJs,r)
    titulo(window,'T r e e  R e p o r t s')
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    window.addstr(7,19,'1.-  Show Tree',curses.color_pair(2))
    window.addstr(8,19,'2.-  InOrder Traversal',curses.color_pair(2))
    window.addstr(9,19,'3.-  PreOrder Traversal',curses.color_pair(2))
    window.addstr(10,19,'4.-  PostOrder Traversal',curses.color_pair(2))
    window.timeout(-1)
    opcion =-1
    while(opcion ==-1):
        opcion = window.getch()
        if(opcion==49):
            #show tree Report
            arbolito.limpiarV()
            #r = arbolito.leerJson(cadJs,r)
            arbolito.graficarArbolAVL(r)
            window.refresh()
            opcion = -1
        elif(opcion==50):
            #inorder Report
            arbolito.limpiarV()
            #r = arbolito.leerJson(cadJs,r)
            arbolito.graficarInOrden(r)
            opcion = -1
        elif(opcion==51):
            #preorder Report
            arbolito.limpiarV()
            #r = arbolito.leerJson(cadJs,r)
            arbolito.graficarPreOrden(r)
            opcion = -1
        elif(opcion==52):
            #postorder Report
            arbolito.limpiarV()
            #r = arbolito.leerJson(cadJs,r)
            arbolito.graficarPostOrden(r)
            opcion = -1
        elif(opcion==27):
            arbolito.limpiarV()
            r=None
            return     
        else:
            opcion = -1            
    
def titulo(window,texto):
    window.clear()
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    pintarVentana(window)
    centro = round((60-len(texto))/2)
    window.addstr(0,centro,texto,curses.color_pair(3))
    
def pintarVentana(window):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    window.attron(curses.color_pair(1))
    window.border(0)
    window.attroff(curses.color_pair(1))
    window.refresh()  
    