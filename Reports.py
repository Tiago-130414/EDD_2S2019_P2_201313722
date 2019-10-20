import curses
import time
from ArbolAVL import arbolAVL
arbolito = arbolAVL()
r = None

def reportar(window,cadenaB = object,bloqueSeleccionado = object):
    global r
    cjson = str(bloqueSeleccionado.cabeza.data)
    r = arbolito.leerJson(cjson,r)
    arbolito.actFE(r)
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
            reportarArbol(window)
            titulo(window,'R e p o r t s')
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
            window.addstr(7,19,'1.-  BlockChain Report',curses.color_pair(2))
            window.addstr(8,19,'2.-  Tree Reports',curses.color_pair(2))
            window.timeout(-1)
            opcion = -1
        elif(opcion==27):
            r = None
            return     
        else:
            opcion = -1


def reportarArbol(window):
    global r
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
            arbolito.graficarArbolAVL(r)
            window.refresh()
            opcion = -1
        elif(opcion==50):
            #inorder Report
            arbolito.limpiarV()
            ri = "INICIO->"+ str(arbolito.inOrder(r))+"->FIN"
            reportarRecorrido(window,"InOrder Traversal",str(ri))
            arbolito.graficarInOrden(r)
            print(ri)
            ri=""
            opcion = -1
        elif(opcion==51):
            #preorder Report
            arbolito.limpiarV()
            rPr = "INICIO->"+ str(arbolito.preOrder(r))+"->FIN"
            reportarRecorrido(window,"PreOrder Traversal",str(rPr))
            arbolito.graficarPreOrden(r)
            print(rPr)
            rPr=""
            opcion = -1
        elif(opcion==52):
            #postorder Report
            arbolito.limpiarV()
            rPo = "INICIO->"+ str(arbolito.postOrder(r))+"->FIN"
            reportarRecorrido(window,"PostOrder Traversal",str(rPo))
            arbolito.graficarPostOrden(r)
            print(rPo)
            rPo=""
            opcion = -1
        elif(opcion==27):
            arbolito.limpiarV()
            return     
        else:
            opcion = -1            

def rInorden(rTemp):
    pass

def rPreorden():
    pass

def rPostorden():
    pass

def reportarRecorrido(window,texto,recorrido):
    txt=""
    txt2=""
    txt3=""
    txt4=""
    txt5=""
    txt6=""
    txt7=""
    txt8=""
    txt9=""
    txt10=""
    txt11=""
    txt12=""
    txt13=""
    txt14=""
    txt15=""
    txt16=""
    longKd = len(recorrido)
    window.clear()
    curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_BLACK)
    window.attron(curses.color_pair(1))
    window.border(0)
    window.attroff(curses.color_pair(1))
    window.refresh()
    centro = round((60 - len(texto))/2)
    window.addstr(0,centro,texto,curses.color_pair(1))
    if(longKd<50):
        window.addstr(5,5,recorrido,curses.color_pair(1))
    elif(longKd>50 and longKd<=100):
        txt = recorrido[0:50]
        txt2= recorrido[51:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
    elif(longKd>100 and longKd<=150):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
    elif(longKd>150 and longKd<=200):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
    elif(longKd>200 and longKd<=250):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
    elif(longKd>250 and longKd<=300):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))
    elif(longKd>300 and longKd<=350):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
    elif(longKd>350 and longKd<=400):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
    elif(longKd>400 and longKd<=450):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
    elif(longKd>450 and longKd<=500):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:450]
        txt10 = recorrido[451:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
        window.addstr(12,5,txt10,curses.color_pair(1))
    elif(longKd>500 and longKd<=550):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:450]
        txt10 = recorrido[451:500]
        txt11 = recorrido[501:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
        window.addstr(12,5,txt10,curses.color_pair(1))
        window.addstr(13,5,txt11,curses.color_pair(1))    
    elif(longKd>550 and longKd<=600):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:450]
        txt10 = recorrido[451:500]
        txt11 = recorrido[501:550]
        txt12 = recorrido[551:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
        window.addstr(12,5,txt10,curses.color_pair(1))
        window.addstr(13,5,txt11,curses.color_pair(1))
        window.addstr(14,5,txt12,curses.color_pair(1))    
    elif(longKd>600 and longKd<=650):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:450]
        txt10 = recorrido[451:500]
        txt11 = recorrido[501:550]
        txt12 = recorrido[551:600]
        txt13 = recorrido[601:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
        window.addstr(12,5,txt10,curses.color_pair(1))
        window.addstr(13,5,txt11,curses.color_pair(1))
        window.addstr(14,5,txt12,curses.color_pair(1))
        window.addstr(15,5,txt13,curses.color_pair(1))    
    elif(longKd>650 and longKd<=700):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:450]
        txt10 = recorrido[451:500]
        txt11 = recorrido[501:550]
        txt12 = recorrido[551:600]
        txt13 = recorrido[601:650]
        txt14 = recorrido[651:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
        window.addstr(12,5,txt10,curses.color_pair(1))
        window.addstr(13,5,txt11,curses.color_pair(1))
        window.addstr(14,5,txt12,curses.color_pair(1))
        window.addstr(15,5,txt13,curses.color_pair(1))    
        window.addstr(16,5,txt14,curses.color_pair(1))    
    elif(longKd>700 and longKd<=750):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:450]
        txt10 = recorrido[451:500]
        txt11 = recorrido[501:550]
        txt12 = recorrido[551:600]
        txt13 = recorrido[601:650]
        txt14 = recorrido[651:700]
        txt15 = recorrido[701:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
        window.addstr(12,5,txt10,curses.color_pair(1))
        window.addstr(13,5,txt11,curses.color_pair(1))
        window.addstr(14,5,txt12,curses.color_pair(1))
        window.addstr(15,5,txt13,curses.color_pair(1))    
        window.addstr(16,5,txt14,curses.color_pair(1))
        window.addstr(17,5,txt15,curses.color_pair(1))  
    elif(longKd>750 and longKd<=800):
        txt = recorrido[0:50]
        txt2= recorrido[51:100]
        txt3= recorrido[101:150]
        txt4 = recorrido[151:200]
        txt5 = recorrido[201:250]
        txt6 = recorrido[251:300]
        txt7 = recorrido[301:350]
        txt8 = recorrido[351:400]
        txt9 = recorrido[401:450]
        txt10 = recorrido[451:500]
        txt11 = recorrido[501:550]
        txt12 = recorrido[551:600]
        txt13 = recorrido[601:650]
        txt14 = recorrido[651:700]
        txt15 = recorrido[701:750]
        txt16 = recorrido[751:len(recorrido)]
        window.addstr(3,5,txt,curses.color_pair(1))
        window.addstr(4,5,txt2,curses.color_pair(1))
        window.addstr(5,5,txt3,curses.color_pair(1))
        window.addstr(6,5,txt4,curses.color_pair(1))
        window.addstr(7,5,txt5,curses.color_pair(1))
        window.addstr(8,5,txt6,curses.color_pair(1))        
        window.addstr(9,5,txt7,curses.color_pair(1))        
        window.addstr(10,5,txt8,curses.color_pair(1))
        window.addstr(11,5,txt9,curses.color_pair(1))
        window.addstr(12,5,txt10,curses.color_pair(1))
        window.addstr(13,5,txt11,curses.color_pair(1))
        window.addstr(14,5,txt12,curses.color_pair(1))
        window.addstr(15,5,txt13,curses.color_pair(1))    
        window.addstr(16,5,txt14,curses.color_pair(1))
        window.addstr(17,5,txt15,curses.color_pair(1))
        window.addstr(18,5,txt16,curses.color_pair(1))    
    
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
    