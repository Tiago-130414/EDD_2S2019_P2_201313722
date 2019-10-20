import socket
import select
import sys
import easygui
#curses
import curses
from SelectBlock import seleccionar
from insertBlock import cargar
from Reports import reportar
#estructuras
from Lista_Doble import Blockchain
#globales
nomArchivo = ""
seleccionarBloque =""
envio = ""
jsonR =""

def menu(window):
    titulo(window,'M E N U')
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    window.addstr(7,21,'1.- Insert Block',curses.color_pair(2))
    window.addstr(8,21,'2.- Select Block',curses.color_pair(2))
    window.addstr(9,21,'3.- Reports', curses.color_pair(2))
    window.addstr(10,21,'4.- Salir',curses.color_pair(2))
    window.timeout(-1)


def titulo(window,txt):
    window.clear()
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    pintarVentana(window)
    centro = round((60-len(txt))/2)
    window.addstr(0,centro,txt,curses.color_pair(3))

def pintarVentana(window):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    window.attron(curses.color_pair(1))
    window.border(0)
    window.attron(curses.color_pair(1))
    window.refresh() 

stdscr  = curses.initscr()
curses.start_color()
window = curses.newwin(20,60,0,0)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
menu(window)

cadenaBloques = Blockchain()
bloqueS = Blockchain()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct Usage: script, IP address, port numer")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address,Port))

opcion = -1 
while (opcion==-1):
    window.refresh()
    read_sockets = select.select([server],[],[],1)[0]
    import msvcrt
    if msvcrt.kbhit():read_sockets.append(sys.stdin)

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            bandeja = message.decode('utf-8')
            bandeja = str(bandeja)
            #print("<server>")
            #print(message.decode('utf-8'))
            if (bandeja == 'true'):
                #insertar si es true
                #agrega el json a la lista
                cadenaBloques.agregarJson(jsonR)
                easygui.msgbox("T R U E  A G R E G U E  B L O Q U E",title="<Server>")
            elif (bandeja == 'false'):
                print("falso")
                easygui.msgbox("F A L S E  N O  A G R E G U E  B L O Q U E",title="<Server>")
            elif (bandeja == 'Welcome to [EDD]Blockchain Project!'):
                print("bienvenida")
            else:
                #verificar json
                jsonR = str(bandeja)
                print(jsonR)
                bandera  = cadenaBloques.verificarJson(jsonR)
                if(bandera==True):
                    rTrue = 'true'
                    server.sendall(rTrue.encode('utf-8'))
                    easygui.msgbox("B L O Q U E  V A L I D O",title="<Verificacion Bloque>")
                elif(bandera==False):
                    rFalse = 'false'
                    server.sendall(rFalse.encode('utf-8'))
                    easygui.msgbox("B L O Q U E  N O  V A L I D O",title="<Verificacion Bloque>")
                   
        else:
            opcion = window.getch()
            if (opcion == 49):
                #cargar archivos
                nomArchivo = cargar(window)
                nomArchivo = nomArchivo.replace('\n','')
                envio = cadenaBloques.leerCsv(nomArchivo)
                message = envio
                jsonR = envio
                texto_enviar = message
                server.sendall(texto_enviar.encode('utf-8'))
               # sys.stdout.write("<you>")
                #sys.stdout.write(message)
                sys.stdout.flush()
                menu(window)
                opcion=-1
            elif (opcion == 50):
                #seleccionar bloque
                if not cadenaBloques.estaVacia():
                    seleccionar(window,cadenaBloques,bloqueS)
                menu(window)
                opcion=-1
            elif (opcion == 51):
                #reportes       
                if not bloqueS.estaVacia():
                    if not cadenaBloques.estaVacia():            
                        reportar(window,cadenaBloques,bloqueS)
                        menu(window)
                        opcion = -1
                    else:
                        menu(window)
                        opcion =-1
                else:
                    menu(window)
                    opcion =-1

            elif (opcion == 52):
                #salir
                break
            else:
                opcion =-1

curses.endwin()                
server.close()
