import sys
import os
import json
from os import remove
#arbol completo
cad =""
cad2=""
#arbol recorrido inorden
cadInO=""
cadInO2=""
rIn=""
#arbol recorrido postorden
cadPost=""
cadPost2=""
rPo=""
#arbol recorrido preorden
cadPre=""
cadPre2=""
rPre=""
List=[]
class nodoArbol(object): 
    def __init__(self, carnet, nombre):
        self.nombre = nombre 
        self.carnet = carnet 
        self.izquierda = None
        self.derecha = None
        self.altura = 1
        self.FE = 0
  
class arbolAVL(object): 
    
    def insertar(self, raiz, cnt, nom): 
      
        if not raiz: 
            return nodoArbol(cnt,nom) 
        elif cnt < raiz.carnet: 
            raiz.izquierda = self.insertar(raiz.izquierda, cnt, nom) 
        else: 
            raiz.derecha = self.insertar(raiz.derecha, cnt, nom) 
  
        raiz.altura = 1 + max(self.getAltura(raiz.izquierda), 
                           self.getAltura(raiz.derecha)) 
  
        
        raiz.FE = self.getBalance(raiz)
        balance = self.getBalance(raiz) 
  
        # Caso 1 - izquierda  izquierda 
        if balance > 1 and cnt < raiz.izquierda.carnet: 
            return self.rotacionDerecha(raiz) 
  
        # Caso 2 - derecha derecha 
        if balance < -1 and cnt > raiz.derecha.carnet: 
            return self.rotacionIzquierda(raiz) 
  
        # Caso 3 - izquierda derecha 
        if balance > 1 and cnt > raiz.izquierda.carnet: 
            raiz.izquierda = self.rotacionIzquierda(raiz.izquierda) 
            return self.rotacionDerecha(raiz) 
  
        # Caso 4 - derecha izquierda
        if balance < -1 and cnt < raiz.derecha.carnet: 
            raiz.derecha = self.rotacionDerecha(raiz.derecha) 
            return self.rotacionIzquierda(raiz) 
        
        
        return raiz 
  
    def actFE(self,raiz):
        if raiz:
           self.actFE(raiz.izquierda)
           fe = self.getBalance(raiz)
           raiz.FE = fe
           self.actFE(raiz.derecha)
            
    def rotacionIzquierda(self, z): 
  
        y = z.derecha 
        T2 = y.izquierda 
   
        y.izquierda = z 
        z.derecha = T2 
  
        z.altura = 1 + max(self.getAltura(z.izquierda), 
                         self.getAltura(z.derecha)) 
        y.altura = 1 + max(self.getAltura(y.izquierda), 
                         self.getAltura(y.derecha)) 
  
        return y 
  
    def rotacionDerecha(self, z): 
  
        y = z.izquierda 
        T3 = y.derecha 
  
        y.derecha = z 
        z.izquierda = T3 
  
        z.altura = 1 + max(self.getAltura(z.izquierda), 
                        self.getAltura(z.derecha)) 
        y.altura = 1 + max(self.getAltura(y.izquierda), 
                        self.getAltura(y.derecha)) 
  
        return y 
  
    def getAltura(self, raiz): 
        if not raiz: 
            return 0
  
        return raiz.altura 
  
    def getBalance(self, raiz): 
        if not raiz: 
            return 0
  
        return self.getAltura(raiz.izquierda) - self.getAltura(raiz.derecha) 
    #recorrido de arbol

    def preOrder(self, raiz): 
        global rPre
        if raiz: 
            rPre += raiz.carnet +"-"+raiz.nombre+"->"
            self.preOrder(raiz.izquierda) 
            self.preOrder(raiz.derecha)
        return rPre 

    def inOrder(self, raiz):
        global rIn
        if raiz:
            self.inOrder(raiz.izquierda) 
            rIn += raiz.carnet +"-"+raiz.nombre+"->"
            self.inOrder(raiz.derecha)    
        return rIn

    def postOrder(self,raiz):
        global rPo
        if raiz:
           self.postOrder(raiz.izquierda) 
           self.postOrder(raiz.derecha)    
           rPo += raiz.carnet +"-"+raiz.nombre+"->" 
        return rPo
    #grafica arbol completo

    def listadoNodos(self, raiz):
        global cad
        if raiz:
            self.listadoNodos(raiz.izquierda)
            cad +="\tNodo"+str(raiz.nombre)+"[label=\"<izquierda>|"+"carne: "+str(raiz.carnet)+"\\n"+"nombre: "+str(raiz.nombre)+"\\n"+"altura: "+str(raiz.altura)+"\\n"+"FE:"+str(raiz.FE)+"|<derecha>\"];\n"
            self.listadoNodos(raiz.derecha) 
        return cad         

    def apuntadores(self, raiz):
        global cad2
        if not raiz:
            return cad2
        else:
            self.apuntadores(raiz.izquierda)

            if raiz.izquierda is not None:
                cad2 += "\tNodo"+raiz.nombre+":izquierda->Nodo"+raiz.izquierda.nombre+";\n";
       
            if raiz.derecha is not None:
                cad2 += "\tNodo"+raiz.nombre+":derecha->Nodo"+raiz.derecha.nombre+";\n";

            self.apuntadores(raiz.derecha)    
        return cad2

    def graficarArbolAVL(self,raiz):
        List.clear()
        if not raiz:
            return
        else:
            cadena ="\t"
            cadena2 = ""
            ruta_Grafica_LD = "C:/Graficas_Practica2/graficaArbolAVL.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph ArbolAVL{\n")
            archivo.write("\trankdir=TB;\n")
            archivo.write("\tordering=out;")
            archivo.write("\tgraph [splines=compound,nodesep=0.5]")
            archivo.write("\tsubgraph cluster_0{\n")
            archivo.write("\tstyle=filled;\n")
            archivo.write("\tcolor = grey;\n")  
            archivo.write("\tlabelloc=\"t\";\n")
            archivo.write("\tnode[shape = record, style=\"rounded,filled\", fillcolor=\"orange:red\",width=0.7,height=0.5];\n")
            cadena = self.listadoNodos(raiz)
            archivo.write(cadena)
            cadena2 = self.apuntadores(raiz)    
            archivo.write(cadena2)
            archivo.write("\tlabel = \"Arbol AVL\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close() 
            os.system("dot C:/Graficas_Practica2/graficaArbolAVL.dot -o C:/Graficas_Practica2/graficaArbolAVL.png -Tpng -Gcharset=utf8")
            os.system("C:/Graficas_Practica2/graficaArbolAVL.png")       

    def limpiarV(self):
        #arbol completo
        global cad 
        global cad2
        cad =""
        cad2=""
        #arbol recorrido inorden                
        global cadInO
        global cadInO2
        cadInO=""
        cadInO2=""
        #arbol recorrido postorden
        global cadPost
        global cadPost2
        cadPost=""
        cadPost2=""
        #arbol recorrido preorden
        global cadPre
        global cadPre2
        cadPre=""
        cadPre2=""
        #recorridos en consola
        global rIn
        global rPre
        global rPo
        rIn = ""
        rPre = ""
        rPo = ""
    # grafica recorrido inorden        
    def listadoNodosInO(self,raiz):
        global cadInO
        if raiz:
            self.listadoNodosInO(raiz.izquierda)
            cadInO +="\tNodo"+str(raiz.nombre)+"C"+str(raiz.carnet)+"[label=\""+"carne: "+str(raiz.carnet)+"\\n"+"nombre: "+str(raiz.nombre)+"\"];\n"
            self.listadoNodosInO(raiz.derecha) 
        return cadInO   

    def apuntadoresInO(self,raiz):
        global cadInO2
        if not raiz:
            return cadInO2
        else:
            self.apuntadoresInO(raiz.izquierda)
            cadInO2 += "\tNodo"+raiz.nombre+"C"+str(raiz.carnet)+"->";
            self.apuntadoresInO(raiz.derecha)
        return cadInO2    

    def graficarInOrden(self,raiz):
        temp = 0
        if not raiz:
            return
        else:
            cadena3 ="\t"
            cadena4 = ""
            ruta_Grafica_LD = "C:/Graficas_Practica2/graficaArbolAVLInO.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph ArbolAVLInOrden{\n")
            archivo.write("\trankdir=LR;\n")
            archivo.write("\tordering=out;")
            archivo.write("\tgraph [splines=compound,nodesep=0.5]")
            archivo.write("\tsubgraph cluster_0{\n")
            archivo.write("\tstyle=filled;\n")
            archivo.write("\tcolor = grey;\n")  
            archivo.write("\tlabelloc=\"t\";\n")
            archivo.write("\tnode[shape = record, style=\"rounded,filled\", fillcolor=\"orange:red\",width=0.7,height=0.5];\n")
            cadena3 = self.listadoNodosInO(raiz)
            archivo.write(cadena3)
            cadena4 = self.eliminarUlt(self.apuntadoresInO(raiz))
            archivo.write(cadena4)
            archivo.write("\tlabel = \"Arbol AVL InOrden\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close() 
            os.system("dot C:/Graficas_Practica2/graficaArbolAVLInO.dot -o C:/Graficas_Practica2/graficaArbolAVLInO.png -Tpng -Gcharset=utf8")
            os.system("C:/Graficas_Practica2/graficaArbolAVLInO.png")  
            self.inOrder(raiz)
            global cadInO
            global cadInO2
            cadInO=""
            cadInO2=""

    #grafica recorrido preorden
    def listadoNodosPreO(self,raiz):
        global cadPre
        if raiz:              
            cadPre +="\tNodo"+str(raiz.nombre)+"[label=\""+"carne: "+str(raiz.carnet)+"\\n"+"nombre: "+str(raiz.nombre)+"\"];\n"
            self.listadoNodosPreO(raiz.izquierda)
            self.listadoNodosPreO(raiz.derecha) 
        return cadPre   

    def apuntadoresPreO(self,raiz):
        global cadPre2
        if not raiz:
            return cadPre2
        else:
            
            cadPre2 += "\tNodo"+raiz.nombre+"->";
            self.apuntadoresPreO(raiz.izquierda)
            self.apuntadoresPreO(raiz.derecha)
        return cadPre2           

    def graficarPreOrden(self,raiz):
        temp = 0
        if not raiz:
            return
        else:
            cadena5 ="\t"
            cadena6 = ""
            ruta_Grafica_LD = "C:/Graficas_Practica2/graficaArbolAVLPreO.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph ArbolAVLPreOrden{\n")
            archivo.write("\trankdir=LR;\n")
            archivo.write("\tordering=out;")
            archivo.write("\tgraph [splines=compound,nodesep=0.5]")
            archivo.write("\tsubgraph cluster_0{\n")
            archivo.write("\tstyle=filled;\n")
            archivo.write("\tcolor = grey;\n")  
            archivo.write("\tlabelloc=\"t\";\n")
            archivo.write("\tnode[shape = record, style=\"rounded,filled\", fillcolor=\"orange:red\",width=0.7,height=0.5];\n")
            cadena5 = self.listadoNodosPreO(raiz)
            archivo.write(cadena5)
            cadena6 = self.eliminarUlt(self.apuntadoresPreO(raiz))
            archivo.write(cadena6)
            archivo.write("\tlabel = \"Arbol AVL PreOrden\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close() 
            os.system("dot C:/Graficas_Practica2/graficaArbolAVLPreO.dot -o C:/Graficas_Practica2/graficaArbolAVLPreO.png -Tpng -Gcharset=utf8")
            os.system("C:/Graficas_Practica2/graficaArbolAVLPreO.png")  
            self.preOrder(raiz)
            global cadPre
            global cadPre2
            cadPre=""
            cadPre2=""

    #grafica recorrido postorden
    
    def listadoNodosPostO(self,raiz):
        global cadPost
        if raiz:              
            self.listadoNodosPostO(raiz.izquierda)
            self.listadoNodosPostO(raiz.derecha)
            cadPost +="\tNodo"+str(raiz.nombre)+"[label=\""+"carne: "+str(raiz.carnet)+"\\n"+"nombre: "+str(raiz.nombre)+"\"];\n"
        return cadPost  

    def apuntadoresPostO(self,raiz):
        global cadPost2
        if not raiz:
            return cadPost2
        else:
            self.apuntadoresPostO(raiz.izquierda)
            self.apuntadoresPostO(raiz.derecha)
            cadPost2 += "\tNodo"+raiz.nombre+"->";
        return cadPost2  

    def graficarPostOrden(self,raiz):
        temp = 0
        if not raiz:
            return
        else:
            cadena7 ="\t"
            cadena8 = ""
            ruta_Grafica_LD = "C:/Graficas_Practica2/graficaArbolAVLPostO.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph ArbolAVLPostOrden{\n")
            archivo.write("\trankdir=LR;\n")
            archivo.write("\tordering=out;")
            archivo.write("\tgraph [splines=compound,nodesep=0.5]")
            archivo.write("\tsubgraph cluster_0{\n")
            archivo.write("\tstyle=filled;\n")
            archivo.write("\tcolor = grey;\n")  
            archivo.write("\tlabelloc=\"t\";\n")
            archivo.write("\tnode[shape = record, style=\"rounded,filled\", fillcolor=\"orange:red\",width=0.7,height=0.5];\n")
            cadena7 = self.listadoNodosPostO(raiz)
            archivo.write(cadena7)
            cadena8 = self.eliminarUlt(self.apuntadoresPostO(raiz))
            archivo.write(cadena8)
            archivo.write("\tlabel = \"Arbol AVL PostOrden\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close() 
            os.system("dot C:/Graficas_Practica2/graficaArbolAVLPostO.dot -o C:/Graficas_Practica2/graficaArbolAVLPostO.png -Tpng -Gcharset=utf8")
            os.system("C:/Graficas_Practica2/graficaArbolAVLPostO.png")  
            cadPost=""
            cadPost2=""
    #eliminar flechita final
    def eliminarUlt(self,cd):
        temp = len(cd)
        cadenaSF = cd[:temp-2]
        return cadenaSF

    def leerJson(self,archivoJson,r=object):
            estudiantes = json.loads(archivoJson)
            self.preordenJson(estudiantes)
            r = self.insertarC(r)
            return r

    def preordenJson(self,estudiantes):
            if not estudiantes:
                return
            #ingresar los datos al arbol
            est = estudiantes["value"]
            List.append(est)
            #lt = est.split('-')
            #nombre = lt[1]
            #carne = lt[0]
            #raiz = self.insertar(raiz,int(carne),nombre)
            self.preordenJson(estudiantes["left"])
            self.preordenJson(estudiantes["right"])

    def insertarC(self, r=object):
        
        carne=""
        nombre=""
        for x in range(0,len(List)):
            lt = List[x].split('-')
            nombre = lt[1]
            carne = lt[0]
            r = self.insertar(r,carne,nombre)
        return r        

"""myTree = arbolAVL() 
raiz = None
  
raiz = myTree.insertar(raiz, 201403525,"Nery") 
raiz = myTree.insertar(raiz, 201212963,"Andres") 
raiz = myTree.insertar(raiz, 201005874,"Estudiante1") 
raiz = myTree.insertar(raiz, 201313526,"Alan") 
raiz = myTree.insertar(raiz, 201403819,"Anne") 
raiz = myTree.insertar(raiz, 201403624,"Fernando")
raiz = myTree.insertar(raiz, 201602255,"Estudiante2") 
  
print("pre orden")  
myTree.preOrder(raiz)
print()
print("in orden")
myTree.inOrder(raiz)
print()
print("post order")
myTree.postOrder(raiz) 

myTree.graficarArbolAVL(raiz)
myTree.graficarPreOrden(raiz)
myTree.graficarInOrden(raiz)
myTree.graficarPostOrden(raiz)
"""