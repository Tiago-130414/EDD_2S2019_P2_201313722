import curses
from curses import KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN
from SelectBlock import seleccionar
from insertBlock import cargar
from Reports import reportar
#Estructuras
from Lista_Doble import Blockchain
#manejo archivos
from leerJSON import archivos
nomArchivo =""
seleccionBloque=""
def menu(window):
    titulo(window,'M    E   N   U')
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    window.addstr(7,21,'1.-  Insert Block',curses.color_pair(2))
    window.addstr(8,21,'2.-  Select Block',curses.color_pair(2))
    window.addstr(9,21,'3.-  Reports',curses.color_pair(2))
    window.addstr(10,21,'4.-  Salir',curses.color_pair(2))
    window.timeout(-1)

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

stdscr = curses.initscr()
curses.start_color()
window = curses.newwin(20,60,0,0)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
menu(window)
manejoArchivos = archivos()
cadenaDeBloques = Blockchain()
bloqueS = Blockchain()

opcion =-1
while(opcion == -1):
    opcion = window.getch()
    if(opcion==49):
        #Insert Block
        #cargar retorna un string con el nombre de archivo que se va a cargar
        nomArchivo = cargar(window)
        nomArchivo = nomArchivo.replace('\n','')
        cadenaDeBloques.leerCsv(nomArchivo)
        menu(window) 
        opcion = -1
    elif(opcion==50):
        #Select Block
        if not cadenaDeBloques.estaVacia():
            seleccionar(window, cadenaDeBloques,bloqueS)
        menu(window)
        opcion = -1
    elif(opcion==51):
        #Reports
        if not bloqueS.estaVacia():
            if not cadenaDeBloques.estaVacia():
                reportar(window,cadenaDeBloques,bloqueS) 
                menu(window)
                opcion = -1     
        else:        
            menu(window)
            opcion = -1    
    elif(opcion==52):
        #Salir
        pass
    else:
        opcion = -1

curses.endwin()