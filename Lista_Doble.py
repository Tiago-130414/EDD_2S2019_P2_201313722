import os
import sys
import csv
import time
import json
from sha_256 import encriptar
class nodoBlockChain:
    def __init__(self, index,fechaHora,nombreClase,datosAvl,hashAnterior,hashPropio):
        self.indice = index
        self.timestamp = fechaHora
        self.clase = nombreClase
        self.data = datosAvl
        self.previousHash = hashAnterior
        self.hashActual = hashPropio
        self.siguiente = None
        self.anterior = None

class Blockchain:
    def __init__(self):
        self.cabeza = None     

    def estaVacia(self):
        return True if self.cabeza is None else False

    def agregarFinal(self,ind,FH,nomClase,datAvl,hashAnt,hashProp):
        #agrega al final de la lista
        nuevo_nodo = nodoBlockChain(ind,FH,nomClase,datAvl,hashAnt,hashProp) 
        last = self.cabeza
        nuevo_nodo.siguiente = None

        if self.cabeza is None:
            nuevo_nodo.anterior = None
            self.cabeza = nuevo_nodo
            return

        while (last.siguiente is not None):
            last = last.siguiente

        last.siguiente = nuevo_nodo
        nuevo_nodo.anterior = last        
        
    def mostrar (self):
        nodo = self.cabeza
        while (nodo is not None):
            print(str(nodo.indice) + ',' + nodo.timestamp + ',' + nodo.clase + ',' + nodo.data + ',' + str(nodo.previousHash) + ',' + str(nodo.hashActual))
            last = nodo
            nodo = nodo.siguiente
           
        print("De regreso: ")
        while(last is not None):
            print(str(last.indice) + ',' + last.timestamp + ',' + last.clase + ',' + last.data + ',' + str(last.previousHash) + ',' + str(last.hashActual))
            last = last.anterior    

    def listG(self,node):
        cad =""
        while(node is not None):
           cad += "Nodo"+str(node.indice) +"BLCHN"+str(node.clase)+ "[label=\""+"Class= "+node.clase+"\\n"+"TimeStamp= "+node.timestamp+"\\n"+"PHash= "+str(node.previousHash)+"\\n"+"HASH="+str(node.hashActual)+"\"style = filled, fillcolor = \"red:orange\"];"+"\n" 
           node = node.siguiente
        return cad

    def listarElementosLD(self,node):
        t = ""
        while(node is not None):
           if(node.siguiente!=None):
                t += "Nodo"+str(node.indice) +"BLCHN"+str(node.clase)+"->"+"Nodo"+str(node.siguiente.indice) +"BLCHN"+str(node.siguiente.clase)+"[dir=both];\n" 
           node = node.siguiente
        return t

    def graficarListaDoble(self):
        if(self.estaVacia()):
            return
        else:
            listado = self.listarElementosLD(self.cabeza)
            
            ruta_Grafica_LD = "C:/Graficas_Practica2/graficaLD.dot"
            archivo = open(ruta_Grafica_LD,'w')
            archivo.writelines("digraph{\n")
            archivo.write("rankdir=LR;\n")
            archivo.write("labelloc=\"t\";\n")
            archivo.write("subgraph cluster_0{\n")
            archivo.write("style=filled;\n")
            archivo.write("color = lightgrey;\n")  
            archivo.write("node[shape=component];\n")
            archivo.write(self.listG(self.cabeza))    
            archivo.write(listado)
            archivo.write("label = \"Block Chain\";\n")
            archivo.write("}\n")   
            archivo.write("}\n")   
            archivo.close() 
            os.system("dot C:/Graficas_Practica2/graficaLD.dot -o C:/Graficas_Practica2/graficaLD.png -Tpng -Gcharset=utf8")
            os.system("C:/Graficas_Practica2/graficaLD.png")   

    def leerCsv(self,nombreArchivo):
        bloque =""
        contador=0
        fh = self.fechaHora()
        nomClase = ""
        jsonString = ""
        hashC = ""
        hashP = ""
        cadHash =""
        with open (nombreArchivo) as File:
            lee = csv.reader(File, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            datos  = list(lee)
            #clase
            if(self.estaVacia()):
                index = 0
                hashC = "0000"
                nomClase = datos[0][1]
                jsonString = datos[1][1]
                cadHash = str(index)+fh+nomClase+jsonString+str(hashC)
                hashP = encriptar(cadHash)
                bloque = "{\n"+"\"INDEX\": "+str(index)+",\n"
                bloque += "\"TIMESTAMP\": " +"\""+ fh +"\""+",\n"
                bloque += "\"CLASS\": " +"\""+ nomClase+"\"" +",\n"
                bloque += "\"DATA\": " + jsonString +",\n"
                bloque += "\"PREVIOUSHASH\": "+"\"" + hashC +"\""+",\n"
                bloque += "\"HASH\": "+"\""+ hashP +"\""+"\n"
                bloque += "}"
                return bloque
                #self.agregarFinal(index,fh,nomClase,jsonString,hashC,hashP)
            else:
                last = self.cabeza
                while(last.siguiente is not None):
                    last = last.siguiente
                index = int(last.indice) + 1
                nomClase = datos[0][1]
                jsonString = datos[1][1]
                hashC = str(last.hashActual)
                cadHash = str(index)+fh+nomClase+jsonString+str(hashC)
                hashP = encriptar(cadHash) 
                bloque = "{\n"+"\"INDEX\": "+str(index)+",\n"
                bloque += "\"TIMESTAMP\": " +"\""+ fh +"\""+",\n"
                bloque += "\"CLASS\": " +"\""+ nomClase+"\"" +",\n"
                bloque += "\"DATA\": " + jsonString +",\n"
                bloque += "\"PREVIOUSHASH\": "+"\"" + hashC +"\""+",\n"
                bloque += "\"HASH\": "+"\""+ hashP +"\""+"\n"
                bloque += "}"
                return bloque
                #self.agregarFinal(index,fh,nomClase,jsonString,str(hashC),str(hashP))
                    
    def fechaHora(self):
        fecha=""
        hora=""
        fechaHora=""
        hora = time.strftime("%H:%M:%S")
        fecha = time.strftime("%d-%m-%y-")
        fechaHora = fecha+"::"+hora
        return fechaHora

    def retornarHashUltimo(self):
        last = self.cabeza
        has=""
        if(last.estaVacia()):
            has = "0000"
            return has
        else:    
            while(last.siguiente is not None):
                last = last.siguiente
            has = last.hashActual
            return has  

    def agregarJson(self,archivoJson):
        ind = ""
        tim=""
        cs=""
        dt=""
        ph=""
        hsh=""
        estudiante = json.loads(archivoJson)
        ind = int(estudiante['INDEX'])
        tim = str(estudiante['TIMESTAMP'])
        cs = str(estudiante['CLASS'])
        dt = json.dumps(estudiante['DATA'],indent=2)
        ph = str(estudiante['PREVIOUSHASH'])
        hsh = str(estudiante['HASH'])
        self.agregarFinal(ind,tim,cs,dt,ph,hsh)

"""lista = Blockchain()
lista.agregarFinal(1,"fecha1","EDD","prueba1",0,0)
lista.agregarFinal(2,"fecha2","EDD","prueba2",0,1)
lista.agregarFinal(3,"fecha3","EDD","prueba3",1,2)
lista.agregarFinal(4,"fecha4","EDD","prueba4",2,3)
lista.agregarFinal(5,"fecha5","EDD","prueba5",3,4)
lista.agregarFinal(6,"fecha6","EDD","prueba6",4,5)
lista.agregarFinal(7,"fecha7","EDD","prueba7",5,6)
lista.agregarFinal(8,"fecha8","EDD","prueba8",6,7)
lista.graficarListaDoble()
lista.mostrar()
"""