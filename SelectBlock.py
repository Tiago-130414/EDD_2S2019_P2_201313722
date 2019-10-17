import curses
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,KEY_ENTER
import json
def seleccionar(window,listaD = object):
    txt = ""    
    titulo(window,'S e l e c t  B l o c k')
    aux = listaD.cabeza
    pintarUsuario(window,aux)
    while True:
        salida = window.getch()
        if(salida == KEY_LEFT):
                #izquierda
                titulo(window,'S e l e c t  B l o c k')
                if(aux.anterior is not None):
                    aux = aux.anterior
                    pintarUsuario(window,aux)
                else:
                    pintarUsuario(window,aux)            
        if(salida == KEY_RIGHT):
                #derecha
                titulo(window,'S e l e c t  B l o c k')
                if(aux.siguiente is not None):
                    aux = aux.siguiente
                    pintarUsuario(window,aux)
                else:
                    pintarUsuario(window,aux)      
        if(salida == 10):
                #Seleccionar usuario con enter
                #txt = aux.usuario
                print("presione enter")
                return txt              
        if(salida == 27):
                #salida escape
                break
    
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

def pintarUsuario(window,nodo):
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        texto1 = "INDEX: " + str(nodo.indice)
        texto2 = "TIMESTAMP: " +nodo.timestamp
        texto3 = "CLASS: "+nodo.clase
        p = json.loads(nodo.data)
        texto4 = "DATA: " + str(p)[0:25]
        txt = str(p)[26:50]
        texto5 = "PREVIOUSHASH: " + nodo.previousHash[0:24]
        txt2 = nodo.previousHash[25:64]
        texto6 = "HASH: " + nodo.hashActual[0:32]
        txt3 = nodo.hashActual[33:64]
        if(len(nodo.previousHash)==4):
                window.addstr(4,15,texto1,curses.color_pair(2))
                window.addstr(5,15,texto2,curses.color_pair(2))
                window.addstr(6,15,texto3,curses.color_pair(2))
                window.addstr(7,15,texto4,curses.color_pair(2))
                window.addstr(8,15,txt,curses.color_pair(2))
                window.addstr(9,15,texto5,curses.color_pair(2))
                window.addstr(10,15,texto6,curses.color_pair(2))
                window.addstr(11,15,txt3,curses.color_pair(2))
        else:
                window.addstr(4,15,texto1,curses.color_pair(2))
                window.addstr(5,15,texto2,curses.color_pair(2))
                window.addstr(6,15,texto3,curses.color_pair(2))
                window.addstr(7,15,texto4,curses.color_pair(2))
                window.addstr(8,15,txt,curses.color_pair(2))
                window.addstr(9,15,texto5,curses.color_pair(2))
                window.addstr(10,15,txt2,curses.color_pair(2))
                window.addstr(11,15,texto6,curses.color_pair(2))
                window.addstr(12,15,txt3,curses.color_pair(2))        
        window.refresh()       