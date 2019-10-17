import curses
from curses.textpad import Textbox, rectangle
def cargar(window):
    window.clear()
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    titulo(window, "Ingrese nombre archivo csv: (Ctrl-G para cargar)")
    window.attron(curses.color_pair(4)) 
    editwin = curses.newwin(3,15, 9,25) 
    rectangle(window, 7,11, 1+11+1, 1+45+1)
    window.attron(curses.color_pair(4))
    window.refresh()
    box = Textbox(editwin)
    box.edit()
    nombreA = box.gather()
    return nombreA   

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