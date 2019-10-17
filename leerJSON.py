import json
import csv
import time
class archivos:

    def leerJson(self,archivoJson):
            estudiantes = json.loads(archivoJson)
            self.preordenJson(estudiantes)
          
    def preordenJson(self,estudiantes):
            if not estudiantes:
                return

            #ingresar los datos al arbol
            print(estudiantes["value"])
            self.preordenJson(estudiantes["left"])
            self.preordenJson(estudiantes["right"])
    
                    
#obj = archivos()
#obj.leerCsv()                        
     #print(estudiantes["value"])
            #print(estudiantes["left"]["value"])
            #print(estudiantes["right"]["value"])
 